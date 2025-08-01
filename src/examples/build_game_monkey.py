#------------------------------------------------------------------------------#
'''Build game Monkey in Danger

Author: Merc
Name:   Monkey in danger

Description
Monkey ir running away from one of its predators, the snakes.
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

    print('Building Monkey in danger')

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

    game_file_name        = 'monkey.game'
    meta.soft_name        = 'Monkey in danger'
    meta.soft_author      = "Merc"
    meta.soft_description = 'Um jogo de corrida onde o macaco deve evitar as cobras e coletar as bananas'
    meta.soft_icon        = None

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = path_sounds/'music-1.mp3'
    meta.game_ambience_volume = 0.4 

    # Appearance
    #--------------------------------------------------------------------------#

    path_background = path_backgrounds/'selva_vertical.png'
    imag_background = MetaImage((1536,1024), path=path_background)
    
    meta.background_image = imag_background
    meta.background_scrolls = True

    meta.track_image   = None
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    path_score = path_scoreboards/'frame_neon.png'
    imag_score = MetaImage((390,160), path=path_score)

    path_font = path_fonts/'Party_Confetti.ttf'
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

    path_player = path_objects/'macaco.png'
    imag_player = MetaImage((120,200), path=path_player)

    meta.player       = MetaObject(imag_player)
    meta.player_speed = 400

    # Obstacles
    #--------------------------------------------------------------------------#

    
    points = 10

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage((90, 135), path=path_objects/'cobra.png')
    meta.obstacles.append(MetaObject(imag_obstacle, points))

    # Collectibles
    #--------------------------------------------------------------------------#
    path_collect = path_sounds/'collect-ring.mp3'
    points = 100
    volume = 0.2
   
    meta.collectibles_frequency = 1
    meta.collectibles = []

    imag_collectible = MetaImage(( 110, 135), path=path_objects/'banana.png')
    meta.collectibles.append(MetaObject(imag_collectible, points))

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + 2*t')
    meta.boundary = BoundaryFunctions('35', '65')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

