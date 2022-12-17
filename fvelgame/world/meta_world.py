#------------------------------------------------------------------------------#

'''This module defines the MetaWorld class.

It stores all information about the GameWorld in an intermediate state
between Pyside and PyGame being independent of both libraries. This class 
must be saved in a binary file and used to create a GameWorld.
'''

#------------------------------------------------------------------------------#

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import pickle

# Default screen resolution
SCREEN_SIZE = (1920, 1080)

#------------------------------------------------------------------------------#

from world.functions import VelocityFunction, MarginFunctions

#------------------------------------------------------------------------------#
class MetaImage:
    '''Describes an image to be used on game.'''

    #--------------------------------------------------------------------------#
    def __init__(self, size=SCREEN_SIZE, color=(0,0,0), path=None ):
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

        # Game general information
        #----------------------------------------------------------------------#

        self.game = {}
        self.game['author'     ] = ''
        self.game['name'       ] = ''
        self.game['description'] = ''
        self.game['icon'       ] = None

        # Game dynamics
        #----------------------------------------------------------------------#

        self.dynamics = {}
        self.dynamics['vertical'              ] = True  
        self.dynamics['player_speed'          ] = 4 # Pixels per frame
        self.dynamics['obstacles_frequency'   ] = 3 # Average occurrences per second
        self.dynamics['collectibles_frequency'] = 1
        self.dynamics['score_time_bonus'      ] = 1 # Points per second

        # Game appearance
        #----------------------------------------------------------------------#

        self.appearance = {}
        self.appearance['background'  ] = MetaImage( color=(39,38,67) )
        self.appearance['track'       ] = MetaImage( color=(38,90,90) )
        self.appearance['ost_position'] = (100,100)
        self.appearance['ost_bgcolor' ] = ( 55, 55, 55)
        self.appearance['ost_fgcolor' ] = (255,255,255)

        # Objects
        #----------------------------------------------------------------------#

        self.objects = {}

        # Player
        imag_player = MetaImage( (35,60), color=( 49,116,200) )
        self.objects['player'] = MetaObject(imag_player)

        # Obstacles
        self.objects['obstacles'] = []

        imag_obstacle = MetaImage( (70,70), color=(200, 32, 57) )
        self.objects['obstacles'].append( MetaObject( imag_obstacle, 10 ) )
 
        imag_obstacle = MetaImage( (100,40), color=(200, 32, 57) )
        self.objects['obstacles'].append( MetaObject( imag_obstacle, 10 ) )
 
        imag_obstacle = MetaImage( (40,100), color=(200, 32, 57) )
        self.objects['obstacles'].append( MetaObject( imag_obstacle, 10 ) )

        # Collectibles
        self.objects['collectibles'] = []

        imag_collectible = MetaImage( (50,50), color=(240,212,117) )
        self.objects['collectibles'].append( MetaObject( imag_collectible, 100 ) )

        imag_collectible = MetaImage( (30,80), color=(240,212,117) )
        self.objects['collectibles'].append( MetaObject( imag_collectible, 100 ) )


        # Ambience sound and functions
        #----------------------------------------------------------------------#

        self.ambience_sound = None

        self.velocity = VelocityFunction(5, 0.5)
        self.margins  = MarginFunctions(0.35, 0.65)

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

