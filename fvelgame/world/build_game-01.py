#------------------------------------------------------------------------------#

'''This script builds a Game example.

Author: Luis D'Afonseca
Name:   Racing

Description
Simple racing game with treasures and obstacles.
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, MarginFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld 

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game 01: Racing...')

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

    meta.soft_name        = 'Racing'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = 'Simple racing game with treasures and obstacles'
    meta.soft_icon        = None

    # Game 
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True   
    meta.game_time_bonus = 1
    meta.game_ambience   = path_sounds/'music-1.mp3'

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'racing_background.png'
    imag_background = MetaImage((1920,6000), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True
    
    meta.track_image = None

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

    path_player = path_objects/'sport_car-1.png'
    imag_player = MetaImage((48,108), path=path_player)

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
        
        path_obstacle = path_objects/f'sport_car-{ii}.png'
        imag_obstacle = MetaImage((40,90), path=path_obstacle)

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

    meta.velocity = VelocityFunction( 0.40, 0.02 )
    meta.margins  = MarginFunctions ( 0.35, 0.65 )

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/'racing.game'

    print(F'Writing: {path}')

    meta.save(path)

#------------------------------------------------------------------------------#

