from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Half(Event):
    @staticmethod
    def is_end_half(event):
        return Half.get_event_type_id(event) == pe.HALF_END
