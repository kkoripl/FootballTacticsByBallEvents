import json

from code.models.stats_bomb.match import sb_match
from code.models.stats_bomb.competition import sb_competition


def readSBCompetitionsFromJson(json_location):
    with open(json_location, encoding='utf-8-sig') as json_file:
        competitions = []
        for competition in json.load(json_file):
            competitions.append(sb_competition.StatsBombCompetition(competition))
    return competitions


def readSBMatchesFromJson(json_location):
    with open(json_location, encoding='utf-8-sig') as json_file:
        matches = []
        for match in json.load(json_file):
            matches.append(sb_match.StatsBombMatch(match))
    return matches
