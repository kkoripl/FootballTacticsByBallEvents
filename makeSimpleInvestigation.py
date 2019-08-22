from makeOccupancyMaps import makeOccupancyMaps
from predict_team_by_occupancy_maps import predict_team_by_occupancy_maps


def makeSimpleInvestigation(length, x_bin, y_bin, to, k):
    makeOccupancyMaps(length, x_bin, y_bin)
    score = predict_team_by_occupancy_maps(length, to, k)
    print(score)

makeSimpleInvestigation(length = 4,
                        x_bin = 5,
                        y_bin = 15,
                        to = 5,
                        k=5)