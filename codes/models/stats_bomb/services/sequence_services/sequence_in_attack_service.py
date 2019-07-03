from itertools import islice

from codes.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from codes.models.stats_bomb.services.events_services.particular_events.half_service import Half
from codes.models.stats_bomb.services.events_services.particular_events.interception_service import Interception
from codes.models.stats_bomb.services.events_services.particular_events.shot_service import Shot


class PossessionStringsService:

    def __init__(self):
        self.lastTeamWithBall = None
        self.__last = -1
        self.__play_segment_window_size = 4

    def makePlaySegments(self, events):
        sequences = self.getPossessionStringsWithTooShortRemoved(events)
        play_segments = []
        for sequence in sequences:
            play_segments += [x for x in self.window(sequence, self.__play_segment_window_size)]
        return play_segments

    def getPossessionStrings(self, events):
        sequences = []
        for event in events:
            if self.isPossessionStringStartingAt(event):
                sequences.append([event])
            elif self.isPossessionStringEndingAt(event):
                pass
            else:
                if self.isAttackingTeamEvent(event) and self.isNotPressing(event):
                    sequences[self.__last].append(event)

        return sequences

    def getPossessionStringsWithTooShortRemoved(self, events):
        return self.removeTooShortPossessionStrings(self.getPossessionStrings(events))

    def isPossessionStringStartingAt(self, event):
        decision = self.isSetPiece(event) or Pass.isKickOff(event) \
               or Pass.isBallFromGoalkeeper(event) or (not self.isTeamStillInPossesionAt(event)) \
                or Interception.isClearance(event)
        if not self.isTeamStillInPossesionAt(event):
            self.changeTeamInPossesionFor(self.getTeamInPossesionAt(event))
        return decision

    def isSetPiece(self, event):
        return Pass.isPassFromSetPiece(event) or Shot.isShotFromSetPiece(event)

    def isTeamStillInPossesionAt(self, event):
        return self.lastTeamWithBall == event.possession_team.name

    def getTeamInPossesionAt(self, event):
        return event.getPossessionTeamName()

    def changeTeamInPossesionFor(self, team):
        self.lastTeamWithBall = team

    def isPossessionStringEndingAt(self, event):
        return Half.isEndHalf(event) # or Faul.isFaul(event)

    def isAttackingTeamEvent(self, event):
        return self.lastTeamWithBall == event.team.name

    def isNotPressing(self, event):
        return event.type.name != 'Pressure'

    def removeTooShortPossessionStrings(self, sequences):
        return [sequence for sequence in sequences if len(sequence) >= self.__play_segment_window_size]

    def window(self, seq, n=2):
        "Returns a sliding window (of width n) over data from the iterable"
        "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
        it = iter(seq)
        result = tuple(islice(it, n))
        if len(result) == n:
            yield result
        for elem in it:
            result = result[1:] + (elem,)
            yield result










