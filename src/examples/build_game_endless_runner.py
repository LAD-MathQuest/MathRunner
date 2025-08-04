#------------------------------------------------------------------------------#
'''Build game Endless Runner

Author: Mariana Matias do Nascimento
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

    print('Building Endless Runner')

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

    game_file_name        = 'endless_runner.game'
    meta.soft_name        = 'Endless Runner'
    meta.soft_author      = 'Mariana Matias do Nascimento'
    meta.soft_description = 'A racing game where the character runs an infinite amount of time dodging obstacles'
    meta.soft_icon        = MetaImage.from_file(path_icons/'endless_runner.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 1
    meta.game_ambience   = read_bytes_io(path_sounds/'run-away-runner.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1920,6000),
        path = path_backgrounds/'space.jpg'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image = MetaImage(size=(100,100),
        color=(0,0,0)
    )
    meta.track_scrolls = False
    meta.track_kills   = (True, True)

    meta.min_color = (0, 0, 0)
    meta.max_color = (0, 0, 0)
    meta.min_width = 3
    meta.max_width = 3

    # Scoreboard
    imag_score = MetaImage.from_file(size=(390,160),
        path=path_scoreboards/'frame_neon.png'
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
        MetaImage.from_file(size = (48,108),
            path = path_objects/'plane_1.png'
        )
    )
    meta.player_speed = 400

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'explosion.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    imag_obstacle = MetaImage.from_file(size = (80,80),
        path = path_objects/'enemy_spaceship.png'
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

    imag_collectible = MetaImage.from_file(size = (46,38),
        path = path_objects/'ruby.png'
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
    meta.boundary = BoundaryFunctions('10', '90')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#
