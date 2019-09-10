import json

from codes.models.classes.event import Event
from codes.models.classes.lineup import Lineup
from codes.models.classes.player import Player


def json_events_2_obj(data):
    events = []
    for event in data:
        events.append(json_event_2_obj(event))
    return events


def json_event_2_obj(data):
    data["id"] = data["_id"]
    data["pass_obj"] = data.get("pass")
    data.pop("_id", None)
    data.pop("pass", None)
    data = json.dumps(data)  # take a dictionary as input and returns a string as output.
    return json.loads(data, object_hook=Event.from_dict)  # take a string as input and returns a dictionary as output.


def json_lineup_2_obj(lineup):
    lineup.pop("_id", None)
    players = get_players_from_lineup(lineup)
    lineup.pop("lineup", None)
    data = json.dumps(lineup)
    lineup = json.loads(data, object_hook=Lineup.from_dict)
    lineup.set_lineup(players)
    return lineup


def get_players_from_lineup(data):
    players = []
    players_lineup = data["lineup"]
    for player in players_lineup:
        players.append(json_player_2_obj(player))
    return players


def json_player_2_obj(data):
    data = json.dumps(data)  # take a dictionary as input and returns a string as output.
    return json.loads(data, object_hook=Player.from_dict)