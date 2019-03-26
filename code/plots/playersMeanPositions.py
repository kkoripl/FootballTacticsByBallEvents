import matplotlib.pyplot as plt

def drawPlayersMeanPositions(pitch, playersEvents):
    for playerLocation in playersEvents.values():
        plt.plot(playerLocation['avg_position'][0], playerLocation['avg_position'][1], 'x', color="blue")