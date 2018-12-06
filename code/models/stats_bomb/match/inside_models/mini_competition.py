from code.models.stats_bomb import field_names


class MiniCompetition(object):
    def __init__(self, competition):
        self.competition_id = competition[field_names.competition_id]
        self.country_name = competition[field_names.country_name]
        self.competition_name = competition[field_names.competition_name]

    def __str__(self):
        return "MiniCompetition(competition_id: {}, country_name: {}, competition_name: {})"\
                .format(self.competition_id, self.country_name, self.competition_name)