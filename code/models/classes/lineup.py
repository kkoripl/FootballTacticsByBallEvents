class Lineup:
    match_id = None
    team_id = None
    team_name = None
    lineup = None

    def setLineup(self, lineup):
        self.lineup = lineup

    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self)

    def getPlayer(self, playerId):
        return next((x for x in self.lineup if x.player_id == playerId), None)

    def gotPlayer(self, playerId):
        return next((True for x in self.lineup if x.player_id == playerId), False)


