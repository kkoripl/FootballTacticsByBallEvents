from codes.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.data_preparation_models.players_positions import PlayersPositions as pp
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Pass(Event):

    # OUTCOME TYPES
    INCOMPLETE = 9
    INJURY_CLEARANCE = 74
    OUT = 75
    PASS_OFFSIDE = 76
    UNKNOWN = 77

    @staticmethod
    def get_event_outcome_id(event, type=pefn.PASS):
        return super().get_event_outcome_id(event, type)

    @staticmethod
    def __get_pass_field(event):
        return event.pass_obj

    @staticmethod
    def is_pass_completed(event):
        return not hasattr(event.pass_obj, 'outcome')

    @staticmethod
    def is_pass(event):
        return Pass.get_event_type_id(event) in [pe.PASS, pe.HIGH_PASS, pe.LOW_PASS]

    @staticmethod
    def __is_pass_and_got_type_field(event):
        return Pass.is_pass(event) and Pass.is_type_field_in(Pass.__get_pass_field(event))

    @staticmethod
    def is_pass_recovered_well(event):
        return Pass.__is_pass_and_got_type_field(event) \
               and Pass.get_event_type_id(Pass.__get_pass_field(event)) == pe.RECOVERY \
               and Pass.is_pass_completed(event)

    @staticmethod
    def is_ball_from_gk(event):
        return Pass.__is_goal_kick(event) or Pass.__is_pass_from_gk(event)

    @staticmethod
    def __is_goal_kick(event):
        return Pass.__is_pass_and_got_type_field(event) \
               and Pass.is_pass_from_goal_kick(Pass.__get_pass_field(event))

    @staticmethod
    def is_pass_from_goal_kick(field_pass):
        return Pass.get_event_type_id(field_pass) == pe.GOAL_KICK

    @staticmethod
    def __is_pass_from_gk(event):
        return Pass.is_pass(event) and event.position.id == pp.GOALKEEPER

    @staticmethod
    def is_kick_off(event):
        return Pass.__is_pass_and_got_type_field(event) \
               and Pass.get_event_type_id(Pass.__get_pass_field(event)) == pe.KICK_OFF

    @staticmethod
    def is_pass_from_set_piece(event):
        return Pass.__is_pass_and_got_type_field(event) and \
               Pass.get_event_type_id(Pass.__get_pass_field(event)) in [pe.CORNER, pe.FREE_KICK, pe.PENALTY, pe.THROW_IN]

    @staticmethod
    def get_recipient_id(event):
        return event.pass_obj.recipient.id

    @staticmethod
    def get_x_end_location(event):
        return event.pass_obj.end_location[0]

    @staticmethod
    def get_y_end_location(event):
        return event.pass_obj.end_location[1]