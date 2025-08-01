#------------------------------------------------------------------------------#
'''Build game Student

Author: Luis D'Afonseca
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
        save_meta,
        read_bytes_io
    )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building Student')

    path_resources   = Path(__file__).parent/'resources'
    path_backgrounds = path_resources/'backgrounds'
    path_scoreboards = path_resources/'scoreboards'
    path_objects     = path_resources/'objects'
    path_sounds      = path_resources/'sounds'
    path_fonts       = path_resources/'fonts'
    path_icons       = path_resources/'icons'

    path_games = Path(__file__).parents[1]/'games'

    #--------------------------------------------------------------------------#

    meta = MetaWorld()

    # Software
    #--------------------------------------------------------------------------#

    game_file_name        = 'student.game'
    meta.soft_name        = 'Student'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = '''Um estudante confiante só quer saber de jogar videogames\nPerca o máximo de pontos fugindo dos livros e jogando videogames'''
    meta.soft_icon        = read_bytes_io(path_icons/'student.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = -2
    meta.game_ambience   = read_bytes_io(path_sounds/'music-1.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage(
        color=(55,55,55)
    )
    meta.background_scrolls = False

    # Track
    meta.track_image   = MetaImage(
        color=(102,153,153)
    )
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    meta.min_color = None
    meta.max_color = None
    meta.min_width = 3
    meta.max_width = 3

    # Scoreboard
    meta.scoreboard = MetaScoreboard(
        text_font      = read_bytes_io(path_fonts/'Party_Confetti.ttf'),
        text_font_size = 28,
        text_spacing   = 1,
        text_position  = (160,20),
        text_bgcolor   = (55,55,55)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(90,140),
            path=path_objects/'confident_student.png'
        )
    )
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    # Image sizes
    # file = [ (110,143), (168,130), (92,124),
    #          (207,155), (203,103), (166,111),
    #          (135,147), (204,114), (227,148) ]
    sizes = [ (80,104),  (100,77), (80,108),
              (100,75),  (100,51), (100,67),
              (100,109), (100,56), (160,104) ]

    for ii in range(9):

        imag_obstacle = MetaImage.from_file(size=sizes[ii],
            path=path_objects/f'book-{ii+1}.png',
        )
        obstacle = MetaObject(
            image  = imag_obstacle,
            sound  = crash_sound,
            volume = 0.9,
        )
        meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    collect_sound = read_bytes_io(path_sounds/'collect-ring.mp3')

    meta.collectibles_frequency = 1
    meta.collectibles = []

    # Image sizes
    # file = [ (197, 133), (224, 221), (227, 219), (168, 223), (202, 133) ]
    sizes = [ (100,68), (100,99), (100,96), (80,106), (100,66) ]

    for ii in range(5):

        imag_collectible = MetaImage.from_file(size=sizes[ii],
            path=path_objects/f'video_game_controller-{ii+1}.png'
        )
        collectible = MetaObject(
            image  = imag_collectible,
            score  = -100,
            sound  = collect_sound,
            volume = 0.2
        )
        meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + 2*t')
    meta.boundary = BoundaryFunctions('3', '87')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

