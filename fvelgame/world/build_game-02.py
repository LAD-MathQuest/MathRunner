#------------------------------------------------------------------------------#

'''This script builds a Game example.

Author: Luis D'Afonseca
Name:   Student

Description
A student runs from studying and seeks only playing video games.
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, MarginFunctions
from world.meta_world import MetaWorld, MetaImage, MetaObject

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game 02: Student...')

    meta = MetaWorld()

    # Game general information
    #--------------------------------------------------------------------------#
    meta.game['author'     ] = "Luis D'Afonseca"
    meta.game['name'       ] = 'Student'
    meta.game['description'] = 'A student runs from studying and seeks only playing video games.'
    meta.game['icon'       ] = None

    # Game dynamics
    #--------------------------------------------------------------------------#

    meta.dynamics['vertical'              ] = False
    meta.dynamics['player_speed'          ] = 4.0
    meta.dynamics['obstacles_frequency'   ] = 3  # Average occurrences per second
    meta.dynamics['collectibles_frequency'] = 1
    meta.dynamics['score_time_bonus'      ] = 0.001 # Points per millisecond

    # Game appearance
    #--------------------------------------------------------------------------#
    meta.appearance['background'  ] = MetaImage( color=( 51,  51,  51) )
    meta.appearance['track'       ] = MetaImage( color=(255, 249, 243) )
    meta.appearance['ost_position'] = (1600,10)
    meta.appearance['ost_bgcolor' ] = ( 55, 55, 55)
    meta.appearance['ost_fgcolor' ] = (255,255,255)

    # Objects
    #--------------------------------------------------------------------------#

    path_resources = Path(__file__).parents[1] / 'resources'
    path_objects   = path_resources / 'objects' 
    path_crash     = path_resources / 'sounds' / 'car_crash.mp3'   

    # Player
    path_player = path_objects / 'sport_car-1.png'
    imag_player = MetaImage((48,108), path=path_player)
    meta.objects['player'] = MetaObject(imag_player)

    # Obstacles
    meta.objects['obstacles'] = []

    imag_obstacle = MetaImage( (100,100), color=(200, 32, 57) )
    meta.objects['obstacles'].append(MetaObject( imag_obstacle, 10, path_crash ))

    # Collectibles
    meta.objects['collectibles'] = []

    # File resolution
    # sizes = [ (197, 133),
    #           (224, 221),
    #           (227, 219),
    #           (168, 223),
    #           (202, 133) ]

    sizes = [ (100,  68),
              (100,  99),
              (100,  96),
              (100, 133),
              (100,  66) ]

    for ii in range(5):
        path_collectible = path_objects / f'video_game_controller-{ii+1}.png'
        imag_collectible = MetaImage(sizes[ii], path=path_collectible)
        meta.objects['collectibles'].append(MetaObject(imag_collectible, 100))

    # Ambience sound and functions
    #--------------------------------------------------------------------------#

    path_ambience = path_resources / 'sounds' / 'music-1.mp3'     
    meta.ambience_sound = path_ambience

    meta.velocity = VelocityFunction( 5, 0.5 )
    meta.margins  = MarginFunctions(0.1, 0.9 )

    path = path_resources / 'games' / 'student.pkl'

    print(F'Writing: {path}')

    meta.save(path)

#------------------------------------------------------------------------------#

