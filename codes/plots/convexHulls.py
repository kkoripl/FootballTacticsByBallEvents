import matplotlib.pyplot as plt

from codes.plots.pitch import drawPitch


def drawConvexHulls(team):
    for player in team.lineup:
        drawPitch()
        if player.convex_hulls['defence'] is not None:
            drawPlayerConvexHulls(player.events_locations['defence'], player.convex_hulls['defence'], 'blue')
        if player.convex_hulls['attack'] is not None:
            drawPlayerConvexHulls(player.events_locations['attack'], player.convex_hulls['attack'], 'red')
        plt.plot(player.avg_position[0], player.avg_position[1], 'x', color="blue")
        plt.show()

def drawPlayerConvexHulls(eventsLocations, convexHulls, color):
    for simplex in convexHulls.simplices:
        plt.plot(eventsLocations[simplex, 0], eventsLocations[simplex, 1], '-', color="black")
        plt.fill(eventsLocations[convexHulls.vertices, 0],
                 eventsLocations[convexHulls.vertices, 1], color, alpha=0.05)
