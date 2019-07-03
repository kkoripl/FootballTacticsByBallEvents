import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from codes.data_parsers.stats_bomb.DataParser import jsonLineup2Obj, jsonEvents2Obj
from codes.db_connection.db_connection import DbConnection
from codes.models.classes.match import Match
from codes.models.stats_bomb.services.events_services.players_events_service import PlayersEventsService
from codes.models.stats_bomb.services.lineup_services.lineupService import LineupService
from codes.models.stats_bomb.services.sequence_services.sequence_in_attack_service import PossessionStringsService
from codes.models.stats_bomb.services.statistics_services.convex_hull_service import ConvexHullService
from codes.plots.pitch import drawPitch

if __name__ == "__main__":
    dbConnection = DbConnection()
    lineUpService = LineupService()
    playersEventsService = PlayersEventsService()
    convexHullService = ConvexHullService()
    possStrings = PossessionStringsService()

    events = dbConnection.returnEventsCollection().find({'match_id': 19714}).sort([("index", 1)])
    events = jsonEvents2Obj(events)
    h = dbConnection.returnLineupsCollection().find_one({'match_id': 19714, 'team_id': 971})
    a = dbConnection.returnLineupsCollection().find_one({'match_id': 19714, 'team_id': 746})
    match = Match(19714, jsonLineup2Obj(h), jsonLineup2Obj(a))
    match = playersEventsService.divideMatchEventsBetweenPlayersAndTeams(events, match)
    possession_strings = possStrings.getPossessionStringsWithTooShortRemoved(match.home.events)
    play_segments = possStrings.makePlaySegments(match.home.events)
    # drawPlayersMeanPositions(match.home)
    # drawPlayersMeanPositions(match.away)
    # drawConvexHulls(match.home)
    # drawConvexHulls(match.away)

    for player in match.home.lineup:
        if len(player.events_locations['attack']) != 0 and len(player.events_locations['defence']) != 0:
            locations = np.concatenate((player.events_locations['attack'], player.events_locations['defence']), axis=0)
            sns.set_style("white")
            drawPitch()
            fit = sns.kdeplot(locations[:, 0], locations[:, 1], kernel='gau', n_levels=1, cbar=True)
            # print(fit)
            plt.show()

    #
    # attackingSequences = sequenceInAttack.getAttackSequencesWithTooShortRemoved(events);
    #
    # for sequence in attackingSequences:
    #     print('------ NEXT SEQUENCE -----')
    #     for elem in sequence:
    #         print(elem)
    #
    #     drawPitch(sequence)