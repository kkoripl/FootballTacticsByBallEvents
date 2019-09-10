from itertools import islice

import numpy as np
from scipy.stats import entropy

from codes.models.stats_bomb.data_preparation_models.pitch_location import PitchLocation
from codes.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event
from codes.models.stats_bomb.services.events_services.particular_events.half_service import Half
from codes.models.stats_bomb.services.events_services.particular_events.interception_service import Interception
from codes.models.stats_bomb.services.events_services.particular_events.shot_service import Shot


class PossessionStringsService:

    def __init__(self, play_segment_window, x_bins, y_bins):
        self.__last_event_type_id = None
        self.last_team_w_ball = None
        self.__last = -1
        self.__play_segment_window_size = play_segment_window
        self.__pitch_location_service = PitchLocation()
        self.__x_bins = x_bins
        self.__y_bins = y_bins

    def create_events_entropy_maps(self, match):
        home_ps = self.make_play_segments(match.home.possesion_strings)
        away_ps = self.make_play_segments(match.away.possesion_strings)
        return self.create_events_entropy_map(home_ps), self.create_events_entropy_map(away_ps)

    def create_events_entropy_map(self, play_segments):
        bins_map = []
        vertical_bins_ranges, horizontal_bins_ranges = self.__pitch_location_service.create_pitch_bins(self.__x_bins,
                                                                                                       self.__y_bins)
        for i in range(0, len(vertical_bins_ranges) * len(horizontal_bins_ranges)):
            bins_map.append([])
        # bins_map = np.zeros(shape=(len(vertical_bins_ranges)*len(horizontal_bins_ranges),len(vertical_bins_ranges)*len(horizontal_bins_ranges)))
        entropy_map = np.zeros(len(vertical_bins_ranges) * len(horizontal_bins_ranges))
        for play_segment in play_segments:
            if play_segment[0].location is not None:
                first_event_bin = self.__pitch_location_service.find_pitch_bin(play_segment[0].location,
                                                                               vertical_bins_ranges,
                                                                               horizontal_bins_ranges)
                for event in play_segment[1:]:
                    if event.location is not None:
                        # bins_map[first_event_bin, self.__pitch_location_service.findPitchBin(event.location, vertical_bins_ranges, horizontal_bins_ranges)] += 1
                        bins_map[first_event_bin].append(
                            self.__pitch_location_service.find_pitch_bin(event.location, vertical_bins_ranges,
                                                                         horizontal_bins_ranges))
        for i in range(0, len(bins_map)):
            entropy_map[i] = self.compute_entropy(bins_map[i])

        return entropy_map

    def make_play_segments(self, possession_strings):
        play_segments = []
        for string in self.remove_too_short_possession_strings(possession_strings):
            play_segments += [x for x in self.window(string, self.__play_segment_window_size)]

        return play_segments

    def get_possession_strings(self, match):
        home_strings = []
        away_strings = []
        for event in match.events:
            if event.got_player() and not Event.is_ball_receipt(event):
                if self.is_possession_string_starting_at(event):
                    if event.team.name == match.home.team_name:
                        home_strings.append([event])
                    else:
                        away_strings.append([event])
                elif self.is_possession_string_ending_at(event):
                    pass
                else:
                    if self.is_attacking_team_event(event) and self.is_not_pressing(event):
                        if event.team.name == match.home.team_name:
                            home_strings[self.__last].append(event)
                        else:
                            away_strings[self.__last].append(event)
            self.__last_event_type_id = event.type.id

        return home_strings, away_strings

    def is_possession_string_starting_at(self, event):
        decision = self.is_set_piece(event) or Pass.is_kick_off(event) \
                   or Pass.is_pass_from_goal_kick(event) or (not self.is_team_still_in_possession_at(event)) \
                   or Interception.isClearance(event)
        if not self.is_team_still_in_possession_at(event):
            self.change_team_in_possession_to(self.get_team_in_possession_at(event))
        return decision

    def is_set_piece(self, event):
        return Pass.is_pass_from_set_piece(event) or Shot.is_shot_from_set_piece(event)

    def is_team_still_in_possession_at(self, event):
        return self.last_team_w_ball == event.possession_team.name

    def get_team_in_possession_at(self, event):
        return event.get_possession_team_name()

    def change_team_in_possession_to(self, team):
        self.last_team_w_ball = team

    def is_possession_string_ending_at(self, event):
        return Half.is_end_half(event)  # or Faul.isFaul(event)

    def is_attacking_team_event(self, event):
        return self.last_team_w_ball == event.team.name

    def is_not_pressing(self, event):
        return event.type.name != 'Pressure'

    def remove_too_short_possession_strings(self, sequences):
        return [sequence for sequence in sequences if len(sequence) >= self.__play_segment_window_size]

    def window(self, seq, n=2):
        "Returns a sliding window (of width n) over data from the iterable"
        "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
        it = iter(seq)
        result = tuple(islice(it, n))
        if len(result) == n:
            yield result
        for elem in it:
            result = result[1:] + (elem,)
            yield result

    def compute_entropy(self, labels, base=None):
        value, counts = np.unique(labels, return_counts=True)
        return entropy(counts, base=base)
