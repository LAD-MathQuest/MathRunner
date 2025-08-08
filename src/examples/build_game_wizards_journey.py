#---------------------------------------------------------------------------read_bytes_io()
'''Build game Wizard's Journey

Author: Samuel Lopes
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

    print("Building Wizard's Journey")

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

    game_file_name        = "wizards_journey.game"
    meta.soft_name        = "Wizard's Journey"
    meta.soft_author      = "Samuel Lopes"
    meta.soft_description = "Fuja das criaturas malignas enquanto avança em uma floresta mágica"
    meta.soft_icon        = MetaImage.from_file(path_icons/'wizards_journey.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = True
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'music_theme_wizard.wav')
    meta.game_ambience_volume = 0.4

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1920,1080),
        path=path_backgrounds/'magical_woods.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image   = False
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

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
        MetaImage.from_file(size=(140,140),
            path=path_objects/'wizard.png'
        )
    )
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 3
    meta.obstacles = []

    obstacles = ['dragon', 'wood_spirit', 'evil_spirit']

    for ii in range(3):

        imag_obstacle = MetaImage.from_file(size=(120,140),
            path=path_objects/f'{obstacles[ii]}.png',
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

    imag_collectible = MetaImage.from_file(size=(80,100),
        path=path_objects/'grimorio.png'
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

    meta.velocity = VelocityFunction('25 + 2*t')
    meta.boundary = BoundaryFunctions('30','70')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

