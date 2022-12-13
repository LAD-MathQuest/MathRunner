#------------------------------------------------------------------------------#

'''This module defines the MetaWorld class.

It stores all information about the GameWorld in an intermediate state
between Pyside and PyGame being independent of both libraries. This class 
must be saved in a binary file and used to create a GameWorld.
'''

# Default screen resolution
FULLHD_SIZE = (1920, 1080)

#------------------------------------------------------------------------------#

from world.functions import VelocityFunction, MarginFunctions

#------------------------------------------------------------------------------#
class MetaImage:
    '''Describes an image to be used on game.'''

    #--------------------------------------------------------------------------#
    def __init__(self, size=FULLHD_SIZE, color=(0,0,0) ):

        self.size  = size  # (width, height)
        self.color = color
        self.image = None

#------------------------------------------------------------------------------#
class MetaWorld:

    #--------------------------------------------------------------------------#
    def __init__( self, path=None ):

        #### if path:
        ####     load(path)
        ####     return

        self.game = {}
        self.game['author'     ] = ''
        self.game['name'       ] = ''
        self.game['icon'       ] = None
        self.game['description'] = ''

        self.dynamics = {}
        self.dynamics['vertical'           ] = True  
        self.dynamics['player_speed'       ] = 4.0
        self.dynamics['obstacles_frequency'] = 3  # Average occurrences per second
        self.dynamics['treasures_frequency'] = 1
        self.dynamics['score_time_bonus'   ] = 0.001 # Points per millisecond
        self.dynamics['score_dodge'        ] = 10
        self.dynamics['score_treasure'     ] = 100

        self.appearance = {}
        self.appearance['player'      ] = MetaImage( (35,60), ( 49,116,200) )
        self.appearance['obstacle'    ] = MetaImage( (90,17), (200, 32, 57) )
        self.appearance['treasure'    ] = MetaImage( (30,30), (240,212,117) )
        self.appearance['background'  ] = MetaImage( color=(39,38,67) )
        self.appearance['track'       ] = MetaImage( color=(38,90,90) )
        self.appearance['ost_position'] = (100,100)
        self.appearance['ost_bgcolor' ] = (55,55,55)
        self.appearance['ost_fgcolor' ] = (255,255,255)

        self.sound = {}
        self.sound['music'    ] = None
        self.sound['collision'] = None
        self.sound['treasure' ] = None

        self.velocity = VelocityFunction( 5, 0.5 )
        self.margins  = MarginFunctions( 0.3, 0.7 )

    #------------------------------------------------------------------------------#
    def save(self, filename):
        pass
    
    #------------------------------------------------------------------------------#
    def load(self, filename):
        pass

#------------------------------------------------------------------------------#

