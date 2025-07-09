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

    print('Building: Healthy Run')

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

    game_file_name        = 'healthy_run.game'
    meta.soft_name        = 'Healthy Run'
    meta.soft_author      = "Lígia Aguiar"
    meta.soft_description = "A game that encourages healthy eating"
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = path_sounds/'music_healthy.mp3'
    meta.game_ambience_volume = 0.4 

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'healthy_background.png'
    imag_background = MetaImage((1920,1800), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True

    meta.track_image   = None
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    path_font = path_fonts/'Party_Confetti.ttf'
    meta.scoreboard = MetaScoreboard(text_font      = path_font,
                                     text_font_size = 25,
                                     text_spacing   = 1,
                                     text_position  = (160,20),
                                     text_bgcolor   = (34,139,34))

    # Player
    #--------------------------------------------------------------------------#

    imag_player = MetaImage(size=(75, 167), path=path_objects/'girl.png')
    meta.player = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    path_crash = path_sounds/'music_healthy2.mp3'
    points = -10
    volume = 0.7

    meta.obstacles_frequency = 3
    meta.obstacles = []

    # Image sizes
    # file = [ (120,120), (150,150), (150,150)]
    # 
    sizes = [ (80,104),  (100,77), (80,108)]

    for ii in range(3):

        path_obstacle = path_objects / f'food-{ii+1}.png'
        imag_obstacle = MetaImage(sizes[ii], path=path_obstacle)

        meta.obstacles.append(MetaObject(imag_obstacle, points, path_crash, volume))
   

    # Collectibles
    #--------------------------------------------------------------------------#

    path_collect = path_sounds/'music_healthy1.mp3'
    points = 100
    volume = 0.5

    meta.collectibles_frequency = 1
    meta.collectibles = []

    # Image sizes
    # file = [ (150, 128), (130, 138), (150, 150)]
    sizes = [ (100,68), (100,99), (100,96)]

    for ii in range(3):
        path_collectible = path_objects / f'healthy_food-{ii+1}.png'
        imag_collectible = MetaImage(sizes[ii], path=path_collectible)
        meta.collectibles.append(MetaObject(imag_collectible, points, path_collect, volume))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('0.25 + 0.01*t')
    meta.boundary = BoundaryFunctions('3', '7')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#
