import argparse

import pandas as pd
from sklearn.model_selection import ParameterGrid

from codes.azure_utils.dataFolderConnector import connectDataFolder
from codes.data_parsers.stats_bomb.json_directories import JsonDirectories
from make_occupancy_maps import makeOccupancyMaps
from predict_team_by_occupancy_maps import predict_team_by_occupancy_maps


def doInvestigation():
    parser = argparse.ArgumentParser()
    connectDataFolder(parser)
    makeFirstInvestigation()


def makeFirstInvestigation():
    json_directories = JsonDirectories()
    df = pd.DataFrame(columns=['psl', 'x_bins', 'y_bins', 'to', 'k', 'score'])
    param_grid = {'play_segements_length': range(4, 13),
                  'z_train_occurances': range(5, 12),
                  'z_k': range(5, 31),
                  'x_bins': range(5, 21),
                  'y_bins': range(4, 17),
                  }
    length = None
    x_bin = None
    y_bin = None
    for parameters in ParameterGrid(param_grid):
        to = parameters['z_train_occurances']
        k_val = parameters['z_k']

        print(' ------------ ')
        print('LENGTH: ' + str(parameters['play_segements_length']))
        print('X_BIN: ' + str(parameters['x_bins']))
        print('Y_BIN: ' + str(parameters['y_bins']))
        print('TO: ' + str(to))
        print('K: ' + str(k_val))

        if length != parameters['play_segements_length'] or x_bin != parameters['x_bins'] or y_bin != parameters[
            'y_bins']:
            length = parameters['play_segements_length']
            x_bin = parameters['x_bins']
            y_bin = parameters['y_bins']
            makeOccupancyMaps(length, x_bin, y_bin)

        score = predict_team_by_occupancy_maps(length, to, k_val)
        df = df.append(pd.DataFrame({'psl': [length],
                                     'x_bins': [x_bin],
                                     'y_bins': [y_bin],
                                     'to': [to],
                                     'k': [k_val],
                                     'score': [score]}))
    df.to_csv(json_directories.create_first_investigation_scores_csv_path())


doInvestigation()
