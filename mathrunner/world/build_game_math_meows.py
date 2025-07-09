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

    print('Building: Math Meows')

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

    game_file_name        = 'math_meows.game'
    meta.soft_name        = 'Maths & Meows'
    meta.soft_author      = "Nandnn"
    meta.soft_description = "Help the math teacher save the kittens, watch out for the cars!"
    meta.soft_icon        = path_objects/'Teacher_PixelArt.png'

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = path_sounds/'music_theme_16bits.mp3'
    meta.game_ambience_volume = 0.4 

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'campus_background.png'
    imag_background = MetaImage((2130,1231), path=path_background)

    meta.background_image   = imag_background
    meta.background_scrolls = True

    meta.track_image   = False
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    path_font = path_fonts/'Party_Confetti.ttf'
    meta.scoreboard = MetaScoreboard(image=MetaImage(color=(55,55,55),size=(230,100)),
                                     image_position=(153,13),
                                     text_font      = path_font,
                                     text_font_size = 28,
                                     text_spacing   = 1,
                                     text_position  = (160,20),
                                     text_bgcolor   = (55,55,55))

    # Player
    #--------------------------------------------------------------------------#

    imag_player = MetaImage(path=path_objects/'teacher.png', size=(170,130))
    meta.player = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    points = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage(path=path_objects/'car_blue.png',size=(231,120)) #size (largura, altura);
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    imag_obstacle = MetaImage(path=path_objects/'car_red.png',size=(230,130))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    imag_obstacle = MetaImage(path=path_objects/'car_green.png',size=(224,126))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#
    path_collect = path_sounds/'meow_01.mp3'
    points = 100
    volume = 0.4

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage(path=path_objects/'cat-1.png', size=(160,100))
    meta.collectibles.append(MetaObject(imag_collectible, points, path_collect, volume))

    path_collect = path_sounds/'meow_02.mp3'
    points = 100
    volume = 0.4

    imag_collectible = MetaImage(path=path_objects/'cat-2.png', size=(160,100))
    meta.collectibles.append(MetaObject(imag_collectible, points, path_collect, volume))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('0.25 + 0.005*t')
    meta.boundary = BoundaryFunctions('1.8', '9 + sin(pi*x/40)')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#

