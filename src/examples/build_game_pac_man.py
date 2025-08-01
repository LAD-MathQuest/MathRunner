#------------------------------------------------------------------------------#
'''Build game Pac Man

Author: Emanuelle Lima
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

    print('Building Pac Man')

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

    game_file_name        = "pac_man.game"
    meta.soft_name        = "Pac Man"
    meta.soft_author      = "Emanuelle Lima"
    meta.soft_description = "Ajude o Pac Man a fugir dos fantasmas e a comer cerejas"
    meta.soft_icon        = read_bytes_io(path_icons/'pac_man.png')

    # Game
    #--------------------------------------------------------------------------#

    meta.game_vertical   = False
    meta.game_time_bonus = 10
    meta.game_ambience   = read_bytes_io(path_sounds/'pacman.mp3')
    meta.game_ambience_volume = 0.7

    # Appearance
    #--------------------------------------------------------------------------#

    # Background
    meta.background_image = MetaImage.from_file(size=(1920,1080),
        path=path_backgrounds/'pistapacman.png'
    )
    meta.background_scrolls = True

    # Track
    meta.track_image   = False
    meta.track_scrolls = False
    meta.track_kills   = (False, False)

    # Scoreboard
    imag_score = MetaImage(size=(280,100),
        color=(59,29,139)
    )
    meta.scoreboard = MetaScoreboard(
        image          = imag_score,
        image_position = (153,13),
        text_font      = read_bytes_io(path_fonts/'Arcade.ttf'),
        text_font_size = 15,
        text_spacing   = 1.3,
        text_position  = (160,20),
        text_bgcolor   = (59,29,139)
    )

    # Player
    #--------------------------------------------------------------------------#

    meta.player = MetaObject(
        MetaImage.from_file(size=(130,130),
            path=path_objects/'pacman.png'
        )
    )
    meta.player_speed = 800

    # Obstacles
    #--------------------------------------------------------------------------#

    crash_sound = read_bytes_io(path_sounds/'car_crash.mp3')

    meta.obstacles_frequency = 2
    meta.obstacles = []

    ghosts = ['vermelho', 'verde', 'azul']

    for ii in range(3):

        imag_obstacle = MetaImage.from_file(size=(130,130),
            path=path_objects/f'fantasma{ghosts[ii]}.png',
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

    imag_collectible = MetaImage.from_file(size=(120,120),
        path=path_objects/'cereja.png'
    )
    collectible = MetaObject(
        image  = imag_collectible,
        score  = 100,
        sound  = read_bytes_io(path_sounds/'pacmaneat.mp3'),
        volume = 0.5
    )
    meta.collectibles.append(collectible)

    imag_collectible = MetaImage.from_file(size=(110,110),
        path=path_objects/'cerejaveneno.png'
    )
    collectible = MetaObject(
        image  = imag_collectible,
        score  = 100,
        sound  = read_bytes_io(path_sounds/'pacmanpain.mp3'),
        volume = 0.5
    )
    meta.collectibles.append(collectible)

    # Functions
    #--------------------------------------------------------------------------#

    meta.velocity = VelocityFunction ('20 + t')
    meta.boundary = BoundaryFunctions('10', '90')

    # Saving
    #--------------------------------------------------------------------------#

    save_meta(meta, path_games/game_file_name)

#------------------------------------------------------------------------------#

