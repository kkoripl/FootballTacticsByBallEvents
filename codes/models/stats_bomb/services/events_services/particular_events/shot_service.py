from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Shot(Event):

    # OUTCOME TYPES
    BLOCKED = 96
    GOAL = 97
    OFF_TARGET = 98
    POST = 99
    SAVED = 100
    WAYWARD = 101

    @staticmethod
    def __get_shot_field(event):
        return event.shot

    @staticmethod
    def is_shot(event):
        return Shot.get_event_type_id(event) == pe.SHOT

    @staticmethod
    def __is_shot_and_got_type_field(event):
        return Shot.is_shot(event) and Shot.is_type_field_in(Shot.__get_shot_field(event))

    @staticmethod
    def is_shot_from_set_piece(event):
        return Shot.__is_shot_and_got_type_field(event) and \
               Shot.get_event_type_id(Shot.__get_shot_field(event)) in [pe.CORNER, pe.FREE_KICK, pe.PENALTY, pe.THROW_IN]