from collections import defaultdict

import numpy as np

from code.models.stats_bomb.services.events_services.particular_events.event_service import Event


class PlayersEventsService:
    def __init__(self):
        self.home = 0
        self.away = 1

    def divideMatchEventsBetweenPlayers(self, events, lineups, matchId):
        teamsIds = list(lineups[matchId].keys())
        teamEvents = self.divideMatchEventsBetweenTeams(events, teamsIds)
        playersEvents = self.setupEventInPlayersData(lineups, matchId, teamsIds)
        playersEvents = self.setupConvexHullsInPlayersData(lineups, matchId, teamsIds)
        playersEvents[matchId][teamsIds[self.home]] = self.addEventsToPlayers(teamEvents[self.home], playersEvents[matchId][teamsIds[self.home]])
        playersEvents[matchId][teamsIds[self.away]] = self.addEventsToPlayers(teamEvents[self.away], playersEvents[matchId][teamsIds[self.away]])
        for player in playersEvents[matchId][teamsIds[self.home]].values():
            player['eventsLocations']['defence'] = np.array(player['eventsLocations']['defence'])
            player['eventsLocations']['attack'] = np.array(player['eventsLocations']['attack'])
        for player in playersEvents[matchId][teamsIds[self.away]].values():
            player['eventsLocations']['defence'] = np.array(player['eventsLocations']['defence'])
            player['eventsLocations']['attack'] = np.array(player['eventsLocations']['attack'])
        return playersEvents

    def divideMatchEventsBetweenTeams(self, events, teamsIds):
        teamEvents = defaultdict(list)
        for event in events:
            if Event.isPlayerEvent(event):
                if Event.isTeamEvent(event, teamsIds[self.home]):
                    teamEvents[self.home].append(event)
                elif Event.isTeamEvent(event, teamsIds[self.away]):
                    teamEvents[self.away].append(event)
        return teamEvents

    def addEventsToPlayers(self, teamEvents, playersEvents):
        for event in teamEvents:
            if Event.isAttackingEvent(event):
                playersEvents[Event.getPlayerId(event)]['events']['attack'].append(event)
                if 'location' in event:
                    playersEvents[Event.getPlayerId(event)]['eventsLocations']['attack'].append(event['location'])
            elif Event.isDefendingEvent(event):
                playersEvents[Event.getPlayerId(event)]['events']['defence'].append(event)
                if 'location' in event:
                    playersEvents[Event.getPlayerId(event)]['eventsLocations']['defence'].append(event['location'])
        return playersEvents

    def setupConvexHullsInPlayersData(self, lineups, matchId, teamsIds):
        [teamPlayer.update({'convexHulls': {'attack': None, 'defence': None}}) for teamPlayer in lineups[matchId][teamsIds[self.home]].values()]
        [teamPlayer.update({'convexHulls': {'attack':  None, 'defence': None}}) for teamPlayer in lineups[matchId][teamsIds[self.away]].values()]
        return lineups

    def setupEventInPlayersData(self, lineups, matchId, teamsIds):
        [teamPlayer.update({'events': {'attack': [], 'defence': []}}) for teamPlayer in lineups[matchId][teamsIds[self.home]].values()]
        [teamPlayer.update({'eventsLocations': {'attack': [], 'defence': []}}) for teamPlayer in lineups[matchId][teamsIds[self.home]].values()]
        [teamPlayer.update({'events': {'attack': [], 'defence': []}}) for teamPlayer in lineups[matchId][teamsIds[self.away]].values()]
        [teamPlayer.update({'eventsLocations': {'attack': [], 'defence': []}}) for teamPlayer in lineups[matchId][teamsIds[self.away]].values()]
        return lineups

    def __getAvgPlayerEventsPosition(self, playerEvents):
        locationsAt = np.array([event['location'] for event in playerEvents['attack'] if 'location' in event])
        locations = np.array([event['location'] for event in playerEvents['defence'] if 'location' in event])
        print('locations: ' + str(locations.shape) + ' / locationsAt: ' + str(locationsAt.shape))

        if len(locationsAt) != 0 and len(locations) != 0:
            locations = np.concatenate((locations, locationsAt), axis=0)
        elif len(locations) == 0 : locations = locationsAt

        if len(locations) == 0:
            return None
        else: return np.mean(locations, axis=0).tolist()

    def getAvgPlayersEventsPositions(self, teamPlayersEvents):
        for team in teamPlayersEvents.keys():
            for player in teamPlayersEvents[team].keys():
                print('Zawodnik: ' + str(teamPlayersEvents[team][player]['player_name']))
                teamPlayersEvents[team][player]['avg_position'] = self.__getAvgPlayerEventsPosition(teamPlayersEvents[team][player]['events'])
        return teamPlayersEvents