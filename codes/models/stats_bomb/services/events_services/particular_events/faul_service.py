from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Faul(Event):

    @staticmethod
    def is_faul(event):
        return Faul.get_event_type_id(event) in [pe.FAUL_WON]