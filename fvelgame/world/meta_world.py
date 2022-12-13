#------------------------------------------------------------------------------#

'''This module defines the MetaWorld class.

It stores all information about the GameWorld in an intermediate state
between Pyside and PyGame being independent of both libraries. This class 
must be saved in a binary file and used to create a GameWorld.
'''

import sys
sys.path.append('..')

import pickle

# Default screen resolution
FULLHD_SIZE = (1920, 1080)

#------------------------------------------------------------------------------#

from world.functions import VelocityFunction, MarginFunctions

#------------------------------------------------------------------------------#
class MetaImage:
    '''Describes an image to be used on game.'''

    #--------------------------------------------------------------------------#
    def __init__(self, size=FULLHD_SIZE, color=(0,0,0), path=None ):
        '''Create a MetaImage.

        Height (size[1]) equal to None means to keep the image aspect ratio
        '''

        self.size       = size  # (width, height)
        self.color      = color
        self.image_path = path

#------------------------------------------------------------------------------#
class MetaObject:
    '''Describes game object.'''

    #--------------------------------------------------------------------------#
    def __init__(self, image, score=0, sound=None ):

        self.image = image
        self.score = score
        self.sound = sound

#------------------------------------------------------------------------------#
class MetaWorld:

    #--------------------------------------------------------------------------#
    def __init__( self ):
        '''Create a default MetaWorld.'''

        self.game = {}
        self.game['author'     ] = ''
        self.game['name'       ] = ''
        self.game['description'] = ''
        self.game['icon'       ] = None

        self.dynamics = {}
        self.dynamics['vertical'           ] = True  
        self.dynamics['player_speed'       ] = 4.0
        self.dynamics['obstacles_frequency'] = 3  # Average occurrences per second
        self.dynamics['treasures_frequency'] = 1
        self.dynamics['score_time_bonus'   ] = 0.001 # Points per millisecond

        self.appearance = {}
        self.appearance['background'  ] = MetaImage( color=(39,38,67) )
        self.appearance['track'       ] = MetaImage( color=(38,90,90) )
        self.appearance['ost_position'] = (100,100)
        self.appearance['ost_bgcolor' ] = ( 55, 55, 55)
        self.appearance['ost_fgcolor' ] = (255,255,255)

        imag_player   = MetaImage( (35,60), color=( 49,116,200) )
        imag_obstacle = MetaImage( (90,17), color=(200, 32, 57) )
        imag_treasure = MetaImage( (30,30), color=(240,212,117) )
    
        self.objects = {}
        self.objects['player'   ] = MetaObject( imag_player )
        self.objects['obstacles'] = MetaObject( imag_obstacle, 10 )
        self.objects['treasures'] = MetaObject( imag_treasure, 100 )

        self.ambience_sound = None

        self.velocity = VelocityFunction( 5, 0.5 )
        self.margins  = MarginFunctions( 0.3, 0.7 )

    #--------------------------------------------------------------------------#
    def save(self, path):
        '''Save itself using pickle.'''

        with open(path, 'wb') as file:
            pickle.dump(self,file)

    #--------------------------------------------------------------------------#
    def load(path):
        '''Load a pickled file and returna MetaWorld object.'''

        with open(path, 'rb') as file:
            meta = pickle.load(file)

        # Simple data validation
        meta.game['author']
        meta.dynamics['player_speed']
        meta.appearance['background']

        return meta

#------------------------------------------------------------------------------#

