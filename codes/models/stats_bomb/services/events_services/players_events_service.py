import numpy as np
from scipy.spatial.qhull import ConvexHull


class PlayersEventsService:

    def divide_events_for_players_and_teams(self, events, match):
        self.__add_events_to_players_and_teams(events, match.home, match.away)
        # self.__add_avg_positions_and_convex_hulls_to_players(match.home)
        # self.__add_avg_positions_and_convex_hulls_to_players(match.away)
        return match

    def __add_events_to_players_and_teams(self, events, home_lineup, away_lineup):
        for event in events:
            if event.got_player():
                player = home_lineup.get_player(event.player.id)
                if player is None:
                    player = away_lineup.get_player(event.player.id)

                if player is not None:
                    self.__add_event_to_team(event, player, home_lineup, away_lineup)
                    if event.is_attacking_event():
                        player.add_attacking_event(event)
                    elif event.is_defending_event():
                        player.add_defensive_event(event)

    def __add_event_to_team(self, event, player, home_lineup, away_lineup):
        if home_lineup.got_player(player.player_id):
            home_lineup.add_event(event)
        else:
            away_lineup.add_event(event)

    def __add_avg_positions_and_convex_hulls_to_players(self, team):
        self.__extract_players_events_locations(team)
        self.__add_avg_positions_to_players(team)
        self.__add_convex_hulls_to_players(team)

    def __extract_players_events_locations(self, team):
        for player in team.lineup:
            player.events_locations['attack'] = np.array([event.location for event in player.events['attack'] if event.location is not None])
            player.events_locations['defence'] = np.array([event.location for event in player.events['defence'] if event.location is not None])

    def __add_avg_positions_to_players(self, team):
        for player in team.lineup:
            player.avg_position = self.__calculate_avg_positions(player.events_locations['attack'], player.events_locations['defence'])

    def __add_convex_hulls_to_players(self, team):
        for player in team.lineup:
            player.convex_hulls['attack'] = self.__calculate_convex_hulls(player.events_locations['attack'])
            player.convex_hulls['defence'] = self.__calculate_convex_hulls(player.events_locations['defence'])

    def __calculate_convex_hulls(self, locations):
        if len(locations) < 3:
            return None
        else:
            return ConvexHull([location for location in locations])

    def __calculate_avg_positions(self, attack_locations, defence_locations):
        locations = None

        if len(attack_locations) != 0 and len(defence_locations) != 0:
            locations = np.concatenate((defence_locations, attack_locations), axis=0)
        elif len(defence_locations) == 0:
            locations = attack_locations
        else:
            locations = defence_locations

        if len(locations) == 0:
            return None
        else:
            return np.mean(locations, axis=0).tolist()
