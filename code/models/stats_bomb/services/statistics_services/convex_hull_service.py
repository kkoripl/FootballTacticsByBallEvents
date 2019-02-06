from scipy.spatial import ConvexHull

class ConvexHullService:
    def createPlayersConvexHulls(self, playersEventsLocations):
        return [[playersEventsLocations.player, self.createConvexHull(eventLocations)]
                for eventLocations in playersEventsLocations]

    def createConvexHull(self, points):
        return ConvexHull(points)