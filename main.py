import os

from code.data_parsers.json_utils import readSBCompetitionsFromJson, readSBMatchesFromJson
from code.data_parsers import json_directories
if __name__ == "__main__":

    competitionsDirectory = json_directories.getSBCompetitionsDirectory()
    matchesDirectory = json_directories.getSBMatchesDirectory()

    for competitionFile in os.listdir(competitionsDirectory):
        if competitionFile.endswith('.json'):
            print(' ------- COMPETITION FILE ------')
            comps = readSBCompetitionsFromJson('{}/{}'.format(competitionsDirectory, competitionFile))
            for comp in comps:
                print(comp)

    for matchFile in os.listdir(matchesDirectory):
        if matchFile.endswith('.json'):
            print(' ------- MATCH FILE ------')
            matches = readSBMatchesFromJson('{}/{}'.format(matchesDirectory, matchFile))
            for match in matches:
                print(match)
