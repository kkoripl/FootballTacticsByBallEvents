from code.models.stats_bomb import field_names


class MiniTeam:
    def __init__(self, team, whichTeam):
        if whichTeam == field_names.home_team:
            self.team_id = team[field_names.home_team_id]
            self.team_name = team[field_names.home_team_name]
        else:
            self.team_id = team[field_names.away_team_id]
            self.team_name = team[field_names.away_team_name]

    def __str__(self):
        return "MiniTeam(team_id: {}, team_name: {})".format(self.team_id, self.team_name)