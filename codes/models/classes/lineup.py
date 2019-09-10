class Lineup:
    match_id = None
    team_id = None
    team_name = None
    lineup = None
    events = None
    possesion_strings = None

    def set_lineup(self, lineup):
        self.lineup = lineup

    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.__dict__.update(d)
        obj.events = []
        obj.possesion_strings = []
        return obj

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def get_player(self, player_id):
        return next((x for x in self.lineup if x.player_id == player_id), None)

    def got_player(self, player_id):
        return next((True for x in self.lineup if x.player_id == player_id), False)

    def add_event(self, event):
        self.events.append(event)


