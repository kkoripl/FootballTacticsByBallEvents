import matplotlib.pyplot as plt

from code.plots.pitch import drawPitch


def drawConvexHulls(pitch, playersEvents):
    for playerEvents in playersEvents.values():
        drawPitch()
        if playerEvents['convexHulls']['defence'] != None:
            for simplex in playerEvents['convexHulls']['defence'].simplices:
                #print(playerEvents['eventsLocations']['defence'])
                plt.plot(playerEvents['eventsLocations']['defence'][simplex,0], playerEvents['eventsLocations']['defence'][simplex,1], '-', color="black")
            plt.fill(playerEvents['eventsLocations']['defence'][playerEvents['convexHulls']['defence'].vertices, 0],
                     playerEvents['eventsLocations']['defence'][playerEvents['convexHulls']['defence'].vertices, 1], 'blue', alpha=0.15)
            #plt.plot(playerEvents['avg_position'][0], playerEvents['avg_position'][1], 'x', color="blue")

        if playerEvents['convexHulls']['attack'] != None:
            for simplex in playerEvents['convexHulls']['attack'].simplices:
                # print(playerEvents['eventsLocations']['attack'])
                plt.plot(playerEvents['eventsLocations']['attack'][simplex, 0],
                         playerEvents['eventsLocations']['attack'][simplex, 1], '-', color="black")
            plt.fill(playerEvents['eventsLocations']['attack'][playerEvents['convexHulls']['attack'].vertices, 0],
                     playerEvents['eventsLocations']['attack'][playerEvents['convexHulls']['attack'].vertices, 1],
                     'red', alpha=0.15)
        plt.plot(playerEvents['avg_position'][0], playerEvents['avg_position'][1], 'x', color="blue")
        plt.show()
