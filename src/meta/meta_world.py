#------------------------------------------------------------------------------#
'''This module defines the MetaWorld class.

It stores all information about the GameWorld in an intermediate state
between PySide and PyGame being independent of both libraries. This class
must be saved in a binary file and used to create a GameWorld.
'''

#------------------------------------------------------------------------------#

import pickle

from .velocity_function import VelocityFunction
from .boundary_function import BoundaryFunctions
from .meta_image        import MetaImage
from .meta_object       import MetaObject
from .meta_scoreboard   import MetaScoreboard

#------------------------------------------------------------------------------#
class MetaWorld:

    #--------------------------------------------------------------------------#
    def __init__( self ):
        '''Create a default MetaWorld'''

        # Software
        #----------------------------------------------------------------------#

        self.soft_name        = 'MathRunner'
        self.soft_author      = "Luis D'Afonseca"
        self.soft_description = 'Um jogo para explorar funções'
        self.soft_icon        = None

        # Game
        #----------------------------------------------------------------------#

        self.game_vertical        = True
        self.game_time_bonus      = 1     # Score points bonus per second
        self.game_ambience        = None  # Ambience sound
        self.game_ambience_volume = 1.0   # Sound volume

        # Appearance
        #----------------------------------------------------------------------#

        self.background_image   = MetaImage(color=(39,38,67))
        self.background_scrolls = False

        # If track_image if null the game will not draw the track
        self.track_image   = MetaImage(color=(38,90,90))
        self.track_scrolls = False
        self.track_kills   = (False, False)

        self.min_color = None
        self.max_color = None
        self.min_width = 1
        self.max_width = 1

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

        imag_obstacle = MetaImage((70,70), color=color)
        self.obstacles.append( MetaObject( imag_obstacle, points ))

        imag_obstacle = MetaImage((100,40), color=color)
        self.obstacles.append( MetaObject( imag_obstacle, points ))

        imag_obstacle = MetaImage((40,100), color=color)
        self.obstacles.append( MetaObject( imag_obstacle, points ))

        # Collectibles
        #----------------------------------------------------------------------#

        color  = (240,212,117)
        points = 100

        self.collectibles_frequency = 1
        self.collectibles = []

        imag_collectible = MetaImage((50,50), color=color)
        self.collectibles.append( MetaObject(imag_collectible, points))

        imag_collectible = MetaImage((30,80), color=color )
        self.collectibles.append( MetaObject(imag_collectible, points))

        # Functions
        #----------------------------------------------------------------------#

        self.velocity = VelocityFunction ('25 + 2*t')
        self.boundary = BoundaryFunctions('35', '65')

#------------------------------------------------------------------------------#
def save_meta(meta: MetaWorld, path) -> None:

    try:
        pickle.dump(meta, path)

    except TypeError:
        with open(path, 'wb') as file:
            pickle.dump(meta, file)

#------------------------------------------------------------------------------#
def load_meta(path) -> MetaWorld:

    try:
        meta = pickle.load(path)

    except TypeError:
        with open(path, 'rb') as file:
            meta = pickle.load(file)

    return meta

#------------------------------------------------------------------------------#

