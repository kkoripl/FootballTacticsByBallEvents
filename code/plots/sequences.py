import matplotlib.pyplot as plt

from code.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from code.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from code.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from code.models.stats_bomb.services.events_services.particular_events.shot_service import Shot


def drawSequence(sequence, sub_plot):
    lastBallReceiptEvent = None
    for event in sequence:
        if Pass.isPass(event):
            if lastBallReceiptEvent is not None:
                if lastBallReceiptEvent[pefn.TYPE][pefn.ID] == pe.DRIBBLE:
                    drawRunningWithBallWoStart(lastBallReceiptEvent, event)
                else:
                    drawRunningWithBallWithStart(lastBallReceiptEvent, event)
            drawPass(event, sub_plot)
        elif Shot.isShot(event):
            drawShot(event, sub_plot)
        elif event[pefn.TYPE][pefn.ID] == pe.DRIBBLE:
            if lastBallReceiptEvent is not None:
                drawRunningWithBallWithStart(lastBallReceiptEvent, event)
            drawDribble(event)
            lastBallReceiptEvent = event
        elif event[pefn.TYPE][pefn.ID] in (pe.BALL_RECEIPT, pe.BALL_RECOVERY):
            lastBallReceiptEvent = event

def drawPass(pass_event, sub_plot):
    plt.plot([int(pass_event["location"][0]), int(pass_event["pass"]["end_location"][0])],
             [int(pass_event["location"][1]), int(pass_event["pass"]["end_location"][1])],
             color="blue")

    plt.plot(int(pass_event["location"][0]), int(pass_event["location"][1]), "o", color="green")

def drawShot(shot_event, sub_plot):
    plt.plot([int(shot_event["location"][0]), int(shot_event["shot"]["end_location"][0])],
             [int(shot_event["location"][1]), int(shot_event["shot"]["end_location"][1])],
             color="red")

    plt.plot(int(shot_event["location"][0]), int(shot_event["location"][1]), "o", color="green")

def drawRunningWithBallWithStart(start_event, stop_event):
    plt.plot([int(start_event["location"][0]), int(stop_event["location"][0])],
             [int(start_event["location"][1]), int(stop_event["location"][1])],
             "--",
             color="purple")
    plt.plot(int(start_event["location"][0]), int(start_event["location"][1]), "o", color="purple")

def drawRunningWithBallWoStart(start_event, stop_event):
    plt.plot([int(start_event["location"][0]), int(stop_event["location"][0])],
             [int(start_event["location"][1]), int(stop_event["location"][1])],
             "--",
             color="purple")

def drawDribble(dribble_event):
    plt.plot(int(dribble_event["location"][0]), int(dribble_event["location"][1]), "^", color="orange")