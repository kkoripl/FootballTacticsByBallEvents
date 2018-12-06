from code.models.stats_bomb import field_names


class MiniSeason:
    def __init__(self, season):
        self.season_id = season[field_names.season_id]
        self.season_name = season[field_names.season_name]

    def __str__(self):
        return "MiniSeason(season_id: {}, season_name: {})".format(self.season_id, self.season_name)