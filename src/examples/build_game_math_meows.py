#------------------------------------------------------------------------------#
'''Build game Maths & Meows

Author: Nandnn
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

    print('Building Math Meows')

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

    game_file_name        = 'math_meows.game'
    meta.soft_name        = 'Maths & Meows'
    meta.soft_author      = "Nandnn"
    meta.soft_description = "Help the math teacher save the kittens, watch out for the cars!"
    meta.soft_icon        = read_bytes_io(path_icons/'math_meows.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'music_theme_16bits.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(2130,1231),
        path=path_backgrounds/'campus_background.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image   = False
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    meta.min_color = None
    meta.max_color = None
    meta.min_width = 3
    meta.max_width = 3

    # Scoreboard
    imag_score = MetaImage(size=(230,100),
        color=(55,55,55)
    )
    meta.scoreboard = MetaScoreboard(
        image          = imag_score,
        image_position = (153,13),
        text_font      = read_bytes_io(path_fonts/'Party_Confetti.ttf'),
        text_font_size = 28,
        text_spacing   = 1,
        text_position  = (160,20),
        text_bgcolor   = (55,55,55)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(170,130),
            path=path_objects/'teacher.png'
        )
    )
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    cars  = ['blue', 'red', 'green']
    sizes = [(115,60), (115,65), (112,63)]

    for ii in range(3):

        imag_obstacle = MetaImage.from_file(size=sizes[ii],
            path=path_objects/f'car_{cars[ii]}.png'
        )
        obstacle = MetaObject(
            image  = imag_obstacle,
            sound  = crash_sound,
            volume = 0.9
        )
        meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    meta.collectibles_frequency = 1
    meta.collectibles = []

    for ii in range(1,3):

        imag_collectible = MetaImage.from_file(size=(80,50),
            path=path_objects/f'cat-{ii}.png',
        )
        collectible = MetaObject(
            image  = imag_collectible,
            score  = 100,
            sound  = read_bytes_io(path_sounds/f'meow_0{ii}.mp3'),
            volume = 0.4
        )
        meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + t')
    meta.boundary = BoundaryFunctions('1', '75')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

