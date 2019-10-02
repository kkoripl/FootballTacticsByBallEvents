from codes.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class PassMapsService:

    def grant_passes_to_players(self, team, events):
        passes = self.__get_passes_till_team_changed(team.team_id, events)
        for pass_event in passes:
            if Event.is_team_event(pass_event, team.team_id):
                passer = team.get_player(Event.get_player_id(pass_event))
                passer.passes.append(pass_event)

    def count_std_pass_map_connections(self, team):
        for passer in team.lineup:
            passer.passes_cnt = {}
            for pass_event in passer.passes:
                receiver = team.get_player(Pass.get_recipient_id(pass_event))
                self.__increment_player_std_pass_cnt(passer, receiver)

    def count_positional_pass_map_connections(self, loc_x_min, team):
        for passer in team.lineup:
            passer.passes_cnt = {}
            for pass_event in passer.passes:
                if Pass.get_x_end_location(pass_event) >= loc_x_min:
                    receiver = team.get_player(Pass.get_recipient_id(pass_event))
                    self.__increment_player_std_pass_cnt(passer, receiver)

    def count_under_pressure_pass_map_connections(self, team):
        for passer in team.lineup:
            passer.passes_cnt = {}
            for pass_event in passer.passes:
                if pass_event.under_pressure:
                    receiver = team.get_player(Pass.get_recipient_id(pass_event))
                    self.__increment_player_std_pass_cnt(passer, receiver)

    def __get_passes_till_team_changed(self, team_id, events):
        passes = []
        for i in range(0, len(events)):
            event = events[i]
            if Pass.is_pass(event) and Pass.is_pass_completed(event) and Event.is_team_event(event, team_id):
                passes.append(event)
            elif Event.is_substitiution(event) or Event.player_sent_off(event):
                return passes

    def __increment_player_std_pass_cnt(self, passer, recipient):
        if recipient.player_id in passer.passes_cnt:
            passer.passes_cnt[recipient.player_id] += 1
            recipient.passes_cnt[passer.player_id] += 1
        else:
            passer.passes_cnt[recipient.player_id] = 1
            recipient.passes_cnt[passer.player_id] = 1


