import matplotlib.pyplot as plt
from matplotlib.patches import Arc

from codes.models.stats_bomb.data_preparation_models.pitch_location import PitchLocation as pl


def draw_pitch(ax):

    #Pitch Outline & Centre Line
    ax.plot([0, 0], [0, pl.Y_SIZE],  color="black") #left goalline
    ax.plot([0, pl.X_SIZE], [pl.Y_SIZE, pl.Y_SIZE],  color="black") #upper sideline
    ax.plot([pl.X_SIZE, pl.X_SIZE], [pl.Y_SIZE, 0],  color="black") #right goalline
    ax.plot([pl.X_SIZE, 0], [0, 0],  color="black") #bottom sideline
    ax.plot([pl.MIDDLE_CORDINATES[pl.X], pl.MIDDLE_CORDINATES[pl.X]], [0, pl.Y_SIZE],  color="black") #center line

    #Left Penalty Area
    ax.plot([18, 18], [62, 18], color="black")
    ax.plot([0, 18], [62, 62], color="black")
    ax.plot([18, 0], [18, 18], color="black")

    #Right Penalty Area
    ax.plot([pl.X_SIZE, 102], [62, 62], color="black")
    ax.plot([102, 102], [62, 18], color="black")
    ax.plot([102, pl.X_SIZE], [18, 18], color="black")

    #Left 6-yard Box
    ax.plot([0, 6], [50, 50], color="black")
    ax.plot([6, 6], [50, 30], color="black")
    ax.plot([6, 0], [30, 30], color="black")

    #Right 6-yard Box
    ax.plot([pl.X_SIZE, 114], [50, 50], color="black")
    ax.plot([114, 114], [50, 30], color="black")
    ax.plot([114, pl.X_SIZE], [30, 30], color="black")

    #Left goal
    ax.plot([0, -2], [36, 36], color="black")
    ax.plot([-2, -2], [36, 44], color="black")
    ax.plot([-2, 0], [44, 44], color="black")

    #Right Goal
    ax.plot([120, 122], [36, 36], color="black")
    ax.plot([122, 122], [36, 44], color="black")
    ax.plot([122, 120], [44, 44], color="black")

    #Prepare Circles
    centreCircle = plt.Circle(pl.MIDDLE_CORDINATES, 9.15, color="black",fill=False)
    centreSpot = plt.Circle(pl.MIDDLE_CORDINATES, 0.8, color="black")
    leftPenSpot = plt.Circle((12, 40), 0.8, color="black")
    rightPenSpot = plt.Circle((108, 40), 0.8, color="black")

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    #Prepare Arcs
    leftArc = Arc((12, 40), height=18.3, width=18.3, angle=0, theta1=310, theta2=50, color="black")
    rightArc = Arc((108, 40), height=18.3, width=18.3, angle=0, theta1=130, theta2=230, color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

    #Tidy Axes
    ax.axis('off')
    return ax