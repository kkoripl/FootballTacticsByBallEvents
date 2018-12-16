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