from models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from models.stats_bomb.services.events_services.particular_events.event_service import Event


class PassMapsService:

    def create_players_pass_map(self, team, events):
        passes = self.__get_passes_till_team_changed(team.team_id, events)
        for ball_pass in passes:
            if Event.is_team_event(ball_pass, team.team_id):
                passer = team.get_player(Event.get_player_id(ball_pass))
                receiver = team.get_player(Pass.get_recipient_id(ball_pass))
                self.__increment_players_passes_cnt(passer, receiver)

    def __get_passes_till_team_changed(self, team_id, events):
        passes = []
        for i in range(0, len(events)):
            event = events[i]
            if Pass.is_pass(event) and Pass.is_pass_completed(event) and Event.is_team_event(event, team_id):
                passes.append(event)
            elif Event.is_substitiution(event) or Event.player_sent_off(event):
                return passes

    def __increment_players_passes_cnt(self, passer, recipient):
        if recipient.player_id in passer.passes_cnt:
            passer.passes_cnt[recipient.player_id] += 1
            recipient.passes_cnt[passer.player_id] += 1
        else:
            passer.passes_cnt[recipient.player_id] = 1
            recipient.passes_cnt[passer.player_id] = 1
