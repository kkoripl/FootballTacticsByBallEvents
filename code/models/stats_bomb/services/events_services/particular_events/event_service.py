from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn


class Event:
    @staticmethod
    def getEventTypeId(event):
        return event[pefn.TYPE][pefn.ID]

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
    def getX(event):
        return event["location"][0]

    @staticmethod
    def getY(event):
        return event["location"][1]

    @staticmethod
    def getLocation(event):
        return Point(Event.getX(event), Event.getY(event))

    @staticmethod
    def isPlayerEvent(event):
        return pefn.PLAYER in event.keys()

    @staticmethod
    def getPlayerId(event):
        return event[pefn.PLAYER][pefn.ID]

    @staticmethod
    def isTeamEvent(event, teamId):
        return event[pefn.TEAM][pefn.ID] == teamId
