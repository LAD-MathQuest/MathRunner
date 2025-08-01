#------------------------------------------------------------------------------#
'''Test game 05

Tilling background and track
Horizontal scrolling
Background doesn't scroll
Track doesn't scroll
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

    print('Building test 05')

    path_resources   = Path(__file__).parents[1]/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'

    path_games = Path(__file__).parents[2]/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    game_file_name        = 'test-05.game'
    meta.soft_name        = 'Test 05'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = meta.soft_name
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = None
    meta.game_ambience_volume = 0.4 

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image   = MetaImage.from_file(path=path_backgrounds/'tile-blue.png',size=(400,400))
    meta.background_scrolls = False

    # Track
    meta.track_image   = MetaImage.from_file(path=path_backgrounds/'tile-green.png')
    meta.track_scrolls = False
    meta.track_kills   = (True, True)

    meta.min_color = (255, 0, 0)
    meta.max_color = (255, 0, 0)
    meta.min_width = 3
    meta.max_width = 3

    # Scoreboard
    meta.scoreboard = MetaScoreboard(text_font_size = 28,
                                     text_spacing   = 1,
                                     text_position  = (160,20),
                                     text_bgcolor   = (55,55,55))

    # Player
    #--------------------------------------------------------------------------#

    imag_player       = MetaImage((90,40), color=(80, 86, 93))
    meta.player       = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    points = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage((80,30), color=(200,50,50))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#

    points = 100

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage((50,50), color=(242, 182, 0))
    meta.collectibles.append(MetaObject(imag_collectible, points))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction('40 + t')
    meta.boundary = BoundaryFunctions(
        '20 + 15*sin(x/10) + 2*cos(0.8*x)', 
        '80 + 15*sin(x/20) + 2*cos(1.2*x)'
    )

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

