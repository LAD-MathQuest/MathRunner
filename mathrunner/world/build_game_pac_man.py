#------------------------------------------------------------------------------#

'''Build game Pac Man

Author: Emanuelle Lima
Name: Pac Man

Description
A magical adventure with Wizard
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, BoundaryFunctions
from world.meta_world import MetaImage, MetaObject, MetaScoreboard, MetaWorld

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building: Pac Man')

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

    game_file_name        = "pacman.game"
    meta.soft_name        = "Pac Man"
    meta.soft_author      = "Emanuelle Lima"
    meta.soft_description = "Ajude o Pac Man a fugir dos fantasmas e a comer cerejas"
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = path_sounds/'pacman.mp3'
    meta.game_ambience_volume = 0.7

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'pistapacman.png'
    imag_background = MetaImage((1920,1080), path=path_background)
    
    meta.background_image = imag_background
    meta.background_scrolls = True

    meta.track_image   = False
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    path_font = path_fonts/'Arcade.ttf'
    meta.scoreboard = MetaScoreboard(image=MetaImage(color=(59,29,139),size=(280,100)),
                                     image_position=(153,13),
                                     text_font      = path_font,
                                     text_font_size = 15,
                                     text_spacing   = 1.3,
                                     text_position  = (160,20),
                                     text_bgcolor   = (59,29,139))

    # Player
    #--------------------------------------------------------------------------#

    imag_player = MetaImage(path=path_objects/'pacman.png', size=(130,130))
    meta.player = MetaObject(imag_player)
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    points = 10

    meta.obstacles_frequency = 2
    meta.obstacles = []

    imag_obstacle = MetaImage(path=path_objects/'fantasmavermelho.png', size=(130,130))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    imag_obstacle = MetaImage(path=path_objects/'fantasmaverde.png', size=(130,130))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    imag_obstacle = MetaImage(path=path_objects/'fantasmaazul.png', size=(130,130))
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#

    points = 100
    volume = 1.5

    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage(path=path_objects/'cereja.png', size=(120,120))
    meta.collectibles.append(MetaObject(imag_collectible, points, sound=path_sounds/'pacmaneat.mp3', volume=1.0))

    
    # Oil spill
    path_collect = path_sounds/'pacmanpain.mp3'

    # File image size [312, 344]
    path_collectible = path_objects/'cerejaveneno.png'
    imag_collectible = MetaImage((100,110), path=path_collectible)

    collectible = MetaObject(imag_collectible, points, path_collect, volume)
    meta.collectibles.append(collectible)


    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('0.2 + 0.01*t')
    meta.boundary = BoundaryFunctions('1', '9')

    # Saving
    #--------------------------------------------------------------------------#

    path = path_games/game_file_name
    meta.save(path)

#------------------------------------------------------------------------------#

