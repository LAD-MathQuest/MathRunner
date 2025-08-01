#------------------------------------------------------------------------------#
'''Build game Monkey in Danger

Author: Merc
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from meta import (
        VelocityFunction,
        BoundaryFunctions,
        MetaImage,
        MetaObject,
        MetaScoreboard,
        MetaWorld,
        save_meta,
        read_bytes_io
    )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building Monkey in danger')

    path_resources   = Path(__file__).parent/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'
    path_icons       = path_resources/'icons'

    path_games = Path(__file__).parents[1]/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    game_file_name        = 'monkey.game'
    meta.soft_name        = 'Monkey in Danger'
    meta.soft_author      = "Merc"
    meta.soft_description = 'Um jogo de corrida onde o macaco deve evitar as cobras e coletar as bananas'
    meta.soft_icon        = read_bytes_io(path_icons/'monkey.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'music-1.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1536,1024),
        path=path_backgrounds/'selva_vertical.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image   = None
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    meta.min_color = None
    meta.max_color = None
    meta.min_width = 3
    meta.max_width = 3

    # Scoreboard
    imag_score = MetaImage.from_file(size=(390,160),
        path=path_scoreboards/'frame_neon.png'
    )
    meta.scoreboard = MetaScoreboard(
        image          = imag_score,
        image_position = (54,67),
        text_font      = read_bytes_io(path_fonts/'Party_Confetti.ttf'),
        text_font_size = 28,
        text_spacing   = 1.2,
        text_position  = (103,100),
        text_bgcolor   = (90,93,102),
        text_fgcolor   = (0,204,255)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(60,100),
            path=path_objects/'macaco.png'
        )
    )
    meta.player_speed = 400

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage.from_file(size=(45, 67),
        path=path_objects/'cobra.png'
    )
    obstacle = MetaObject(
        image  = imag_obstacle,
        sound  = crash_sound,
        volume = 0.9
    )
    meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    collect_sound = read_bytes_io(path_sounds/'collect-ring.mp3')

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage.from_file(size=(55,67),
        path=path_objects/'banana.png'
    )
    collectible = MetaObject(
        image  = imag_collectible,
        score  = 100,
        sound  = collect_sound,
        volume = 0.2
    )
    meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + 2*t')
    meta.boundary = BoundaryFunctions('35', '65')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

