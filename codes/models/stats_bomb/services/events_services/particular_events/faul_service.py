from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Faul(Event):

    @staticmethod
    def isFaul(event):
        return Faul.getEventTypeId(event) in [pe.FAUL_WON]