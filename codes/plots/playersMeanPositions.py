import matplotlib.pyplot as plt

from codes.plots.pitch import drawPitch


def drawPlayersMeanPositions(team):
    drawPitch()
    for player in team.lineup:
        if player.havePlayedInGame():
            plt.plot(player.avg_position[0], player.avg_position[1], 'x', color="blue")
    plt.show()