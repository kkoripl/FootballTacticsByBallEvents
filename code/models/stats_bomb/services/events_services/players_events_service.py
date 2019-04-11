import numpy as np


class PlayersEventsService:

    def divideMatchEventsBetweenPlayers(self, events, match):
        self.__addEventsToPlayers(events, match.home, match.away)
        self.__addAvgPositionsToPlayers(match.home)
        self.__addAvgPositionsToPlayers(match.away)
        return match

    def __addEventsToPlayers(self, events, homeLineup, awayLineup):
        for event in events:
            if event.gotPlayer():
                player = homeLineup.getPlayer(event.player.id)
                if player is None:
                    player = awayLineup.getPlayer(event.player.id)

                if player is not None:
                    if event.isAttackingEvent:
                        player.addAttackingEvent(event)
                    elif event.isDefendingEvent:
                        player.addDefensiveEvent(event)

    def __addAvgPositionsToPlayers(self, team):
        attackLocations = None
        defenceLocations = None

        for player in team.lineup:
            attackLocations = np.array([event.location for event in player.events['attack'] if event.location is not None])
            defenceLocations = np.array([event.location for event in player.events['defence'] if event.location is not None])
            player.avg_position = self.__calculateAvgPositions(attackLocations, defenceLocations)

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
