class Player:

    def __init__(self):
        self.player_id = None
        self.player_name = None
        self.jersey_number = None
        self.country = None
        self.events = {'attack': [], 'defence': []}
        self.convex_hulls = {'attack': None, 'defence': None}
        self.events_locations = {'attack': [], 'defence': []}
        self.avg_position = None

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def addAttackingEvent(self, event):
        self.events['attack'].append(event)

    def addDefensiveEvent(self, event):
        self.events['defence'].append(event)

    def havePlayedInGame(self):
        return len(self.events['attack']) + len(self.events['defence']) != 0