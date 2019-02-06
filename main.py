from code.db_connection.db_connection import DbConnection
from code.models.stats_bomb.services.events_services.players_events_service import PlayersEventsService
from code.models.stats_bomb.services.lineup_services.lineupService import LineupService
from code.plots.pitch import drawPitch
from code.plots.playersMeanPositions import drawPlayersMeanPositions

if __name__ == "__main__":
    # drawPitch()
    # sbJsonUtils = SBJsonUtils()
    # events = sbJsonUtils.readSBDataInTypeFromJsons('event')
    # sequenceInAttack = SequenceInAttack()
    dbConnection = DbConnection()
    lineUpService = LineupService()
    playersEventsService = PlayersEventsService()


    events = dbConnection.returnEventsCollection().find({'match_id': 19714}).sort([("index", 1)])
    matches = dbConnection.returnMatchesCollection().find({'_id': 19714})
    lineups = lineUpService.returnMatchesLineups(matches)
    playersEvents = playersEventsService.divideMatchEventsBetweenPlayers(events, lineups, 19714)
    print(playersEvents.keys())
    print(playersEvents[19714].keys())

    playersEvents[19714] = playersEventsService.getAvgPlayersEventsPositions(playersEvents[19714])
    for k in playersEvents[19714].keys():
        print('-----------------------------')
        for v in playersEvents[19714][k].values():
            print(v['player_name'] + ' - ' + str(v['avg_position']))

    pitch = drawPitch()
    drawPlayersMeanPositions(pitch, playersEvents[19714][746])

    #
    # attackingSequences = sequenceInAttack.getAttackSequencesWithTooShortRemoved(events);
    #
    # for sequence in attackingSequences:
    #     print('------ NEXT SEQUENCE -----')
    #     for elem in sequence:
    #         print(elem)
    #
    #     drawPitch(sequence)