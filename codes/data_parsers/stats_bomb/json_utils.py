import json
import os

from codes.data_parsers.stats_bomb.json_directories import JsonDirectories


class SBJsonUtils:
    def __init__(self):
        json_directories = JsonDirectories()
        self.data_directories = {
            'competition': json_directories.get_sb_comp_dir(),
            'match': json_directories.get_sb_matches_dir(),
            'event': json_directories.get_sb_events_dir(),
            'lineup': json_directories.get_sb_lineups_dir(),
        }
        
    def read_sb_data_in_type_from_jsons(self, data_type):
        data_directory = self.data_directories.get(data_type)
        data = []
        for filename in os.listdir(data_directory):
            if self.is_json(filename):
                file_location = os.path.join(data_directory, filename)
                with open(file_location, encoding='utf-8-sig') as json_file:
                    data.extend(self.load_data_from_json(filename, json_file, data_type))
        return data

    def read_match_events_from_jsons(self, match_id):
        file_name = self.build_file_name(match_id)
        data = []
        file_location = os.path.join(self.data_directories.get('event'), file_name)
        with open(file_location, encoding='utf-8-sig') as json_file:
            data.extend(self.load_data_from_json(file_name, json_file, 'event'))
        return data

    def get_all_matches(self):
        data = []
        data_directory = self.data_directories.get('match')
        for file_name in os.listdir(data_directory):
            if self.is_json(file_name):
                file_location = os.path.join(data_directory, file_name)
                with open(file_location, encoding='utf-8-sig') as json_file:
                    data.extend(self.load_data_from_json(file_name, json_file, 'match'))
        return data

    def read_match_lineup_from_jsons(self, match_id, team_id):
        file_name = self.build_file_name(match_id)
        data = []
        file_location = os.path.join(self.data_directories.get('lineup'), file_name)
        with open(file_location, encoding='utf-8-sig') as json_file:
            data.extend(self.load_data_from_json(file_name, json_file, 'lineup'))
        return [x for x in data if x['team_id'] == team_id][0]

    def is_json(self, file):
        return file.endswith('.json')

    def load_data_from_json(self, filename, json_file, data_type):
        new_data = []
        elements = json.load(json_file)
        for element in elements:
            if data_type in ['lineup', 'event']:
                self.add_match_id(element, filename)
            if data_type != 'lineup':
                element = self.change_id_name_to_id(element, data_type)
            new_data.append(element)
        return new_data

    def change_id_name_to_id(self, element, data_type):
        if data_type == 'event':
            element['_id'] = element.pop('id')
        else:
            element['_id'] = element.pop('{}{}'.format(data_type, '_id'))
        return element

    def add_match_id(self, element, filename):
        element['match_id'] = int(filename.split('.', 1)[0]) #split on '.' and get first part
        return element

    def build_file_name(self, match_id):
        return str(match_id) + ".json"


