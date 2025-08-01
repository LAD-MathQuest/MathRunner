#------------------------------------------------------------------------------#
'''Build game Space

Author: Daniel Cristo
'''

#------------------------------------------------------------------------------#

from pathlib import Path

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

    print('Building Space Game')

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

    game_file_name        = 'space.game'
    meta.soft_name        = 'Space'
    meta.soft_author      = "Daniel Cristo"
    meta.soft_description = 'Desvie dos Asteroides e resgate os Astronautas'
    meta.soft_icon        = read_bytes_io(path_icons/'space.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'music_healthy.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1500,1500),
        path=path_backgrounds/'space.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image = MetaImage(
        color=(0,0,255)
    )
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    # Scoreboard
    imag_score = MetaImage.from_file(size=(390,160),
        path=path_scoreboards/'space_display.png'
    )
    meta.scoreboard = MetaScoreboard(
        image          = imag_score,
        image_position = (54,67),
        text_font      = read_bytes_io(path_fonts/'Electronic_Highway_Sign.ttf'),
        text_font_size = 28,
        text_spacing   = 1.2,
        text_position  = (103,100),
        text_bgcolor   = (90,93,102),
        text_fgcolor   = (0,204,255)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(160,160),
            path=path_objects/'rocket.png'
        )
    )
    meta.player_speed = 400

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage.from_file(size=(192,192),
        path=path_objects/'asteroid.png'
    )
    obstacle = MetaObject(
        image  = imag_obstacle,
        sound  = crash_sound,
        volume = 0.9
    )
    meta.obstacles.append(obstacle)

    # Collectibles
    #--------------------------------------------------------------------------#

    collect_sound = read_bytes_io(path_sounds/'collect-ring.mp3')

    meta.collectibles_frequency = 1
    meta.collectibles = []

    astronauts = ['green', 'white', 'brown']

    for ii in range(3):

        imag_collectible = MetaImage.from_file(size=(128,128),
            path=path_objects/f'astronaut-{astronauts[ii]}.png'
        )
        collectible = MetaObject(
            image  = imag_collectible,
            score  = 100,
            sound  = collect_sound,
            volume = 0.2
        )
        meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('25 + 2*t')
    meta.boundary = BoundaryFunctions('12', '90 + 9*sin(x/100)')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#
