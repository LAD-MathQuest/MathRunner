#------------------------------------------------------------------------------#
'''Test game 06

Tilling background and track
Horizontal scrollling
Background scrolls
Track scrolls
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
        save_meta
    )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building test 06')

    path_resources   = Path(__file__).parent/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'

    path_games = Path(__file__).parents[1]/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    game_file_name        = 'test-06.game'
    meta.soft_name        = 'Test 06'
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

    meta.background_image   = MetaImage(path=path_backgrounds/'tile-blue.png')
    meta.background_scrolls = True

    meta.track_image   = MetaImage(path=path_backgrounds/'tile-green.png',size=(400,400))
    meta.track_scrolls = True
    meta.track_kills   = (False, False)

    meta.min_color = (255, 0, 0)
    meta.max_color = (255, 0, 0)
    meta.min_width = 3
    meta.max_width = 3

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

    meta.obstacles_frequency = 0.01
    meta.obstacles = []

    imag_obstacle = MetaImage((80,30), color=(200,50,50))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#

    points = 100

    meta.collectibles_frequency = 25
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

