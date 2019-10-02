import matplotlib.pyplot as plt

from codes.plots.draw_pitch import drawpitch
from codes.plots.players_avg_positions import draw_players_mean_positions
from codes.plots.players_list import draw_players_list


def draw_pass_map(team, home_name, away_name, map_type):
    pitchFig = plt.figure()
    if team.team_name == home_name:
        home_name = r"$\bf{" + home_name + "}$"
    else:
        away_name = r"$\bf{" + away_name + "}$"
    pitchFig.suptitle(map_type + ' pass map: ' + home_name + ' v ' + away_name, fontsize=25)
    pitch_ax = pitchFig.add_axes([0.02, 0, 3.5/6, 1])
    players_ax = pitchFig.add_axes([3.5/6+0.03, 0, 1/3+0.03, 1])
    pitch_ax = drawpitch(pitch_ax, measure='SBData', grass_cutting=True)
    pitch_ax = draw_players_mean_positions(pitch_ax, team)
    pitch_ax = draw_pass_network(pitch_ax, team)
    players_ax = draw_players_list(players_ax, team)

def draw_pass_network(ax, team, line_color='black'):
    max_passes = max([sum(player.passes_cnt.values()) for player in team.lineup])
    for passer in team.lineup:
        if passer.in_xi:
            for receiver_id, cnt in passer.passes_cnt.items():
                receiver = team.get_player(receiver_id)

                ax.plot([passer.avg_position[0], receiver.avg_position[0]],
                        [passer.avg_position[1], receiver.avg_position[1]],
                        linewidth=7.5 *(cnt/max_passes),
                        color=line_color,
                        zorder=0)
    return ax