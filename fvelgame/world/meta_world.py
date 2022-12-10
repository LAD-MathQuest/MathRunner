#------------------------------------------------------------------------------#

'''This module defines the MetaWorld class.

It stores all information about the GameWorld in an intermediate state
between Pyside and PyGame being independent of both libraries. This class 
must be saved in a binary file and used to create a GameWorld.

All position and length measurements are proportional to screen size.

Width  is measured in thousandths of the screen width  [mw]
Height is measured in thousandths of the screen height [mh]

In a FullHD (1920 x 1080 pixels) screen
   1 mw = 1.920 pixels
   1 mh = 1.080 pixels

Velocity is measured in mw (or mh) per millisecond. A moving object with 
velocity of 1 mh/ms go across the screen top bottom in a second.
'''

#------------------------------------------------------------------------------#
class MetaImage:
    '''Describes an image to be used on game.

    The image has a size proportional to the screen.
    It can be an actual image file or color filled rectangle.
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, size = (1000,1000), color=(0,0,0) ):

        self.size  = size  # (width, height)
        self.color = color
        self.image = None

#------------------------------------------------------------------------------#
class SpeedFunction:

    #--------------------------------------------------------------------------#
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #--------------------------------------------------------------------------#
    def eval(self, time):
        return self.a + time * self.b

#------------------------------------------------------------------------------#
class MarginFunctions:

    #--------------------------------------------------------------------------#
    def __init__(self, min_, max_):
        self.const_min = min_
        self.const_max = max_

    #--------------------------------------------------------------------------#
    def eval(self, time):
        return ( self.const_min, self.const_max )

#------------------------------------------------------------------------------#
class MetaWorld:

    #--------------------------------------------------------------------------#
    def __init__(self):

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
        self.appearance['player'      ] = MetaImage( (18,50), (49,116,200) )
        self.appearance['obstacle'    ] = MetaImage( (45,30), (200,32,57)  )
        self.appearance['treasure'    ] = MetaImage( (15,50), (240,212,117))
        self.appearance['background'  ] = MetaImage( color=(39,38,67) )
        self.appearance['track'       ] = MetaImage( color=(38,90,90) )
        self.appearance['ost_position'] = (100,100)
        self.appearance['ost_bgcolor' ] = (55,55,55)
        self.appearance['ost_fgcolor' ] = (255,255,255)

        self.sound = {}
        self.sound['music'    ] = None
        self.sound['collision'] = None
        self.sound['treasure' ] = None

        self.speed   = SpeedFunction  ( 5, 0.0005 )
        self.margins = MarginFunctions( 350, 650  )

#------------------------------------------------------------------------------#
def save_meta_world(meta_world, file_name):
    pass

#------------------------------------------------------------------------------#
def load_meta_world(file_name):
    return MetaWorld()

#------------------------------------------------------------------------------#

