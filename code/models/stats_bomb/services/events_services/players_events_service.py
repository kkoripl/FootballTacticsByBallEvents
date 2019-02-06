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
        playersEvents[matchId][teamsIds[self.home]] = self.addEventsToPlayers(teamEvents[self.home], playersEvents[matchId][teamsIds[self.home]])
        playersEvents[matchId][teamsIds[self.away]] = self.addEventsToPlayers(teamEvents[self.away], playersEvents[matchId][teamsIds[self.away]])
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
            playersEvents[Event.getPlayerId(event)]['events'].append(event)
        return playersEvents

    def setupEventInPlayersData(self, lineups, matchId, teamsIds):
        [teamPlayer.update({'events': []}) for teamPlayer in lineups[matchId][teamsIds[self.home]].values()]
        [teamPlayer.update({'events': []}) for teamPlayer in lineups[matchId][teamsIds[self.away]].values()]
        return lineups

    def getAvgPlayerEventsPosition(self, playerEvents):
        locations = np.array([event['location'] for event in playerEvents if 'location' in event])
        if len(locations) == 0:
            return None
        else: return np.mean(locations, axis=0).tolist()

    def getAvgPlayersEventsPositions(self, teamPlayersEvents):
        for team in teamPlayersEvents.keys():
            for player in teamPlayersEvents[team].keys():
                teamPlayersEvents[team][player]['avg_position'] = self.getAvgPlayerEventsPosition(teamPlayersEvents[team][player]['events'])
        return teamPlayersEvents