import json
import os

from codes.data_parsers.stats_bomb.json_directories import JsonDirectories


class SBJsonUtils:
    def __init__(self):
        json_directories = JsonDirectories()
        self.data_directories = {
            'competition': json_directories.getSBCompetitionsDirectory(),
            'match': json_directories.getSBMatchesDirectory(),
            'event': json_directories.getSBEventsDirectory(),
            'lineup': json_directories.getSBLineupsDirectory(),
        }
        
    def readSBDataInTypeFromJsons(self, wantedDataType):
        data_directory = self.data_directories.get(wantedDataType)
        data = []
        for filename in os.listdir(data_directory):
            if self.isJson(filename):
                file_location = os.path.join(data_directory, filename)
                with open(file_location, encoding='utf-8-sig') as json_file:
                    data.extend(self.loadDataFromJson(filename, json_file, wantedDataType))
        return data

    def readMatchEventsDataFromJson(self, match_id):
        file_name = self.build_file_name(match_id)
        data = []
        file_location = os.path.join(self.data_directories.get('event'), file_name)
        with open(file_location, encoding='utf-8-sig') as json_file:
            data.extend(self.loadDataFromJson(file_name, json_file, 'event'))
        return data

    def getAllMatches(self):
        data = []
        data_directory = self.data_directories.get('match')
        for file_name in os.listdir(data_directory):
            if self.isJson(file_name):
                file_location = os.path.join(data_directory, file_name)
                with open(file_location, encoding='utf-8-sig') as json_file:
                    data.extend(self.loadDataFromJson(file_name, json_file, 'match'))
        return data

    def readMatchLineupDataFromJson(self, match_id, team_id):
        file_name = self.build_file_name(match_id)
        data = []
        file_location = os.path.join(self.data_directories.get('lineup'), file_name)
        with open(file_location, encoding='utf-8-sig') as json_file:
            data.extend(self.loadDataFromJson(file_name, json_file, 'lineup'))
        return [x for x in data if x['team_id'] == team_id][0]

    def isJson(self, file):
        return file.endswith('.json')

    def loadDataFromJson(self, filename, json_file, wantedDataType):
        new_data = []
        for element in json.load(json_file):
            if wantedDataType in ['lineup', 'event']:
                self.addMatchId(element, filename)
            if wantedDataType != 'lineup':
                element = self.changeIdNameToId(element, wantedDataType)
            new_data.append(element)
        return new_data

    def changeIdNameToId(self, element, wantedDataType):
        if wantedDataType == 'event':
            element['_id'] = element.pop('id')
        else:
            element['_id'] = element.pop('{}{}'.format(wantedDataType, '_id'))
        return element

    def addMatchId(self, element, filename):
        element['match_id'] = int(filename.split('.', 1)[0]) #split on '.' and get first part
        return element

    def build_file_name(self, match_id):
        return str(match_id) + ".json"


