#------------------------------------------------------------------------------#

'''This script builds a Game example.

Author: Luis D'Afonseca
Name:   Racing

Description
Simple racing game with treasures and obstacles.
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from world.functions  import VelocityFunction, MarginFunctions
from world.meta_world import MetaWorld, MetaImage, MetaObject

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game 01: Racing...')

    meta = MetaWorld()

    # Game general information
    #--------------------------------------------------------------------------#
    meta.game['author'     ] = "Luis D'Afonseca"
    meta.game['name'       ] = 'Racing'
    meta.game['description'] = 'Simple racing game with treasures and obstacles'
    meta.game['icon'       ] = None

    # Game dynamics
    #--------------------------------------------------------------------------#

    meta.dynamics['vertical'              ] = True  
    meta.dynamics['player_speed'          ] = 4 # Pixels per frame
    meta.dynamics['obstacles_frequency'   ] = 3 # Average occurrences per second
    meta.dynamics['collectibles_frequency'] = 1
    meta.dynamics['score_time_bonus'      ] = 1 # Points per second

    # Game appearance
    #--------------------------------------------------------------------------#
    meta.appearance['background'  ] = MetaImage( color=(39,89,38) )
    meta.appearance['track'       ] = MetaImage( color=(42,41,34) )
    meta.appearance['ost_position'] = (100,100)
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

    for ii in range(2,10):
        path_obstacle = path_objects / f'sport_car-{ii}.png'
        imag_obstacle = MetaImage((40,90), path=path_obstacle)
        meta.objects['obstacles'].append(MetaObject( imag_obstacle, 10, path_crash ))

    # Collectibles
    meta.objects['collectibles'] = []

    for ii in range(1,5):
        path_collectible = path_objects / f'precious_stone-{ii}.png'
        imag_collectible = MetaImage((46,38), path=path_collectible)
        meta.objects['collectibles'].append(MetaObject(imag_collectible, 100))

    # Ambience sound and functions
    #--------------------------------------------------------------------------#

    path_ambience = path_resources / 'sounds' / 'music-1.mp3'     
    meta.ambience_sound = path_ambience

    meta.velocity = VelocityFunction( 5, 0.5 )
    meta.margins  = MarginFunctions( 0.35, 0.65 )

    path = path_resources / 'games' / 'racing.game'

    print(F'Writing: {path}')

    meta.save(path)

#------------------------------------------------------------------------------#

