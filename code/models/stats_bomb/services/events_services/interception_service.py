from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from code.models.stats_bomb.services.events_services.ball_pass_service import Pass
from code.models.stats_bomb.services.events_services.event_service import Event


class Interception (Event):

    #OUTCOME TYPES
    WON = 4
    LOST_IN_PLAY = 13
    LOST_OUT = 14
    SUCCESS_IN_PLAY = 16
    SUCCESS_OUT = 17

    @staticmethod
    def isBallInterception(event):
        if Interception.getEventTypeId(event) in [pe.INTERCEPTION, pe.BALL_RECOVERY] \
               or Pass.isPassRecovery(event): print('------ INTERCEPTION OR PASS RECOVERY -------')
        return Interception.getEventTypeId(event) in [pe.INTERCEPTION, pe.BALL_RECOVERY] \
               or Pass.isPassRecovery(event)