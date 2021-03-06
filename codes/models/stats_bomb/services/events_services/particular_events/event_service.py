from codes.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe


class Event:
    @staticmethod
    def get_event_type_id(event):
        return event.type.id

    @staticmethod
    def is_type_field_in(event):
        return event.type is not None

    @staticmethod
    def get_event_outcome_id(event, type):
        return event.type.outcome.id

    @staticmethod
    def is_successfull_outcome(outcomeId):
        return outcomeId

    @staticmethod
    def get_x(event):
        return event.location[0]

    @staticmethod
    def get_y(event):
        return event.location[1]

    @staticmethod
    def get_location(event):
        return [Event.get_x(event), Event.get_y(event)]

    @staticmethod
    def is_player_event(event):
        return pefn.PLAYER in event.keys()

    @staticmethod
    def get_player_id(event):
        return event.player.id

    @staticmethod
    def get_player(event):
        return event.player

    @staticmethod
    def is_team_event(event, team_id):
        return event.team.id == team_id

    @staticmethod
    def get_possession_team(event):
        return event.possession_team

    @staticmethod
    def get_team(event):
        return event.team

    @staticmethod
    def is_attacking_event(event):
        return Event.get_possession_team(event) == Event.get_team(event) \
               and Event.get_event_type_id(event) in pe.OFFENSIVE_EVENTS \
               and event.play_pattern.id not in [2, 3]

    @staticmethod
    def is_defending_event(event):
        return Event.get_possession_team(event) != Event.get_team(event) \
               and Event.get_event_type_id(event) in pe.DEFENSIVE_EVENTS \
               and event.play_pattern.id not in [2, 3]
    @staticmethod
    def is_ball_receipt(event):
        return Event.get_event_type_id(event) == pe.BALL_RECEIPT

    @staticmethod
    def event_got_card(event):
        return Event.get_event_type_id(event) == pe.FAUL_COMMITTED and event.foul_committed is not None and hasattr(event.foul_committed, 'card')

    @staticmethod
    def player_sent_off(event):
        return Event.event_got_card(event) and event.foul_committed.card.name == 'Red Card'

    @staticmethod
    def got_yellow_card(event):
        return Event.event_got_card(event) and event.foul_committed.card.name == 'Yellow Card'

    @staticmethod
    def is_substitiution(event):
        return Event.get_event_type_id(event) == pe.SUBSTITUTION