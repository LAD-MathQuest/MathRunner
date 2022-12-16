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
    meta.dynamics['player_speed'          ] =  8 # Pixels per frame
    meta.dynamics['obstacles_frequency'   ] =  3 # Average occurrences per second
    meta.dynamics['collectibles_frequency'] =  1
    meta.dynamics['score_time_bonus'      ] = -2 # Points per second

    # Game appearance
    #--------------------------------------------------------------------------#
    meta.appearance['background'  ] = MetaImage( color=( 55, 55, 55) )
    meta.appearance['track'       ] = MetaImage( color=(102,153,153) )
    meta.appearance['ost_position'] = (200,10)
    meta.appearance['ost_bgcolor' ] = ( 55, 55, 55)
    meta.appearance['ost_fgcolor' ] = (255,255,255)

    # Objects
    #--------------------------------------------------------------------------#

    path_resources = Path(__file__).parents[1] / 'resources'
    path_objects   = path_resources / 'objects' 
    path_crash     = path_resources / 'sounds' / 'car_crash.mp3'   
    path_crash = None

    # Player
    path_player = path_objects / 'confident_student.png'
    imag_player = MetaImage((90,140), path=path_player)
    meta.objects['player'] = MetaObject(imag_player)

    # Obstacles
    meta.objects['obstacles'] = []

    # Image sizes
    # file = [ (110,143), (168,130), (92,124),  (207,155), (203,103), 
    #          (166,111), (135,147), (204,114), (227,148) ]
    sizes = [ (80,104), (100,77),  (80,108), (100,75), (100,51),
              (100,67),  (100,109), (100,56),  (160,104) ]

    for ii in range(9):
        path_obstacle = path_objects / f'book-{ii+1}.png'
        imag_obstacle = MetaImage(sizes[ii], path=path_obstacle)
        meta.objects['obstacles'].append(MetaObject(imag_obstacle, -10))

    # Collectibles
    meta.objects['collectibles'] = []

    # Image sizes
    # file = [ (197, 133), (224, 221), (227, 219), (168, 223), (202, 133) ]
    sizes = [ (100,68), (100,99), (100,96), (100,133), (100,66) ]

    for ii in range(5):
        path_collectible = path_objects / f'video_game_controller-{ii+1}.png'
        imag_collectible = MetaImage(sizes[ii], path=path_collectible)
        meta.objects['collectibles'].append(MetaObject(imag_collectible, -100))

    # Ambience sound and functions
    #--------------------------------------------------------------------------#

    path_ambience = path_resources / 'sounds' / 'music-1.mp3'     
    path_ambience = None

    meta.ambience_sound = path_ambience

    meta.velocity = VelocityFunction( 8, 0.3 )
    meta.margins  = MarginFunctions(0.12, 0.9 )

    path = path_resources / 'games' / 'student.game'

    print(F'Writing: {path}')

    meta.save(path)

#------------------------------------------------------------------------------#

