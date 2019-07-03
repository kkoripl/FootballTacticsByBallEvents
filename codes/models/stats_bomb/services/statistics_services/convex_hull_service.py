from scipy.spatial import ConvexHull


class ConvexHullService:
    def createConvexHulls(self, match):
        self.createPlayersConvexHulls(match.home)
        self.createPlayersConvexHulls(match.away)

    def createPlayersConvexHulls(self, team):
        for player in team.lineup:
            player.convex_hulls['attack'] = self.createConvexHull(self.getAttackLocations(player.events))
            player.convex_hulls['defence'] = self.createConvexHull(self.getDefenceLocations(player.events))

    def getAttackLocations(self, events):
        return [event.location for event in events['attack']]

    def getDefenceLocations(self, events):
        return [event.location for event in events['defence']]

    def createConvexHull(self, eventsLocations):
        if len(eventsLocations) < 3:
            return None
        else:
            return ConvexHull([location for location in eventsLocations])
