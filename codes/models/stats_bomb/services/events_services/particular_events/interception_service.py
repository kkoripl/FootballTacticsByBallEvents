from codes.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from codes.models.stats_bomb.services.events_services.particular_events.event_service import Event


class Interception (Event):

    #OUTCOME TYPES
    WON = 4
    LOST_IN_PLAY = 13
    LOST_OUT = 14
    SUCCESS_IN_PLAY = 16
    SUCCESS_OUT = 17

    @staticmethod
    def isBallInterception(event):
        return Interception.get_event_type_id(event) in [pe.INTERCEPTION, pe.BALL_RECOVERY] \
               or Pass.is_pass_recovered_well(event)

    def hasTeamPossesingBallChanged(self, event):
        team_posessing_now = event[pefn.POSSESSION_TEAM]

    @staticmethod
    def isClearance(event):
        return Interception.get_event_type_id(event) == pe.CLEARANCE
