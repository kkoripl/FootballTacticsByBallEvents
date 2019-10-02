import os

import matplotlib

from codes.models.stats_bomb.data_preparation_models.pitch_location import PitchLocation
from codes.plots.pitch import draw_pitch

matplotlib.use('Agg')  # Must be before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as pyplot

def plot_combined_occupancy_map(home_entropy_map, away_entropy_map, match_data, path_to_folder):
    pitchFig = pyplot.figure()
    pitchFig.set_size_inches(7, 3)
    pyplot.axis('off')
    pyplot.title("%s vs. %s %d:%d" % (
        match_data['home_team'], match_data['away_team'], match_data['home_score'], match_data['away_score']))
    ax1 = pitchFig.add_subplot(121)
    ax2 = pitchFig.add_subplot(122)
    draw_pitch(ax1)
    ax1.imshow(home_entropy_map, interpolation='nearest',
               extent=(0, PitchLocation.X_SIZE, 0, PitchLocation.Y_SIZE), vmin=0, vmax=5.5, cmap=get_cmp())
    draw_pitch(ax2)
    img = ax2.imshow(away_entropy_map, interpolation='nearest',
                     extent=(0, PitchLocation.X_SIZE, 0, PitchLocation.Y_SIZE), vmin=0, vmax=5.5, cmap=get_cmp())
    pitchFig.subplots_adjust(right=0.8)
    cbar_ax = pitchFig.add_axes([0.85, 0.05, 0.01, 0.85])
    pitchFig.colorbar(img, cax=cbar_ax)
    pyplot.savefig(create_path_to_save_picture(path_to_folder, match_data))
    pyplot.close(pitchFig)


def plot_team_occupancy_map(team_entropy_map, match_data, path_to_folder):
    pitchFig = pyplot.figure()
    pitchFig.set_size_inches(7, 3)
    pyplot.axis('off')
    pyplot.title("%s vs. %s %d:%d" % (
        match_data['home_team'], match_data['away_team'], match_data['home_score'], match_data['away_score']))
    ax = pitchFig.add_subplot(111)
    draw_pitch(ax)
    img = ax.imshow(team_entropy_map, interpolation='nearest',
                    extent=(0, PitchLocation.X_SIZE, 0, PitchLocation.Y_SIZE), vmin=0, vmax=5.5, cmap=get_cmp())
    pitchFig.colorbar(img)
    pyplot.savefig(create_path_to_save_picture(path_to_folder, match_data))
    pyplot.close(pitchFig)

def get_cmp():
    return 'jet'

def create_path_to_save_picture(dir_path, match_data):
    return os.path.join(dir_path, str(match_data["match_id"]) + "_" + match_data['home_team'] + "_" + match_data[
        'away_team'] + ".png")