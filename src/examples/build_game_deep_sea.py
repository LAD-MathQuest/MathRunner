#------------------------------------------------------------------------------#
'''Build game Deep Sea

Author: Luis D'Afonseca
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

    print('Building Deep Seas')

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

    game_file_name        = 'deep_sea.game'
    meta.soft_name        = 'Deep Sea'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = "Uma aventura em baixo d'água"
    meta.soft_icon        = read_bytes_io(path_icons/'deep_sea.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'music-1.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(
        path_backgrounds/'deep_sea_background.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image   = MetaImage(
        color=(0, 140, 255)
    )
    meta.track_scrolls = False
    meta.track_kills   = (False, True)

    meta.min_color = (19, 43, 63)
    meta.max_color = None
    meta.min_width = 3
    meta.max_width = 1

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
        text_bgcolor   = (55,55,55),
        text_fgcolor   = (255,255,255)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(120, 75),
            path=path_objects/'submarine.png'
        )
    )
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage.from_file(size=(50,54),
        path = path_objects/'mine.png',
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

    for ii in range(1,3):
        imag_collectible = MetaImage.from_file(size=(90,69),
            path=path_objects/f'diver-0{ii}.png'
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
    meta.boundary = BoundaryFunctions(
        '15.2 + 10*sen(x/80) + 5*sen(x/20)',
        '86.8'
    )

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

