from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from code.models.stats_bomb.data_preparation_models.players_positions import PlayersPositions as pp
from code.models.stats_bomb.services.events_services.event_service import Event


class Pass(Event):

    # OUTCOME TYPES
    INCOMPLETE = 9
    INJURY_CLEARANCE = 74
    OUT = 75
    PASS_OFFSIDE = 76
    UNKNOWN = 77

    @staticmethod
    def getEventOutcomeId(event, type=pefn.PASS):
        return super().getEventOutcomeId(event, type)

    @staticmethod
    def __getPassField(event):
        return event[pefn.PASS]

    @staticmethod
    def isPass(event):
        return Pass.getEventTypeId(event) in [pe.PASS, pe.HIGH_PASS, pe.LOW_PASS]

    @staticmethod
    def __isPassAndGotTypeField(event):
        return Pass.isPass(event) and Pass.isTypeFieldIn(Pass.__getPassField(event))

    @staticmethod
    def isPassRecovery(event):
        return Pass.__isPassAndGotTypeField(event) \
               and Pass.getEventTypeId(Pass.__getPassField(event)) == pe.RECOVERY

    @staticmethod
    def isBallFromGoalkeeper(event):
        if Pass.__isGoalKick(event) or Pass.__isPassFromGoalkeeper(event): print('------ PASS FROM GOALKEEPER -------')
        return Pass.__isGoalKick(event) or Pass.__isPassFromGoalkeeper(event)

    @staticmethod
    def __isGoalKick( event):
        return Pass.__isPassAndGotTypeField(event) \
               and Pass.__isPassFromGoalKick(Pass.__getPassField(event))

    @staticmethod
    def __isPassFromGoalKick(field_pass):
        return Pass.getEventTypeId(field_pass) == pe.GOAL_KICK

    @staticmethod
    def __isPassFromGoalkeeper(event):
        return Pass.isPass(event) and event[pefn.POSITION][pefn.ID] == pp.GOALKEEPER

    @staticmethod
    def isKickOff(event):
        if Pass.__isPassAndGotTypeField(event) \
               and Pass.getEventTypeId(Pass.__getPassField(event)) == pe.KICK_OFF: print('------ KICK OFF -------')
        return Pass.__isPassAndGotTypeField(event) \
               and Pass.getEventTypeId(Pass.__getPassField(event)) == pe.KICK_OFF

    @staticmethod
    def isPassFromSetPiece(event):
        return Pass.__isPassAndGotTypeField(event) and \
               Pass.getEventTypeId(Pass.__getPassField(event)) in [pe.CORNER, pe.FREE_KICK, pe.PENALTY, pe.THROW_IN]