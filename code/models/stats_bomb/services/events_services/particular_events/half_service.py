from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from code.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Half(Event):
    @staticmethod
    def isEndHalf(event):
        return Half.getEventTypeId(event) == pe.HALF_END
