#------------------------------------------------------------------------------#
'''Build game Racing

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

    print('Building Racing')

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

    game_file_name        = 'racing.game'
    meta.soft_name        = 'Racing'
    meta.soft_author      = "Luis D'Afonseca"
    meta.soft_description = 'Um jogo de corrida onde o jogador deve evitar os obstáculos e coletar as joias'
    meta.soft_icon        = MetaImage.from_file(path_icons/'racing.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 1
    meta.game_ambience   = read_bytes_io(path_sounds/'music-1.mp3')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1920,6000),
        path=path_backgrounds/'racing_background.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image = MetaImage.from_file(size=(100,100),
        path=path_backgrounds/'racing_track.png',
    )
    meta.track_scrolls = True
    meta.track_kills   = (False, False)

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
        MetaImage.from_file(size=(48,108),
            path=path_objects/'sport_car-1.png',
        )
    )
    meta.player_speed = 400

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    for ii in range(2, 10):

        imag_obstacle = MetaImage.from_file(size=(40,90),
            path=path_objects/f'sport_car-{ii}.png',
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

    for ii in range(1,5):

        imag_collectible = MetaImage.from_file(size=(46,38),
            path=path_objects/f'precious_stone-{ii}.png'
        )
        collectible = MetaObject(
            image  = imag_collectible,
            score  = 100,
            sound  = collect_sound,
            volume = 0.2
        )
        meta.collectibles.append(collectible)

    # Oil spill
    collect_sound = read_bytes_io(path_sounds/'car_drift.mp3')

    # File image size [312, 344]
    imag_collectible = MetaImage.from_file(size=(100,110),
        path=path_objects/'oil_spill.png',
    )
    collectible = MetaObject(
        image  = imag_collectible,
        score  = -200,
        sound  = collect_sound,
        volume = 0.8
    )
    meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction('30 + 2*t')
    meta.boundary = BoundaryFunctions(
      '31 + 22*min(0.3, max(0, cos(x / 170)))',
      '68 - 22*min(0.3, max(0, cos(x / 110)))'
    )

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

