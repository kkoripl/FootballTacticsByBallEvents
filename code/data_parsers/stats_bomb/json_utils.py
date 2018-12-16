import json
import os

from code.data_parsers.stats_bomb import json_directories

data_directories = {
    'competition': json_directories.getSBCompetitionsDirectory(),
    'match': json_directories.getSBMatchesDirectory(),
    'event': json_directories.getSBEventsDirectory(),
    'lineup': json_directories.getSBLineupsDirectory(),
}

class SBJsonUtils:
    def readSBDataInTypeFromJsons(self, wantedDataType):
        data_directory = data_directories.get(wantedDataType)
        data = []
        for filename in os.listdir(data_directory):
            if self.isJson(filename):
                file_location = '{}/{}'.format(data_directory, filename)
                with open(file_location, encoding='utf-8-sig') as json_file:
                    data.extend(self.loadDataFromJson(filename, json_file, wantedDataType))
            break
        return data

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


