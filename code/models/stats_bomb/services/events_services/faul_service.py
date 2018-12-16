from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from code.models.stats_bomb.services.events_services.event_service import Event


class Faul(Event):

    @staticmethod
    def isFaul(event):
        if Faul.getEventTypeId(event) in [pe.FAUL_WON]: print('------ FAUL -------')
        return Faul.getEventTypeId(event) in [pe.FAUL_WON]