import json
from code.data_parsers.json_utils import jsonToSBCompetition

if __name__ == "__main__":
    with open('resources/data/stats_bomb/competitions.json', encoding='utf-8-sig') as json_file:
        json_loaded_data = json.load(json_file)
        json_dumped_data = json.dumps(json_loaded_data)
        x3 = jsonToSBCompetition(json_dumped_data)
        print(x3)
        for x in x3:
            print(x)
