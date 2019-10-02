class Player:

    def __init__(self):
        self.player_id = None
        self.player_name = None
        self.jersey_number = None
        self.country = None
        self.in_xi = False
        self.events = {'attack': [], 'defence': []}
        self.events_locations = {'attack': [], 'defence': []}
        self.avg_position = None
        self.passes_cnt = {}
        self.passes = []

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def add_attacking_event(self, event):
        self.events['attack'].append(event)

    def add_defensive_event(self, event):
        self.events['defence'].append(event)

    def has_played_in_game(self):
        return len(self.events['attack']) + len(self.events['defence']) != 0