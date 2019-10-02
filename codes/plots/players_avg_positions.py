def draw_players_mean_positions(ax, team, in_color='green', edge_color='black'):

    xs = [player.avg_position[0] for player in team.lineup if player.in_xi]
    ys = [player.avg_position[1] for player in team.lineup if player.in_xi]
    numbers = [player.jersey_number for player in team.lineup if player.in_xi]

    for i, number in enumerate(numbers):
        ax.text(xs[i], ys[i], number,
                horizontalalignment='center', verticalalignment='center',
                size='medium', color='white',
                weight='semibold', zorder=2)

    ax.scatter(xs, ys, s=450, color=in_color, edgecolors=edge_color, zorder=1)
    return ax