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
        self.__lastEventTypeId = None
        self.lastTeamWithBall = None
        self.__last = -1
        self.__play_segment_window_size = play_segment_window
        self.__pitch_location_service = PitchLocation()
        self.__x_bins = x_bins
        self.__y_bins = y_bins

    def createEventsEntropyMaps(self, match):
        home_ps = self.makePlaySegments(match.home.possesion_strings)
        away_ps = self.makePlaySegments(match.away.possesion_strings)
        return self.createEventsEntropyMap(home_ps), self.createEventsEntropyMap(away_ps)

    def createEventsEntropyMap(self, play_segments):
        bins_map = []
        vertical_bins_ranges, horizontal_bins_ranges = self.__pitch_location_service.createPitchBins(self.__x_bins, self.__y_bins)
        for i in range(0, len(vertical_bins_ranges)*len(horizontal_bins_ranges)):
            bins_map.append([])
        # bins_map = np.zeros(shape=(len(vertical_bins_ranges)*len(horizontal_bins_ranges),len(vertical_bins_ranges)*len(horizontal_bins_ranges)))
        entropy_map = np.zeros(len(vertical_bins_ranges)*len(horizontal_bins_ranges))
        for play_segment in play_segments:
            if play_segment[0].location is not None:
                first_event_bin = self.__pitch_location_service.findPitchBin(play_segment[0].location, vertical_bins_ranges, horizontal_bins_ranges)
                for event in play_segment[1:]:
                    if event.location is not None:
                        # bins_map[first_event_bin, self.__pitch_location_service.findPitchBin(event.location, vertical_bins_ranges, horizontal_bins_ranges)] += 1
                        bins_map[first_event_bin].append(self.__pitch_location_service.findPitchBin(event.location, vertical_bins_ranges, horizontal_bins_ranges))
        for i in range(0, len(bins_map)):
            entropy_map[i] = self.compute_entropy(bins_map[i])

        return entropy_map


    def makePlaySegments(self, possession_strings):
        play_segments = []
        for string in self.removeTooShortPossessionStrings(possession_strings):
            play_segments += [x for x in self.window(string, self.__play_segment_window_size)]

        return play_segments

    def getPossessionStrings(self, match):
        home_strings = []
        away_strings = []
        for event in match.events:
            if event.gotPlayer() and not Event.isBallReceipt(event):
                if self.isPossessionStringStartingAt(event):
                    if event.team.name == match.home.team_name:
                        home_strings.append([event])
                    else:
                        away_strings.append([event])
                elif self.isPossessionStringEndingAt(event):
                    pass
                else:
                    if self.isAttackingTeamEvent(event) and self.isNotPressing(event):
                        if event.team.name == match.home.team_name:
                            home_strings[self.__last].append(event)
                        else:
                            away_strings[self.__last].append(event)
            self.__lastEventTypeId = event.type.id

        return home_strings, away_strings

    def isPossessionStringStartingAt(self, event):
        decision = self.isSetPiece(event) or Pass.isKickOff(event) \
               or Pass.isPassFromGoalKick(event) or (not self.isTeamStillInPossesionAt(event)) \
                or Interception.isClearance(event)
        if not self.isTeamStillInPossesionAt(event):
            self.changeTeamInPossesionFor(self.getTeamInPossesionAt(event))
        return decision

    def isSetPiece(self, event):
        return Pass.isPassFromSetPiece(event) or Shot.isShotFromSetPiece(event)

    def isTeamStillInPossesionAt(self, event):
        return self.lastTeamWithBall == event.possession_team.name

    def getTeamInPossesionAt(self, event):
        return event.getPossessionTeamName()

    def changeTeamInPossesionFor(self, team):
        self.lastTeamWithBall = team

    def isPossessionStringEndingAt(self, event):
        return Half.isEndHalf(event) # or Faul.isFaul(event)

    def isAttackingTeamEvent(self, event):
        return self.lastTeamWithBall == event.team.name

    def isNotPressing(self, event):
        return event.type.name != 'Pressure'

    def removeTooShortPossessionStrings(self, sequences):
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










