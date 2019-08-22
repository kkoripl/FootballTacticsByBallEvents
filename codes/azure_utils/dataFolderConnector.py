import os

from codes.data_parsers.stats_bomb.json_directories import JsonDirectories


def connectDataFolder(parser):
    parser.add_argument('--data-folder', type=str, dest='data_folder', help='data folder mounting point')
    args = parser.parse_args()
    if args.data_folder is not None:
        head, tail = os.path.split(args.data_folder)
        JsonDirectories.DATA_DIRECTORY = head
        JsonDirectories.OUTPUTS_DIRECTORY = ''