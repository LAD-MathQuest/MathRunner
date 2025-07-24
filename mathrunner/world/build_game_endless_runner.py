#------------------------------------------------------------------------------#

'''Build game 

Author: 
Name: 

Description

'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, BoundaryFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building: Endless Runner')

    path_resources   = Path(__file__).parents[1]/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'
    path_games       = path_resources/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    game_file_name        = 'endless_runner.game'
    meta.soft_name        = 'Endless Runner'
    meta.soft_author      = "Mariana Matias do Nascimento"
    meta.soft_description = 'A racing game where the character runs an infinite amount of time dodging obstacles'
    meta.soft_icon        = path_objects/'plane_1.png' 

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 1
    meta.game_ambience   = path_sounds/'run-away-runner.mp3'
    meta.game_ambience_volume = 0.4 

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'space.jpg'
    imag_background = MetaImage((1920,6000), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True

    meta.track_image   = None
    meta.track_scrolls = False
    meta.track_kills   = (True, True)

    path_score = path_scoreboards/'frame_neon.png'
    imag_score = MetaImage((390,160), path=path_score)

    path_font = path_fonts/'Electronic_Highway_Sign.ttf'

    meta.scoreboard = MetaScoreboard(image          = imag_score,
                                     image_position = (54,67),
                                     text_font      = path_font,
                                     text_font_size = 28,
                                     text_spacing   = 1.2,
                                     text_position  = (103,100),
                                     text_bgcolor   = (90,93,102),
                                     text_fgcolor   = (0,204,255))

    # Player
    #--------------------------------------------------------------------------#

    path_player = path_objects/'plane_1.png'
    imag_player = MetaImage((48,108), path=path_player)

    meta.player       = MetaObject(imag_player)
    meta.player_speed = 400

    # Obstacles
    #--------------------------------------------------------------------------#

    path_crash = path_sounds/'explosion.mp3'
    points = 10
    volume = 0.9

    meta.obstacles_frequency = 3
    meta.obstacles = []

    for ii in range(2,10):

        path_obstacle = path_objects/f'enemy_spaceship.png'
        imag_obstacle = MetaImage((80,80), path=path_obstacle)

        obstacle = MetaObject(imag_obstacle, points, path_crash, volume)
        meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    path_collect = path_sounds/'collect-ring.mp3'
    points = 100
    volume = 0.2

    meta.collectibles_frequency = 1
    meta.collectibles = []

    for ii in range(1,5):

        path_collectible = path_objects/f'ruby.png'
        imag_collectible = MetaImage((46,38), path=path_collectible)

        collectible = MetaObject(imag_collectible, points, path_collect, volume)
        meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + 2*t')
    meta.boundary = BoundaryFunctions('0', '10')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#
