#------------------------------------------------------------------------------#
'''Build game Wizard's Journey

Author: Samuel Lopes
Name: Wizard's Journey

Description
A magical adventure with Wizard
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
        MetaWorld
    )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print("Building: Wizard's Journey")

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

    game_file_name        = "wizards_jorney.game"
    meta.soft_name        = "Wizard's Journey"
    meta.soft_author      = "Samuel Lopes"
    meta.soft_description = "Fuja das criaturas malignas enquanto avança em uma floresta mágica"
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = path_sounds/'music_theme_wizard.wav'
    meta.game_ambience_volume = 0.1

    # Appearance
    #--------------------------------------------------------------------------#
   
    meta.background_image   = MetaImage((1920,1080), path=path_backgrounds/'magical_woods.png')
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

    imag_player = MetaImage(path=path_objects/'wizard.png', size=(140,140))
    meta.player = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    points = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage(path=path_objects/'dragon.png', size=(120,140))
    meta.obstacles.append(MetaObject(imag_obstacle, points))
    imag_obstacle = MetaImage(path=path_objects/'wood_spirit.png', size=(120,140))
    meta.obstacles.append(MetaObject(imag_obstacle, points))
    imag_obstacle = MetaImage(path=path_objects/'evil_spirit.png', size=(120,140))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#

    points = 100

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage(path=path_objects/'grimorio.png', size=(80,100))
    meta.collectibles.append(MetaObject(imag_collectible, points, sound=path_sounds/'magic.mp3', volume=0.2))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction('25 + 2*t')
    meta.boundary = BoundaryFunctions('30','70')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#

