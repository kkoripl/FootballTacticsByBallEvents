import json

from code.models.classes.event import Event
from code.models.classes.lineup import Lineup
from code.models.classes.player import Player


def jsonEvents2Obj(data):
    events = []
    for event in data:
        events.append(jsonEvent2Obj(event))
    return events

def jsonEvent2Obj(data):
    data["id"] = data["_id"]
    del data["_id"]
    data = json.dumps(data) # take a dictionary as input and returns a string as output.
    return json.loads(data, object_hook=Event.from_dict) # take a string as input and returns a dictionary as output.

def jsonLineup2Obj(lineup):
    del lineup["_id"]
    players = getPlayersFromLineup(lineup)
    del lineup["lineup"]
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

