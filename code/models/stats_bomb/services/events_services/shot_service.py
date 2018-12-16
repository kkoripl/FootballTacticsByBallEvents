from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from code.models.stats_bomb.services.events_services.event_service import Event


class Shot(Event):

    # OUTCOME TYPES
    BLOCKED = 96
    GOAL = 97
    OFF_TARGET = 98
    POST = 99
    SAVED = 100
    WAYWARD = 101

    @staticmethod
    def __getShotField(event):
        return event[pefn.SHOT]

    @staticmethod
    def isShot(event):
        return Shot.getEventTypeId(event) == pe.SHOT

    @staticmethod
    def __isShotAndGotTypeField(event):
        return Shot.isShot(event) and Shot.isTypeFieldIn(Shot.__getShotField(event))

    @staticmethod
    def isShotFromSetPiece(event):
        return Shot.__isShotAndGotTypeField(event) and \
               Shot.getEventTypeId(Shot.__getShotField(event)) in [pe.CORNER, pe.FREE_KICK, pe.PENALTY, pe.THROW_IN]