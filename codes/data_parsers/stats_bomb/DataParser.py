import json

from codes.models.classes.event import Event
from codes.models.classes.lineup import Lineup
from codes.models.classes.player import Player


def jsonEvents2Obj(data):
    events = []
    for event in data:
        events.append(jsonEvent2Obj(event))
    return events

def jsonEvent2Obj(data):
    data["id"] = data["_id"]
    data["pass_obj"] = data.get("pass")
    data.pop("_id", None)
    data.pop("pass", None)
    data = json.dumps(data) # take a dictionary as input and returns a string as output.
    return json.loads(data, object_hook=Event.from_dict) # take a string as input and returns a dictionary as output.

def jsonLineup2Obj(lineup):
    lineup.pop("_id", None)
    players = getPlayersFromLineup(lineup)
    lineup.pop("lineup", None)
    data = json.dumps(lineup)
    lineup = json.loads(data, object_hook=Lineup.from_dict)
    lineup.setLineup(players)
    return lineup

def getPlayersFromLineup(data):
    players = []
    playersLineup = data["lineup"]
    for player in playersLineup:
        players.append(jsonPlayer2Obj(player))
    return players


def jsonPlayer2Obj(data):
    data = json.dumps(data)  # take a dictionary as input and returns a string as output.
    return json.loads(data, object_hook=Player.from_dict)

