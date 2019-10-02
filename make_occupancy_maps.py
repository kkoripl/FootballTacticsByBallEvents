import argparse

import pandas as pd

from codes.azure_utils.dataFolderConnector import connectDataFolder
from codes.data_parsers.stats_bomb.data_parser import json_events_2_obj, json_lineup_2_obj
from codes.data_parsers.stats_bomb.json_directories import JsonDirectories
from codes.data_parsers.stats_bomb.json_utils import SBJsonUtils
from codes.models.classes.match import Match
from codes.models.stats_bomb.services.sequence_services.possession_strings_service import PossessionStringsService


def do_occupancy_maps():
    parser = argparse.ArgumentParser()
    connectDataFolder(parser)
    #makeOccupancyMaps(-args)

def make_occupancy_maps(play_segment_length, x_bins, y_bins):
    json_directories = JsonDirectories()

    jsonUtils = SBJsonUtils()
    possStrings = PossessionStringsService(play_segment_window=play_segment_length, x_bins=x_bins, y_bins=y_bins)
    lastCompetition = ""
    lastSeason = ""
    path_to_folder = ""
    occupancy_maps_df = pd.DataFrame(columns=['match_id', 'team_id', 'team', 'occupancy_map'])
    json_directories.create_outputs_dir()

    matches = jsonUtils.get_all_matches()
    for m in matches:
        print(m)
        if lastCompetition != m['competition']['competition_name'] or lastSeason != m['season']['season_name']:
            changedCompetition = m['competition']['competition_name'].replace(" ", "_").replace("'", "")
            changedSeason = m['season']['season_name'].replace("/", "_")
            json_directories.create_competition_subdir(changedCompetition)
            json_directories.create_competition_season_subdir(changedCompetition, changedSeason)
            # path_to_folder = json_directories.create_competition_season_subdir_path(changedCompetition, changedSeason)
        match = Match(m['_id'],
                      json_lineup_2_obj(jsonUtils.read_match_lineup_from_jsons(m['_id'], m['home_team']['home_team_id'])),
                      json_lineup_2_obj(jsonUtils.read_match_lineup_from_jsons(m['_id'], m['away_team']['away_team_id'])),
                      json_events_2_obj(jsonUtils.read_match_events_from_jsons(m['_id'])))

        match.home.possesion_strings, match.away.possesion_strings = possStrings.get_possession_strings(match)
        home_entropy_map, away_entropy_map = possStrings.create_events_entropy_maps(match)

        occupancy_maps_df = occupancy_maps_df.append(
            pd.DataFrame([create_home_occ_map_dict(m, home_entropy_map)]))
        occupancy_maps_df = occupancy_maps_df.append(
            pd.DataFrame([create_away_occ_map_dict(m, away_entropy_map)]))
        # home_entropy_map = home_entropy_map.reshape(PitchLocation.BINS_Y, PitchLocation.BINS_X)
        # away_entropy_map = away_entropy_map.reshape(PitchLocation.BINS_Y, PitchLocation.BINS_X)
        #
        # match_data = {'match_id': m['_id'],
        #               'home_team': m['home_team']['home_team_name'].replace(" ", "_"),
        #               'away_team': m['away_team']['away_team_name'].replace(" ", "_"),
        #               'home_score': m['home_score'],
        #               'away_score': m['away_score']}
        # plot_combined_occupancy_map(home_entropy_map, away_entropy_map, match_data, path_to_folder)
        # match_data['home_team'] = "[%s]" % (match_data['home_team'])
        # match_data['away_team'] = match_data['away_team'].replace("[", "").replace("]", "")
        # plot_team_occupancy_map(home_entropy_map, match_data, path_to_folder)
        # match_data['home_team'] = match_data['home_team'].replace("[", "").replace("]", "")
        # match_data['away_team'] = "[%s]" % (match_data['away_team'])
        # plot_team_occupancy_map(away_entropy_map, match_data, path_to_folder)
    occupancy_maps_df.to_pickle(json_directories.create_occupancy_maps_pkl_path(play_segment_length, x_bins, y_bins))
    del occupancy_maps_df


def create_away_occ_map_dict(match, entropy_map):
    return {'match_id': match['_id'],
            'team_id': match['away_team']['away_team_id'],
            'team': match['away_team']['away_team_name'],
            'occupancy_map': entropy_map}

def create_home_occ_map_dict(match, entropy_map):
    return {'match_id': match['_id'],
            'team_id': match['home_team']['home_team_id'],
            'team': match['home_team']['home_team_name'],
            'occupancy_map': entropy_map}
