from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe


class Event:
    @staticmethod
    def getEventTypeId(event):
        return event.type.id

    @staticmethod
    def isTypeFieldIn(event):
        return pefn.TYPE in event

    @staticmethod
    def getEventOutcomeId(event, type):
        return event[type][pefn.OUTCOME][pefn.ID]

    @staticmethod
    def isSuccessfullOutcome(outcomeId):
        return outcomeId

    @staticmethod
    def __getX(event):
        return event["location"][0]

    @staticmethod
    def __getY(event):
        return event["location"][1]

    @staticmethod
    def getLocation(event):
        return [Event.__getX(event), Event.__getY(event)]

    @staticmethod
    def isPlayerEvent(event):
        return pefn.PLAYER in event.keys()
        # return hasattr(event, pefn.PLAYER) # in event.keys()

    @staticmethod
    def getPlayerId(event):
        return event[pefn.PLAYER][pefn.ID]

    @staticmethod
    def isTeamEvent(event, teamId):
        return event[pefn.TEAM][pefn.ID] == teamId
        # return event.team.id == teamId

    @staticmethod
    def getPossesionTeam(event):
        return event.possession_team

    @staticmethod
    def getTeam(event):
        return event.team

    @staticmethod
    def isAttackingEvent(event):
        return Event.getPossesionTeam(event) == Event.getTeam(event) \
               and Event.getEventTypeId(event) in pe.OFFENSIVE_EVENTS \
               and event.play_pattern.id not in [2, 3]

    @staticmethod
    def isDefendingEvent(event):
        return Event.getPossesionTeam(event) != Event.getTeam(event) \
               and Event.getEventTypeId(event) in pe.DEFENSIVE_EVENTS \
               and event.play_pattern.id  not in [2, 3]
