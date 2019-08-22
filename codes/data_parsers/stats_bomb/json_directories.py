import os


class JsonDirectories:
    DATA_DIRECTORY = '.'
    OUTPUTS_DIRECTORY = '.'

    def getSBEventsDirectory(self):
        return os.path.join(self.getSBDataDirectory(), 'events')

    def getSBLineupsDirectory(self):
        return os.path.join(self.getSBDataDirectory(), 'lineups')
    
    def getSBMatchesDirectory(self):
        return os.path.join(self.getSBDataDirectory(), 'matches')
    
    def getSBCompetitionsDirectory(self):
        return self.getSBDataDirectory()

    def getSBDataDirectory(self):
        return os.path.join(JsonDirectories.DATA_DIRECTORY, 'resources', 'data', 'stats_bomb')
    
    def create_occupancy_maps_pkl_path(self, play_segment_length):
        return os.path.join(self.create_outputs_dir_path(), 'occupancy_maps_' + str(play_segment_length)+'.pkl')

    def create_first_investigation_scores_csv_path(self):
        return os.path.join(self.create_outputs_dir_path(), 'first_int_scores.csv')

    def create_competition_subdir_path(self, competition):
        return os.path.join(self.create_outputs_dir_path(), competition)

    def create_competition_season_subdir_path(self, competition, season):
        return os.path.join(self.create_competition_subdir_path(competition), season)
    
    def create_outputs_dir_path(self):
        if self.OUTPUTS_DIRECTORY != '':
            return os.path.join(JsonDirectories.OUTPUTS_DIRECTORY, 'outputs')
        else:
            return os.path.join('outputs')
    
    def create_outputs_dir(self):
        os.makedirs(self.create_outputs_dir_path(), exist_ok=True)

    def create_competition_season_subdir(self, competition, season):
        os.makedirs(self.create_competition_season_subdir_path(competition, season), exist_ok=True)

    def create_competition_subdir(self, competition):
        os.makedirs(self.create_competition_subdir_path(competition), exist_ok=True)

