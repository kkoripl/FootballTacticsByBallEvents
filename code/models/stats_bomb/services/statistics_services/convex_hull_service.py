from scipy.spatial import ConvexHull


class ConvexHullService:
    def createPlayersConvexHulls(self, playersEvents):
        for team in playersEvents.keys():
            print(team)
            for player in playersEvents[team].keys():
                #print(playersEvents[team][player])
                playersEvents[team][player]['convexHulls']['attack'] = self.createConvexHull(playersEvents[team][player]['eventsLocations']['attack'])
                playersEvents[team][player]['convexHulls']['defence'] = self.createConvexHull(playersEvents[team][player]['eventsLocations']['defence'])
        return playersEvents

    def createConvexHull(self, playerEventsLocations):
        print('Liczba punktow: ' + str(len(playerEventsLocations)))
        if len(playerEventsLocations) < 3:
            return None
        else :
            return ConvexHull([eventLocation for eventLocation in playerEventsLocations])
