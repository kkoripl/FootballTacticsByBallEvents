import matplotlib.pyplot as plt

from plots.draw_pitch import drawpitch
from plots.players_avg_positions import draw_players_mean_positions


def draw_pass_network(ax, team, line_color='black'):
    max_passes = max([sum(player.passes_cnt.values()) for player in team.lineup])
    for passer in team.lineup:
        if passer.in_xi:
            for receiver_id, cnt in passer.passes_cnt.items():
                receiver = team.get_player(receiver_id)

                ax.plot([passer.avg_position[0], receiver.avg_position[0]],
                         [passer.avg_position[1], receiver.avg_position[1]],
                         linewidth=20*(cnt / max_passes), color=line_color,
                        zorder =0)
    return ax

def draw_pass_map(match):
    pitchFig = plt.figure()
    ax = pitchFig.add_subplot(111)
    ax = drawpitch(ax, measure='SBData', grass_cutting=True)
    ax = draw_players_mean_positions(ax, match.home)
    ax = draw_pass_network(ax, match.home)

