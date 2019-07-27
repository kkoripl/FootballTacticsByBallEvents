import numpy as np
from scipy.spatial.qhull import ConvexHull


class PlayersEventsService:

    def divideMatchEventsBetweenPlayersAndTeams(self, events, match):
        self.__addEventsToPlayersAndTeams(events, match.home, match.away)
        # self.__addAvgPositionsAndConvexHullsToPlayers(match.home)
        # self.__addAvgPositionsAndConvexHullsToPlayers(match.away)
        return match

    def __addEventsToPlayersAndTeams(self, events, homeLineup, awayLineup):
        for event in events:
            if event.gotPlayer():
                player = homeLineup.getPlayer(event.player.id)
                if player is None:
                    player = awayLineup.getPlayer(event.player.id)

                if player is not None:
                    self.__addEventToTeam(event, player, homeLineup, awayLineup)
                    if event.isAttackingEvent():
                        player.addAttackingEvent(event)
                    elif event.isDefendingEvent():
                        player.addDefensiveEvent(event)

    def __addEventToTeam(self, event, player, homeLineup, awayLineup):
        if homeLineup.gotPlayer(player.player_id):
            homeLineup.addEvent(event)
        else:
            awayLineup.addEvent(event)

    def __addAvgPositionsAndConvexHullsToPlayers(self, team):
        for player in team.lineup:
            player.events_locations['attack'] = np.array([event.location for event in player.events['attack'] if event.location is not None])
            player.events_locations['defence'] = np.array([event.location for event in player.events['defence'] if event.location is not None])
            player.convex_hulls['attack'] = self.__calculateConvexHulls(player.events_locations['attack'])
            player.convex_hulls['defence'] = self.__calculateConvexHulls(player.events_locations['defence'])
            player.avg_position = self.__calculateAvgPositions(player.events_locations['attack'], player.events_locations['defence'])

    def __calculateConvexHulls(self, locations):
        if len(locations) < 3:
            return None
        else:
            return ConvexHull([location for location in locations])

    def __calculateAvgPositions(self, attackLocations, defenceLocations):
        locations = None

        if len(attackLocations) != 0 and len(defenceLocations) != 0:
            locations = np.concatenate((defenceLocations, attackLocations), axis=0)
        elif len(defenceLocations) == 0:
            locations = attackLocations
        else:
            locations = defenceLocations

        if len(locations) == 0:
            return None
        else:
            return np.mean(locations, axis=0).tolist()
