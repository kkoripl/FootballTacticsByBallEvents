from code.data_parsers.stats_bomb.DataParser import jsonLineup2Obj, jsonEvents2Obj
from code.db_connection.db_connection import DbConnection
from code.models.classes.match import Match
from code.models.stats_bomb.services.events_services.players_events_service import PlayersEventsService
from code.models.stats_bomb.services.lineup_services.lineupService import LineupService
from code.models.stats_bomb.services.statistics_services.convex_hull_service import ConvexHullService
from code.plots.playersMeanPositions import drawPlayersMeanPositions

if __name__ == "__main__":
    dbConnection = DbConnection()
    lineUpService = LineupService()
    playersEventsService = PlayersEventsService()
    convexHullService = ConvexHullService()

    events = dbConnection.returnEventsCollection().find({'match_id': 19714}).sort([("index", 1)])
    events = jsonEvents2Obj(events)
    h = dbConnection.returnLineupsCollection().find_one({'match_id': 19714, 'team_id': 971})
    a = dbConnection.returnLineupsCollection().find_one({'match_id': 19714, 'team_id': 746})
    match = Match(19714, jsonLineup2Obj(h), jsonLineup2Obj(a))
    match = playersEventsService.divideMatchEventsBetweenPlayers(events, match)
    drawPlayersMeanPositions(match.home)
    drawPlayersMeanPositions(match.away)
    # input("Press Enter to continue...")

    # lineup2 = jsonLineup2Obj(lineup2)

    # print(e)
    # input("Press Enter to continue...")
    # matches = dbConnection.returnMatchesCollection().find({'_id': 19714})
    # lineups = lineUpService.returnMatchesLineups(matches)
    # playersEvents = playersEventsService.divideMatchEventsBetweenPlayers(events, lineups, 19714)
    # print(playersEvents.keys())
    # print(playersEvents[19714].keys())

    # # for k in playersEvents[19714].keys():
    # for item in playersEvents[19714][746].items():
    #     print(item)

     # playersEvents[19714] = playersEventsService.getAvgPlayersEventsPositions(playersEvents[19714])
    # playersEvents[19714] = convexHullService.createPlayersConvexHulls(playersEvents[19714])
    # for k in playersEvents[19714].keys():
    #     print('-----------------------------')
    #     for v in playersEvents[19714][k].values():
    #         print(v['player_name'] + ' - ' + str(v['avg_position']))
    #
    # pitch = drawPitch()
    # drawPlayersMeanPositions(pitch, playersEvents[19714][746])
    # print('-------- convex hull 746')
    # drawConvexHulls(pitch, playersEvents[19714][746])
    # print('-------- convex hull 971')
    # drawConvexHulls(pitch, playersEvents[19714][971])

    #
    # attackingSequences = sequenceInAttack.getAttackSequencesWithTooShortRemoved(events);
    #
    # for sequence in attackingSequences:
    #     print('------ NEXT SEQUENCE -----')
    #     for elem in sequence:
    #         print(elem)
    #
    #     drawPitch(sequence)