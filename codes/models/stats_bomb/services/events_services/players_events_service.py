import numpy as np

from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from models.stats_bomb.services.events_services.particular_events.event_service import Event


class PlayersEventsService:

    def add_events_to_players(self, events, home_lineup, away_lineup):
        for event in events:
            if Event.get_event_type_id(event) == pe.STARTING_XI:
                if Event.is_team_event(event, home_lineup.team_id):
                    self.mark_first_eleven(event, home_lineup)
                else:
                    self.mark_first_eleven(event, away_lineup)
            if event.got_player():
                player = home_lineup.get_player(event.player.id)
                if player is None:
                    player = away_lineup.get_player(event.player.id)

                if player is not None:
                    if event.is_attacking_event():
                        player.add_attacking_event(event)
                    elif event.is_defending_event():
                        player.add_defensive_event(event)
        self.__extract_players_events_locations(home_lineup)
        self.__extract_players_events_locations(away_lineup)

    def mark_first_eleven(self, event, team):
        for player_info in event.tactics.lineup:
            team.get_player(player_info.player.id).in_xi = True

    def add_avg_positions_to_players(self, team):
        for player in team.lineup:
            player.avg_position = self.__calculate_avg_positions(player.events_locations['attack'], player.events_locations['defence'])

    def __extract_players_events_locations(self, team):
        for player in team.lineup:
            player.events_locations['attack'] = np.array([event.location for event in player.events['attack'] if event.location is not None])
            player.events_locations['defence'] = np.array([event.location for event in player.events['defence'] if event.location is not None])

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
