from code.models.stats_bomb import field_names
from code.models.stats_bomb.match.inside_models import mini_competition, mini_team, mini_season


class StatsBombMatch:
    def __init__(self, match):
        self.match_id = match[field_names.match_id]
        self.competition = mini_competition.MiniCompetition(match[field_names.competition])
        self.season = mini_season.MiniSeason(match[field_names.season])
        self.match_date = match[field_names.match_date]
        self.kick_off = match[field_names.kick_off]
        self.stadium_name = match[field_names.stadium_name]
        self.referee_name = match[field_names.referee_name]
        self.home_team = mini_team.MiniTeam(match[field_names.home_team], field_names.home_team)
        self.away_team = mini_team.MiniTeam(match[field_names.away_team], field_names.away_team)
        self.home_score = match[field_names.home_score]
        self.away_score = match[field_names.away_score]
        self.match_status = match[field_names.match_status]
        self.last_updated = match[field_names.last_updated]
        self.data_version = match[field_names.data_version]

    def __str__(self):
        return "MATCH[match_id: {},competition: {}, season: {}, match_date: {}, kick_off: {}, stadium_name: {}, " \
               "referee_name: {}, home_team : {}, away_team: {}, home_score: {}, away_score: {}, match_status: {}, " \
               "last_updated: {},  data_version: {}]".format(self.match_id, self.competition, self.season, self.match_date,
                                                            self.kick_off, self.stadium_name, self.referee_name, self.home_team,
                                                            self.away_team, self.home_score, self.away_score, self.match_status,
                                                            self.last_updated, self.data_version)