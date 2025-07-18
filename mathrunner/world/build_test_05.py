#------------------------------------------------------------------------------#
'''Test game 05

Tilling background and track
Horizontal scrollling
Background doesn't scroll
Track doesn't scroll
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, BoundaryFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building test game 05')

    path_resources = Path(__file__).parents[1]/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'
    path_games       = path_resources/'games'
    path_tests       = path_resources/'tests'

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

    # Appearance
    #--------------------------------------------------------------------------#

    meta.background_image   = MetaImage(path=path_tests/'tile-blue.png',size=(400,400))
    meta.background_scrolls = False

    meta.track_image   = MetaImage(path=path_tests/'tile-green.png')
    meta.track_scrolls = False
    meta.track_kills   = (True, True)

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

    meta.velocity = VelocityFunction('0.4 + 0.005*t')
    meta.boundary = BoundaryFunctions(
        '2 + 1.5*sin(x/10) + 0.2*cos(0.8*x)', 
        '8 + 1.5*sin(x/20) + 0.2*cos(1.2*x)'
    )

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#

