import matplotlib.pyplot as plt

from codes.plots.pitch import draw_pitch


def draw_players_mean_positions(team):
    pitchFig = plt.figure()
    pitchFig.set_size_inches(7, 3)
    plt.axis('off')
    draw_pitch(pitchFig)
    for player in team.lineup:
        if player.has_played_in_game():
            plt.plot(player.avg_position[0], player.avg_position[1], 'x', color="blue")
    plt.show()