import argparse
import sys
import threading
import time
import traceback
from queue import Queue
from threading import Thread

import pandas as pd
from sklearn.model_selection import ParameterGrid

from codes.azure_utils.dataFolderConnector import connectDataFolder
from codes.data_parsers.stats_bomb.json_directories import JsonDirectories
from make_occupancy_maps import make_occupancy_maps
from predict_team_by_occupancy_maps import predict_team_by_occupancy_maps

ALL_MAPS_CONFIGS = 0
LOCK = threading.Lock()

def do_investigation():
    parser = argparse.ArgumentParser()
    connectDataFolder(parser)
    make_first_investigation()

def do_partial_investigation(q, df):
    while not q.empty():
        work = q.get()
        length = work[0]
        x_bin = work[1]
        y_bin = work[2]
        test_params = work[3]
        try:
            print("L: {} / X: {} / Y: {}".format(str(length), str(x_bin), str(y_bin)))
            make_occupancy_maps(length, x_bin, y_bin)
            for params in test_params:
                score = predict_team_by_occupancy_maps(length, x_bin, y_bin, params['to'], params['k_val'])
                df.append(pd.DataFrame({'psl': [length],
                                             'x_bins': [x_bin],
                                             'y_bins': [y_bin],
                                             'to': [params['to']],
                                             'k': [params['k_val']],
                                             'score': [score]}))
            show_proceeding()
        except:
            print("-> ERROR! -- L: {} / X: {} / Y: {}".format(str(length), str(x_bin), str(y_bin)))
            exc_info = sys.exc_info()
            traceback.print_exception(*exc_info)

        q.task_done()
    return True

def make_first_investigation():
    start_time = time.ctime()
    print(start_time)
    om_queue = Queue(maxsize=0)
    json_directories = JsonDirectories()
    dfs = []

    om_param_grid = {
        'play_segements_length': range(4, 9),
        'x_bins': range(10, 21),
        'y_bins': range(8, 17)
    }
    test_param_grid = {
        'to': range(5, 12),
        'k_val': range(10, 40)
    }

    om_params = ParameterGrid(om_param_grid)
    all_om_params = len(om_params)
    num_theads = min(50, all_om_params)

    global ALL_MAPS_CONFIGS
    ALL_MAPS_CONFIGS = all_om_params

    test_params = ParameterGrid(test_param_grid)
    for i in range(all_om_params):
        om_queue.put((om_params[i]['play_segements_length'],
                      om_params[i]['x_bins'],
                      om_params[i]['y_bins'],
                      test_params))

    for i in range(num_theads):
        worker = Thread(target=do_partial_investigation, args=(om_queue, dfs))
        worker.setDaemon(True)
        worker.start()

    om_queue.join()
    df = pd.concat(dfs, ignore_index=True)
    df.to_csv(json_directories.create_first_investigation_scores_csv_path())


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(tests_done=0)
def show_proceeding():
    global LOCK
    global ALL_MAPS_CONFIGS
    LOCK.acquire()
    show_proceeding.tests_done += 1
    print('DONE: {}/{}'.format(show_proceeding.tests_done, ALL_MAPS_CONFIGS))
    LOCK.release()

do_investigation()