import time

from make_occupancy_maps import make_occupancy_maps
from predict_team_by_occupancy_maps import predict_team_by_occupancy_maps


def make_simple_first_investigation(length, x_bin, y_bin, to, k):
    start_time = time.time()
    make_occupancy_maps(length, x_bin, y_bin)
    score = predict_team_by_occupancy_maps(length, x_bin, y_bin, to, k)
    print(score)
    elapsed_time = time.time() - start_time
    print(str(elapsed_time))


make_simple_first_investigation(length=4,
                                x_bin=5,
                                y_bin=15,
                                to=5,
                                k=5)
