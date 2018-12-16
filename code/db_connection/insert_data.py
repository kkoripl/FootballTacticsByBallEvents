from code.data_parsers.stats_bomb.json_utils import SBJsonUtils
from code.db_connection import db_connection


def insert_data():
    db = db_connection.DbConnection()
    sbJsonUtils = SBJsonUtils()

    competitions = sbJsonUtils.readSBDataInTypeFromJsons('competition')
    db_competitions = db.returnCompetitionsCollection()
    for competition in competitions:
        db_competitions.replace_one(competition, competition, upsert=True)

    print('COMPETITIONS UPDATED')

    matches = sbJsonUtils.readSBDataInTypeFromJsons('match')
    db_matches = db.returnMatchesCollection()
    for match in matches:
        db_matches.replace_one(match, match, upsert=True)

    print('MATCHES UPDATED')

    lineups = sbJsonUtils.readSBDataInTypeFromJsons('lineup')
    db_lineups = db.returnLineupsCollection()
    for lineup in lineups:
        db_lineups.replace_one(lineup, lineup, upsert=True)

    print('LINEUPS UPDATED')

    events = sbJsonUtils.readSBDataInTypeFromJsons('event')
    db_events = db.returnEventsCollection()
    i = 0
    for ind in range(0,len(events), 50000):
        if ind+49999 > len(events):
            db_events.insert_many(events[ind:len(events)+1])
        else:
            db_events.insert_many(events[ind:ind+50000])
            print('EVENTS INSERTED: ' + str(ind+50000))
            db.disconnect()
            db.connect()
            db_events = db.returnEventsCollection()

    print('EVENTS UPDATED')
