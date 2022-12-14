#------------------------------------------------------------------------------#

'''This script build and save an example of MetaWorld.'''

import sys
sys.path.append('../..')

from pathlib          import Path
from world.functions  import VelocityFunction, MarginFunctions
from world.meta_world import MetaWorld, MetaImage, MetaObject

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    print('Building game-01...')

    meta = MetaWorld()

    meta.game['author'     ] = "Luis D'Afonseca"
    meta.game['name'       ] = 'Corrida'
    meta.game['description'] = ''
    meta.game['icon'       ] = None

    meta.dynamics['vertical'           ] = True  
    meta.dynamics['player_speed'       ] = 4.0
    meta.dynamics['obstacles_frequency'] = 3  # Average occurrences per second
    meta.dynamics['treasures_frequency'] = 1
    meta.dynamics['score_time_bonus'   ] = 0.001 # Points per millisecond

    meta.appearance['background'  ] = MetaImage( color=(39,89,38) )
    meta.appearance['track'       ] = MetaImage( color=(42,41,34) )
    meta.appearance['ost_position'] = (100,100)
    meta.appearance['ost_bgcolor' ] = ( 55, 55, 55)
    meta.appearance['ost_fgcolor' ] = (255,255,255)

    path_resources = Path(__file__).resolve().parents[1]

    path_player   = path_resources / 'objects' / 'sport_car-1.png'
    path_obstacle = path_resources / 'objects' / 'sport_car-7.png'
    path_treasure = path_resources / 'objects' / 'precious_stone-3.png'
    path_crash    = path_resources / 'sounds'  / 'car_crash.mp3'   
    path_ambience = path_resources / 'sounds'  / 'music-1.mp3'     

    imag_player   = MetaImage( (48,108), path=path_player   )
    imag_obstacle = MetaImage( (40, 90), path=path_obstacle )
    imag_treasure = MetaImage( (46, 38), path=path_treasure )

    meta.objects['player'   ] = MetaObject( imag_player )
    meta.objects['obstacles'] = MetaObject( imag_obstacle, 10, path_crash )
    meta.objects['treasures'] = MetaObject( imag_treasure, 100 )

    meta.ambience_sound = path_ambience

    meta.velocity = VelocityFunction( 5, 0.5 )
    meta.margins  = MarginFunctions( 0.3, 0.7 )

    meta.save('game-01.pkl')

    print('Done')

#------------------------------------------------------------------------------#

