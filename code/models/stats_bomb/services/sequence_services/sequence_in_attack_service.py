from code.models.stats_bomb.services.events_services.ball_pass_service import Pass
from code.models.stats_bomb.services.events_services.faul_service import Faul
from code.models.stats_bomb.services.events_services.half_service import Half
from code.models.stats_bomb.services.events_services.interception_service import Interception
from code.models.stats_bomb.services.events_services.shot_service import Shot


class SequenceInAttack:

    def isAttackSequenceStartAt(self, event):
        return self.isSetPiece(event) or Pass.isKickOff(event) \
               or Interception.isBallInterception(event) or Pass.isBallFromGoalkeeper(event)

    def isSetPiece(self, event):
        if Pass.isPassFromSetPiece(event) or Shot.isShotFromSetPiece(event): print('------ SET PIECE -------')
        return Pass.isPassFromSetPiece(event) or Shot.isShotFromSetPiece(event)

    def isAttackSequenceEndAt(self, event):
        return Half.isEndHalf(event) or Faul.isFaul(event)





