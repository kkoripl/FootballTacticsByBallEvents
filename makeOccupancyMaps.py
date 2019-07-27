import argparse
import os

import matplotlib
import pandas as pd

from codes.data_parsers.stats_bomb.DataParser import jsonEvents2Obj, jsonLineup2Obj
from codes.data_parsers.stats_bomb.json_directories import JsonDirectories
from codes.data_parsers.stats_bomb.json_utils import SBJsonUtils
from codes.models.classes.match import Match
from codes.models.stats_bomb.data_preparation_models.pitch_location import PitchLocation
from codes.models.stats_bomb.services.sequence_services.possession_strings_service import PossessionStringsService
from codes.plots.pitch import drawPitch

matplotlib.use('Agg')  # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as pyplot


def makeOccupancyMaps():
    json_directories = JsonDirectories()
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-folder', type=str, dest='data_folder', help='data folder mounting point')
    args = parser.parse_args()
    if args.data_folder is not None:
        print(args.data_folder)
        head, tail = os.path.split(args.data_folder)
        JsonDirectories.DATA_DIRECTORY = head
        JsonDirectories.OUTPUTS_DIRECTORY = ''

    jsonUtils = SBJsonUtils()
    possStrings = PossessionStringsService()
    lastCompetition = ""
    lastSeason = ""
    path_to_folder = ""
    occupancy_maps_df = pd.DataFrame(columns=['match_id', 'team_id', 'team', 'occupancy_map'])
    json_directories.create_outputs_dir()

    matches = jsonUtils.getAllMatches()
    for m in matches:
        print(m)
        if lastCompetition != m['competition']['competition_name'] or lastSeason != m['season']['season_name']:
            changedCompetition = m['competition']['competition_name'].replace(" ", "_").replace("'", "")
            changedSeason = m['season']['season_name'].replace("/", "_")
            json_directories.create_competition_subdir(changedCompetition)
            json_directories.create_competition_season_subdir(changedCompetition, changedSeason)
            path_to_folder = json_directories.create_competition_season_subdir_path(changedCompetition, changedSeason)
        match = Match(m['_id'],
                      jsonLineup2Obj(jsonUtils.readMatchLineupDataFromJson(m['_id'], m['home_team']['home_team_id'])),
                      jsonLineup2Obj(jsonUtils.readMatchLineupDataFromJson(m['_id'], m['away_team']['away_team_id'])),
                      jsonEvents2Obj(jsonUtils.readMatchEventsDataFromJson(m['_id'])))

        match.home.possesion_strings, match.away.possesion_strings = possStrings.getPossessionStrings(match)
        home_entropy_map, away_entropy_map = possStrings.createEventsEntropyMaps(match)

        occupancy_maps_df = occupancy_maps_df.append(
            pd.DataFrame([createHomeOccupancyMapDict(m, home_entropy_map)]))
        occupancy_maps_df = occupancy_maps_df.append(
            pd.DataFrame([createAwayOccupancyMapDict(m, away_entropy_map)]))

        home_entropy_map = home_entropy_map.reshape(PitchLocation.BINS_Y, PitchLocation.BINS_X)
        away_entropy_map = away_entropy_map.reshape(PitchLocation.BINS_Y, PitchLocation.BINS_X)

        match_data = {'match_id': m['_id'],
                      'home_team': m['home_team']['home_team_name'].replace(" ", "_"),
                      'away_team': m['away_team']['away_team_name'].replace(" ", "_"),
                      'home_score': m['home_score'],
                      'away_score': m['away_score']}
        plot_combined_occupancy_map(home_entropy_map, away_entropy_map, match_data, path_to_folder)
        match_data['home_team'] = "[%s]" % (match_data['home_team'])
        match_data['away_team'] = match_data['away_team'].replace("[", "").replace("]", "")
        plot_team_occupancy_map(home_entropy_map, match_data, path_to_folder)
        match_data['home_team'] = match_data['home_team'].replace("[", "").replace("]", "")
        match_data['away_team'] = "[%s]" % (match_data['away_team'])
        plot_team_occupancy_map(away_entropy_map, match_data, path_to_folder)
    occupancy_maps_df.to_csv(os.path.join(json_directories.create_occupancy_maps_csv_path(), 'occupancy_maps.csv'))


def createAwayOccupancyMapDict(match, entropy_map):
    return {'match_id': match['_id'],
            'team_id': match['away_team']['away_team_id'],
            'team': match['away_team']['away_team_name'],
            'occupancy_map': entropy_map}

def createHomeOccupancyMapDict(match, entropy_map):
    return {'match_id': match['_id'],
            'team_id': match['home_team']['home_team_id'],
            'team': match['home_team']['home_team_name'],
            'occupancy_map': entropy_map}

def getCmp():
    return 'jet'

def create_path_to_save_picture(dir_path, match_data):
    return os.path.join(dir_path, str(match_data["match_id"]) + "_" + match_data['home_team'] + "_" + match_data[
        'away_team'] + ".png")


def plot_combined_occupancy_map(home_entropy_map, away_entropy_map, match_data, path_to_folder):
    pitchFig = pyplot.figure()
    pitchFig.set_size_inches(7, 3)
    pyplot.axis('off')
    pyplot.title("%s vs. %s %d:%d" % (
        match_data['home_team'], match_data['away_team'], match_data['home_score'], match_data['away_score']))
    ax1 = pitchFig.add_subplot(121)
    ax2 = pitchFig.add_subplot(122)
    drawPitch(ax1)
    ax1.imshow(home_entropy_map, interpolation='nearest',
               extent=(0, PitchLocation.X_SIZE, 0, PitchLocation.Y_SIZE), vmin=0, vmax=5.5, cmap=getCmp())
    drawPitch(ax2)
    img = ax2.imshow(away_entropy_map, interpolation='nearest',
                     extent=(0, PitchLocation.X_SIZE, 0, PitchLocation.Y_SIZE), vmin=0, vmax=5.5, cmap=getCmp())
    pitchFig.subplots_adjust(right=0.8)
    cbar_ax = pitchFig.add_axes([0.85, 0.05, 0.01, 0.85])
    pitchFig.colorbar(img, cax=cbar_ax)
    pyplot.savefig(create_path_to_save_picture(path_to_folder, match_data))
    pyplot.close(pitchFig)


def plot_team_occupancy_map(team_entropy_map, match_data, path_to_folder):
    pitchFig = pyplot.figure()
    pitchFig.set_size_inches(7, 3)
    pyplot.axis('off')
    pyplot.title("%s vs. %s %d:%d" % (
        match_data['home_team'], match_data['away_team'], match_data['home_score'], match_data['away_score']))
    ax = pitchFig.add_subplot(111)
    drawPitch(ax)
    img = ax.imshow(team_entropy_map, interpolation='nearest',
                    extent=(0, PitchLocation.X_SIZE, 0, PitchLocation.Y_SIZE), vmin=0, vmax=5.5, cmap=getCmp())
    pitchFig.colorbar(img)
    pyplot.savefig(create_path_to_save_picture(path_to_folder, match_data))
    pyplot.close(pitchFig)


makeOccupancyMaps()