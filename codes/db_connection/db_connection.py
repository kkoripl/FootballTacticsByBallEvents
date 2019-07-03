from pymongo import MongoClient

from resources.mongodb import authorization


class DbConnection:
    def __init__(self):
        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        self.client = MongoClient(
            'mongodb+srv://' + authorization.ADMIN_LOGIN + ':' + authorization.ADMIN_PASSWORD + '@footballtacticsbyballevents-dppaq.mongodb.net/test?retryWrites=true')
        self.db = self.client["StatsBombData"]

    def disconnect(self):
        self.client.close()

    def returnEventsCollection(self):
        return self.db["Events"]

    def returnMatchesCollection(self):
        return self.db["Matches"]

    def returnCompetitionsCollection(self):
        return self.db["Competitions"]

    def returnLineupsCollection(self):
        return self.db["Lineups"]