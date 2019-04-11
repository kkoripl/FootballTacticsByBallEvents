import matplotlib.pyplot as plt

from code.plots.pitch import drawPitch


def drawPlayersMeanPositions(team):
    drawPitch()
    for player in team.lineup:
        print(player.player_name)
        print(player.avg_position)
        if player.havePlayedInGame():
            plt.plot(player.avg_position[0], player.avg_position[1], 'x', color="blue")
    plt.show()