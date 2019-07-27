# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot, cm
#
# from codes.data_parsers.stats_bomb.DataParser import jsonLineup2Obj, jsonEvents2Obj
# from codes.models.classes.match import Match
# from codes.models.stats_bomb.services.events_services.players_events_service import PlayersEventsService
# from codes.models.stats_bomb.services.lineup_services.lineupService import LineupService
# from codes.models.stats_bomb.services.sequence_services.possession_strings_service import PossessionStringsService
# from codes.models.stats_bomb.services.statistics_services.convex_hull_service import ConvexHullService
# from codes.plots.pitch import drawPitch
#
# if __name__ == "__main__":
#     lineUpService = LineupService()
#     playersEventsService = PlayersEventsService()
#     convexHullService = ConvexHullService()
#     possStrings = PossessionStringsService()
#     match = Match(19714, jsonLineup2Obj(h), jsonLineup2Obj(a), events)
#     match = playersEventsService.divideMatchEventsBetweenPlayersAndTeams(events, match)
#     match.home.possesion_strings, match.away.possesion_strings = possStrings.getPossessionStrings(match)
#     home_entropy_map, away_entropy_map = possStrings.createEventsEntropyMaps(match)
#     # possession_strings = possStrings.getPossessionStringsWithTooShortRemoved(match.home.events)
#     # entropyMapH = possStrings.createEventsEntropyMap(match.home.events)
#     # entropyMapA = possStrings.createEventsEntropyMap(match.away.events)
#     # play_segments = possStrings.makePlaySegments(match.home.events)
#     # drawPlayersMeanPositions(match.home)
#     # drawPlayersMeanPositions(match.away)
#     # drawConvexHulls(match.home)
#     # drawConvexHulls(match.away)
#
#     img = pyplot.imshow(home_entropy_map, interpolation='nearest')
#     pyplot.colorbar()
#     pyplot.show()
#     pyplot.close()
#
#     img2 = pyplot.imshow(away_entropy_map, interpolation='nearest')
#     pyplot.colorbar()
#     pyplot.show()
#
#     for player in match.home.lineup:
#         if len(player.events_locations['attack']) != 0 and len(player.events_locations['defence']) != 0:
#             locations = np.concatenate((player.events_locations['attack'], player.events_locations['defence']), axis=0)
#             sns.set_style("white")
#             drawPitch()
#             fit = sns.kdeplot(locations[:, 0], locations[:, 1], kernel='gau', n_levels=1, cbar=True)
#             # print(fit)
#             plt.show()
#
#     #
#     # attackingSequences = sequenceInAttack.getAttackSequencesWithTooShortRemoved(events);
#     #
#     # for sequence in attackingSequences:
#     #     print('------ NEXT SEQUENCE -----')
#     #     for elem in sequence:
#     #         print(elem)
#     #
#     #     drawPitch(sequence)