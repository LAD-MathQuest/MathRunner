#------------------------------------------------------------------------------#
'''Build game Healthy Run

Author: Lígia Aguiar
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

    print('Building Healthy Run')

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

    game_file_name        = 'healthy_run.game'
    meta.soft_name        = 'Healthy Run'
    meta.soft_author      = "Lígia Aguiar"
    meta.soft_description = "A game that encourages healthy eating"
    meta.soft_icon        = read_bytes_io(path_icons/'healthy_run.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'music_healthy.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1920,1800),
        path=path_backgrounds/'healthy_background.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image   = None
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    # Scoreboard
    meta.scoreboard = MetaScoreboard(
        text_font      = read_bytes_io(path_fonts/'Party_Confetti.ttf'),
        text_font_size = 25,
        text_spacing   = 1,
        text_position  = (160,20),
        text_bgcolor   = (34,139,34)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(75, 167),
            path=path_objects/'girl.png'
        )
    )
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'music_healthy2.mp3')
    points = -10
    volume = 0.7

    meta.obstacles_frequency = 3
    meta.obstacles = []

    sizes = [(80,104), (100,77), (80,108)]

    for ii in range(3):

        imag_obstacle = MetaImage.from_file(size=sizes[ii],
            path=path_objects / f'food-{ii+1}.png'
        )
        obstacle = MetaObject(
            image  = imag_obstacle,
            sound  = crash_sound,
            volume = 0.9
        )
        meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    collect_sound = read_bytes_io(path_sounds/'music_healthy1.mp3')

    meta.collectibles_frequency = 1
    meta.collectibles = []

    sizes = [(100,68), (100,99), (100,96)]

    for ii in range(3):

        imag_collectible = MetaImage.from_file(size=sizes[ii],
            path=path_objects / f'healthy_food-{ii+1}.png'
        )
        collectible = MetaObject(
            image  = imag_collectible,
            score  = 100,
            sound  = collect_sound,
            volume = 0.5
        )
        meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + t')
    meta.boundary = BoundaryFunctions('30', '70')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#
