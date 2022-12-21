#------------------------------------------------------------------------------#

'''This module defines the MetaWorld class.

It stores all information about the GameWorld in an intermediate state
between Pyside and PyGame being independent of both libraries. This class 
must be saved in a binary file and used to create a GameWorld.
'''

#------------------------------------------------------------------------------#

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
    '''Describes game objects.'''

    #--------------------------------------------------------------------------#
    def __init__(self, image, score=0, sound=None ):

        self.image = image
        self.score = score
        self.sound = sound

#------------------------------------------------------------------------------#
class MetaScoreboard:
    '''Describes the game scoreboard.'''

    #--------------------------------------------------------------------------#
    def __init__(self, 
                 image          = MetaImage((140,140), (200,70,80)), 
                 image_position = (80,80), 
                 text_rect      = (100,100,100,100),
                 text_bgcolor   = ( 55, 55, 55),
                 text_fgcolor   = (255,255,255)):

        self.image          = image
        self.image_position = image_position

        self.text_rect    = text_rect
        self.text_bgcolor = text_bgcolor
        self.text_fgcolor = text_fgcolor

#------------------------------------------------------------------------------#
class MetaWorld:

    #--------------------------------------------------------------------------#
    def __init__( self ):
        '''Create a default MetaWorld.'''

        # Software
        #----------------------------------------------------------------------#

        self.soft_name        = 'FVelGame'
        self.soft_author      = "Luis D'Afonseca"
        self.soft_description = 'Um jogo para explorar funções'
        self.soft_icon        = None

        # Game 
        #----------------------------------------------------------------------#

        self.game_vertical   = True   
        self.game_time_bonus = 1     # Score points bonnus per second
        self.game_ambience   = None  # Ambience sound

        # Appearance
        #----------------------------------------------------------------------#

        self.background_image   = MetaImage( color=(39,38,67) )
        self.background_scrolls = False
        
        # If track_image if null the game will not draw the track
        self.track_image           = MetaImage( color=(38,90,90) )
        self.track_boundaries_kill = False

        self.scoreboard = MetaScoreboard()

        # Player
        #----------------------------------------------------------------------#

        self.player       = MetaObject(MetaImage((35,60), color=(25,25,25)))
        self.player_speed = 400 # Pixels per frame

        # Obstacles
        #----------------------------------------------------------------------#

        color  = (200,32,57)
        points = 10

        self.obstacles_frequency = 4 # Average occurrences per second
        self.obstacles = []

        imag_obstacle = MetaImage( (70,70), color=color )
        self.obstacles.append( MetaObject( imag_obstacle, points ) )
 
        imag_obstacle = MetaImage( (100,40), color=color )
        self.obstacles.append( MetaObject( imag_obstacle, points ) )
 
        imag_obstacle = MetaImage( (40,100), color=color )
        self.obstacles.append( MetaObject( imag_obstacle, points ) )

        # Collectibles
        #----------------------------------------------------------------------#

        color  = (240,212,117)
        points = 100

        self.collectibles_frequency = 1
        self.collectibles = []

        imag_collectible = MetaImage( (50,50), color=color )
        self.collectibles.append( MetaObject( imag_collectible, points ) )

        imag_collectible = MetaImage( (30,80), color=color )
        self.collectibles.append( MetaObject( imag_collectible, points ) )

        # Functions
        #----------------------------------------------------------------------#

        self.velocity = VelocityFunction(0.50, 0.01)
        self.margins  = MarginFunctions (0.35, 0.65)

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

        # TODO Simple data validation

        return meta

#------------------------------------------------------------------------------#

