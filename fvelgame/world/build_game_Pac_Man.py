#------------------------------------------------------------------------------#

'''This script builds a Game example

Author: Emanuelle Lima
Name:   Pac Man

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

    print('Building game 01: PacoMan')

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

    game_file_name        = 'pacoman.game'
    meta.soft_name        = 'Racing'
    meta.soft_author      = "Emanuelle Lima"
    meta.soft_description = 'Um jogo de corrida onde o jogador deve evitar os obstáculos e coletar as joias'
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 1
    meta.game_ambience   = path_sounds/'pacoman.mp3'

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'mazepacoman.png'
    imag_background = MetaImage((1920,6000), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True

    meta.track_image   = None
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

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

    path_player = path_objects/'pacoman.png'
    imag_player = MetaImage(size=(100,108), path=path_player)

    meta.player       = MetaObject(imag_player)
    meta.player_speed = 200

    # Obstacles
    #--------------------------------------------------------------------------#
    
    points = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage(path=path_objects/'ghostman.png', size=(100,100))
    meta.obstacles.append(MetaObject(imag_obstacle, points))



    # Collectibles
    #--------------------------------------------------------------------------#

    path_collect = path_sounds/'collect-ring.mp3'
    points = 100
    volume = 0.2

    meta.collectibles_frequency = 1
    meta.collectibles = []

    for ii in range(1,5):

        path_collectible = path_objects/f'precious_stone-{ii}.png'
        imag_collectible = MetaImage((46,38), path=path_collectible)

        collectible = MetaObject(imag_collectible, points, path_collect, volume)
        meta.collectibles.append(collectible)

    # Oil spill
    path_collect = path_sounds/'car_drift.mp3'
    points = -200
    volume = 1.0

    # File image size [312, 344]
    path_collectible = path_objects/'oil_spill.png'
    imag_collectible = MetaImage((100,110), path=path_collectible)

    collectible = MetaObject(imag_collectible, points, path_collect, volume)
    meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('0.2 + 0.01*t')
    meta.boundary = BoundaryFunctions('0.18', '0.9 + 0.1*sin(pi*x/4)')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#

