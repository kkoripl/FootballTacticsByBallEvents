from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from code.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from code.models.stats_bomb.services.events_services.particular_events.half_service import Half
from code.models.stats_bomb.services.events_services.particular_events.interception_service import Interception
from code.models.stats_bomb.services.events_services.particular_events.shot_service import Shot


class SequenceInAttack:

    def __init__(self):
        self.lastTeamWithBall = None
        self.__last = -1
        self.__minimumEventsInSeq = 4

    def getAttackSequences(self, events):
        sequences = []
        for event in events:
            if self.isAttackSequenceStartAt(event):
                sequences.append([event])
            elif self.isAttackSequenceEndAt(event):
                pass
            else:
                if self.isAttackingTeamEvent(event) and self.isNotPressing(event):
                    sequences[self.__last].append(event)

        return sequences

    def getAttackSequencesWithTooShortRemoved(self, events):
        return self.removeTooShortSequencesFrom(self.getAttackSequences(events));

    def isAttackSequenceStartAt(self, event):
        decision = self.isSetPiece(event) or Pass.isKickOff(event) \
               or Pass.isBallFromGoalkeeper(event) or (not self.isTeamStillInPossesionAt(event)) \
                or Interception.isClearance(event)
        if not self.isTeamStillInPossesionAt(event):
            self.changeTeamInPossesionFor(self.getTeamInPossesionAt(event))
        return decision

    def isSetPiece(self, event):
        return Pass.isPassFromSetPiece(event) or Shot.isShotFromSetPiece(event)

    def isTeamStillInPossesionAt(self, event):
        return self.lastTeamWithBall == self.getTeamInPossesionAt(event)

    def getTeamInPossesionAt(self, event):
        return event[pefn.POSSESSION_TEAM][pefn.NAME]

    def changeTeamInPossesionFor(self, team):
        self.lastTeamWithBall = team

    def isAttackSequenceEndAt(self, event):
        return Half.isEndHalf(event) # or Faul.isFaul(event)

    def isAttackingTeamEvent(self, event):
        return self.lastTeamWithBall == event[pefn.TEAM][pefn.NAME]

    def isNotPressing(self, event):
        return event[pefn.TYPE][pefn.NAME] != 'Pressure'

    def removeTooShortSequencesFrom(self, sequences):
        return [sequence for sequence in sequences if len(sequence) >= self.__minimumEventsInSeq]










