import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def draw_players_list(ax, team):
    team.lineup.sort(key=lambda player: player.jersey_number, reverse=False)
    cell_text = [[player.jersey_number, player.player_nickname] if player.player_nickname is not None
                 else [player.jersey_number, player.player_name]
                 for player in team.lineup if player.in_xi]

    table = ax.table(cellText=cell_text,
                     colLabels=('#', 'Player'),
                     loc='center')

    table.auto_set_font_size(False)
    set_align_for_column(table, col=0, align="center")
    set_align_for_column(table, col=1, align="left")
    table.scale(1, 1)

    cell_dict = table.get_celld()
    for i in range(12):
        if i == 0:
            style_header_number_cell(cell_dict[(i, 0)])
            style_header_name_cell(cell_dict[(i, 1)])
        else:
            style_player_number_cell(cell_dict[(i, 0)])
            style_player_name_cell(cell_dict[(i, 1)])

    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right', 'top', 'bottom', 'left']:
        plt.gca().spines[pos].set_visible(False)

    return ax

def style_header_number_cell(cell):
    style_number_col_width(cell)
    style_cell_borders(cell, 'B', 'grey')
    style_header_font(cell)

def style_header_name_cell(cell):
    style_name_col_width(cell)
    style_cell_borders(cell, 'B', 'grey')
    style_header_font(cell)

def style_player_number_cell(cell):
    style_number_col_width(cell)
    style_cell_borders(cell, 'B', 'grey')
    cell.set_text_props(fontproperties=FontProperties(weight='bold', size=15))

def style_player_name_cell(cell):
    style_name_col_width(cell)
    style_cell_borders(cell, 'B', 'grey')
    cell.set_text_props(fontproperties=FontProperties(size=15))

def style_cell_borders(cell, visible_borders, border_color):
    cell.set_edgecolor(border_color)
    cell.visible_edges = visible_borders

def style_header_font(cell):
    cell.set_text_props(fontproperties=FontProperties(weight='bold', size=18))

def style_number_col_width(cell):
    cell.set_width(0.07)

def style_name_col_width(cell):
    cell.set_width(0.67)

def set_align_for_column(table, col, align="left"):
    cells = [key for key in table._cells if key[1] == col]
    for cell in cells:
        table._cells[cell]._loc = align