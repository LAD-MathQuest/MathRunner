#------------------------------------------------------------------------------#

'''Build game Space

Author: Luis D'Afonseca
Name:   Racing

Description
Simple racing game with treasures and obstacles
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, BoundaryFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building: Space Game')

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

    game_file_name        = 'space.game'
    meta.soft_name        = 'space'
    meta.soft_author      = "Daniel Cristo"
    meta.soft_description = 'Desvie dos Asteroides e resgate os Astronautas'
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = path_sounds/'music_healthy.mp3'
    meta.game_ambience_volume = 0.4 

    # Appearance
    #--------------------------------------------------------------------------#
   
    path_background = path_backgrounds/'space.png'
    imag_background = MetaImage((1500,1500), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True

    meta.track_image   = MetaImage(color=(0,0,255))
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    path_score = path_scoreboards/'space_display.png'
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

    path_player = path_objects/'rocket.png'
    imag_player = MetaImage((320,320), path=path_player)

    meta.player       = MetaObject(imag_player)
    meta.player_speed = 400
    
    # Obstacles
    #--------------------------------------------------------------------------#

    path_crash = path_sounds/'car_crash.mp3'
    points = 10
    volume = 0.9

    meta.obstacles_frequency = 3
    meta.obstacles = []

    for ii in range(2,10):

        path_obstacle = path_objects/f'asteroid.png'
        imag_obstacle = MetaImage((192,192), path=path_obstacle)

        obstacle = MetaObject(imag_obstacle, points, path_crash, volume)
        meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    points = 100

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage(size=(128, 128), path=path_objects/'astronaut-green.png')
    meta.collectibles.append(MetaObject(imag_collectible, points))
    
    imag_collectible = MetaImage(size=(128, 128), path=path_objects/'astronaut-white.png')
    meta.collectibles.append(MetaObject(imag_collectible, points))

    imag_collectible = MetaImage(size=(128, 128), path=path_objects/'astronaut-brown.png')
    meta.collectibles.append(MetaObject(imag_collectible, points))
    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + 2*t')
    meta.boundary = BoundaryFunctions('12', '90 + sin(pi*x/400)')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#
