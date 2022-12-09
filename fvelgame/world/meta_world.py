#------------------------------------------------------------------------------#

'''
This module defines the MetaWorld class

It stores all information about the GameWorld in a intermediate state between Pyside and PyGame
It is independent of both these libraries
This class will be saved in a binary file and used to create a GameWorld
'''

# All position and length measurements are proportional to screen size
#
# Width  is measured in thousandth's of the screen width  [mw]
# Height is measured in thousandth's of the screen height [mh]
# 
# In a FullHD (1920 x 1080 pixels) screen
#    1 mw = 1.920 pixels
#    1 mh = 1.080 pixels

# Velocity is measured in mw (or mh) per millisecond
# A movel with velocity of 1 mh/ms go across the screen top bottom in a second

#------------------------------------------------------------------------------#
class MetaSprite:

    #--------------------------------------------------------------------------#
    def __init__( self, size, color ):

        self.size  = (100.0, 100.0)   # (width, height)
        self.color = (255, 255, 255)  # (R,G,B)
        self.image = None

#------------------------------------------------------------------------------#
class MetaOnScreenText:

    #--------------------------------------------------------------------------#
    def __init__(self):

        self.area    = (100.0, 100.0, 370.0, 70.0 ) # (left, top, width, height) 
        self.bgcolor = ( 55, 55, 55)
        self.fgcolor = (255,255,255)

#------------------------------------------------------------------------------#
class MetaSpeedFunction:

    #--------------------------------------------------------------------------#
    def __init__(self):
        self.a = 5.0
        self.b = 0.0003

    #--------------------------------------------------------------------------#
    def eval( self, time ):
        return self.a + time * self.b

#------------------------------------------------------------------------------#
class MetaTrackMarginFunctions:

    #--------------------------------------------------------------------------#
    def __init__(self):
        self.left_const  = 300
        self.right_const = 700

    #--------------------------------------------------------------------------#
    def eval_left( self, t ):
        return self.left_const

    #--------------------------------------------------------------------------#
    def eval_rigth( self, t ):
        return self.rigth_const

#------------------------------------------------------------------------------#
class MetaBackground:

    #--------------------------------------------------------------------------#
    def __init__(self):

        # Background information
        self.background_color = (0,0,0)
        self.background_image = None

        self.track_min = 450             # "left"
        self.track_max = 550             # "right"
        self.track_pos_player    = 0.2   # "bottom"
        self.track_pos_scrollers = 0.1   # "top"

#------------------------------------------------------------------------------#
class MetaWorld:

    #--------------------------------------------------------------------------#
    def __init__(self):

        # Author and App information
        self.author_name      = ''
        self.game_name        = ''
        self.game_icon        = None
        self.game_description = ''

        # Game dynamics information
        self.vertical = True # False means horizontal scrolling

        # Sound information
        self.sound_background = None
        self.sound_colision   = None
        self.sound_treasure   = None

        # Score computing
        self.score_time_bonus = 0.001 # Points per millisecond
        self.score_dodge      =  10
        self.score_treasure   = 100

        # On screen text
        self.ost = MetaOnScreenText()

        # Scrolling speed function
        self.speed = MetaSpeedFunction()

        # Player moving speed
        self.player_speed = 4.0

        # Average interval in milliseconds
        self.obstacles_average =  700
        self.treasures_average = 3777

        # Sprite parameters
        self.sprite_player   = MetaSprite( (15, 5), ( 17,  57,  69) )
        self.sprite_obstacle = MetaSprite( (40, 2), (141,  29, 117) )
        self.sprite_treasure = MetaSprite( (20, 6), (255, 222,  89) )

        # Background and track
        self.background = MetaBackground()

#------------------------------------------------------------------------------#
def save_meta_world( meta_world, file_name ):
    print(f'Saving {meta_world} to {file_name} ')

#------------------------------------------------------------------------------#
def load_meta_world( file_name ):
    print(f'Loading MetaWorld from {file_name} ')
    return MetaWorld()

#------------------------------------------------------------------------------#

