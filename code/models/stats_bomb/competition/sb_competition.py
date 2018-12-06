from code.models.stats_bomb import field_names


class StatsBombCompetition:
    def __init__(self, competition):
        self.competition_id = competition[field_names.competition_id]
        self.season_id = competition[field_names.season_id]
        self.competition_name = competition[field_names.competition_name]
        self.country_name = competition[field_names.country_name]
        self.season_name = competition[field_names.season_name]
        self.match_updated = competition[field_names.match_updated]
        self.match_available = competition[field_names.match_available]

    def __str__(self) -> str:
        return 'COMP[competition_id: {}, season_id: {}, competition_name: {}, ' \
               'country_name: {}, season_name: {}, match_updated: {}, match_available: {}'.format(
                self.competition_id, self.season_id, self.competition_name, self.country_name,
                self.season_name, self.match_updated, self.match_available)



