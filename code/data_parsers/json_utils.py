import json

from collections import namedtuple

from code.models.stats_bomb import sb_competition


def _json_object_hook(d):
    return namedtuple('X', d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


def jsonToSBCompetition(data):
    comps = []
    for comp in json2obj(data):
        comps.append(sb_competition.StatsBombCompetition(comp.competition_id, comp.season_id, comp.country_name,
                                                         comp.competition_name, comp.season_name, comp.match_updated,
                                                         comp.match_available))
    return comps
