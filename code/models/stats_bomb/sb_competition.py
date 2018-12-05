class StatsBombCompetition:
    def __init__(self, competition_id, season_id, competition_name, country_name, season_name, match_updated, match_available):
        self.competition_id = competition_id
        self.season_id = season_id
        self.competition_name = competition_name
        self.country_name = country_name
        self.season_name = season_name
        self.match_updated = match_updated
        self.match_available = match_available

    def __str__(self) -> str:
        return 'COMP[competition_id: {}, season_id: {}, competition_name: {}, ' \
               'country_name: {}, season_name: {}, match_updated: {}, match_available: {}'.format(
                self.competition_id, self.season_id, self.competition_name, self.country_name,
                self.season_name, self.match_updated, self.match_available)



