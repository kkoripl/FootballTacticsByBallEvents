import matplotlib.pyplot as plt

from codes.models.stats_bomb.data_preparation_models import pitch_events_field_names as pefn
from codes.models.stats_bomb.data_preparation_models.pitch_events import PitchEvents as pe
from codes.models.stats_bomb.services.events_services.particular_events.ball_pass_service import Pass
from codes.models.stats_bomb.services.events_services.particular_events.shot_service import Shot


def draw_sequence(sequence, sub_plot):
    last_ball_receipt_event = None
    for event in sequence:
        if Pass.is_pass(event):
            if last_ball_receipt_event is not None:
                if last_ball_receipt_event[pefn.TYPE][pefn.ID] == pe.DRIBBLE:
                    draw_running_with_ball_wo_start(last_ball_receipt_event, event)
                else:
                    draw_running_with_ball_with_start(last_ball_receipt_event, event)
            draw_pass(event, sub_plot)
        elif Shot.is_shot(event):
            draw_shot(event, sub_plot)
        elif event[pefn.TYPE][pefn.ID] == pe.DRIBBLE:
            if last_ball_receipt_event is not None:
                draw_running_with_ball_with_start(last_ball_receipt_event, event)
            draw_dribble(event)
            last_ball_receipt_event = event
        elif event[pefn.TYPE][pefn.ID] in (pe.BALL_RECEIPT, pe.BALL_RECOVERY):
            last_ball_receipt_event = event


def draw_pass(pass_event, sub_plot):
    plt.plot([int(pass_event["location"][0]), int(pass_event["pass"]["end_location"][0])],
             [int(pass_event["location"][1]), int(pass_event["pass"]["end_location"][1])],
             color="blue")

    plt.plot(int(pass_event["location"][0]), int(pass_event["location"][1]), "o", color="green")


def draw_shot(shot_event, sub_plot):
    plt.plot([int(shot_event["location"][0]), int(shot_event["shot"]["end_location"][0])],
             [int(shot_event["location"][1]), int(shot_event["shot"]["end_location"][1])],
             color="red")

    plt.plot(int(shot_event["location"][0]), int(shot_event["location"][1]), "o", color="green")


def draw_running_with_ball_with_start(start_event, stop_event):
    plt.plot([int(start_event["location"][0]), int(stop_event["location"][0])],
             [int(start_event["location"][1]), int(stop_event["location"][1])],
             "--",
             color="purple")
    plt.plot(int(start_event["location"][0]), int(start_event["location"][1]), "o", color="purple")


def draw_running_with_ball_wo_start(start_event, stop_event):
    plt.plot([int(start_event["location"][0]), int(stop_event["location"][0])],
             [int(start_event["location"][1]), int(stop_event["location"][1])],
             "--",
             color="purple")


def draw_dribble(dribble_event):
    plt.plot(int(dribble_event["location"][0]), int(dribble_event["location"][1]), "^", color="orange")
