#------------------------------------------------------------------------------#
'''This module defines the GameWorld class.

The GameWorld class stores all parameters defined by the game creator
using pygame structures to be used directly by de Engine.
An instance of GameWoclass is created from an instance of MetaWorld.

Here the lengths are measured in pixels.
'''

# TODO take scrolling direction in account

#------------------------------------------------------------------------------#

import pygame

from world.meta_world import MetaWorld

#------------------------------------------------------------------------------#
class SF:
    '''Scale Factor: Unit convertion tool.

    Auxiliary class to compute and store the scale factor from 
    thousandths to pixels.
    '''

    #--------------------------------------------------------------------------#
    def init(size):
        '''Create a ScaleFactor instance from the screen size em pixels.'''

        SF.mw = size[0] / 1000
        SF.mh = size[1] / 1000

    #--------------------------------------------------------------------------#
    def width_to_pixels(width):
        '''Converts widths from thousandths of the screen to pixels'''

        try: 
            return [ int(w*SF.mw) for w in width ]
        except:
            return int(width * SF.mw)

    #--------------------------------------------------------------------------#
    def height_to_pixels(height):
        '''Converts heights from thousandths of the screen to pixels'''
    
        try: 
            return [ int(h*SF.mh) for h in height ]
        except:
            return int(height * SF.mh)

    #--------------------------------------------------------------------------#
    def size_to_pixels(size):
        '''Converts a size from thousandths of the screen to pixels'''
    
        return ( int(size[0] * SF.mw), int(size[1] * SF.mh) )

    #--------------------------------------------------------------------------#
    def rect_to_pixels(rect):
        '''Converts a Rect from thousandths of the screen to pixels'''
    
        rr = pygame.Rect()
    
        rr.x = int(rect.x * SF.mw)
        rr.w = int(rect.w * SF.mw)
        rr.y = int(rect.y * SF.mh)
        rr.h = int(rect.h * SF.mh)
    
        return rr

#------------------------------------------------------------------------------#
def surface_from_meta_image(meta, size):

    surf = pygame.Surface(size)
    surf.fill(meta.color)

    return surf

#------------------------------------------------------------------------------#
class GameObjectParam:
    '''Stores all parameters needed to create game objects (sprite).'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create game object parameters from a meta object.'''

        self.size  = SF.size_to_pixels(meta.size)
        self.image = surface_from_meta_image(meta, self.size)

#------------------------------------------------------------------------------#
class GameWorld:
    '''Stores all parameters needed by the game Engine.'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create a GameWorld from MetaWorld.

        The GameWorld created will be fully configured only after the
        execution of set_dimensions function.
        '''

        self.meta = meta

        self.vertical = meta.dynamics['vertical']

        self.obstacles_frequency = meta.dynamics['obstacles_frequency']
        self.treasures_frequency = meta.dynamics['treasures_frequency']

        self.obstacles_min_time = 100
        self.obstacles_max_time = 1000
        self.treasures_min_time = 500
        self.treasures_max_time = 4000

        self.score_time_bonus = meta.dynamics['score_time_bonus']
        self.score_dodge      = meta.dynamics['score_dodge'     ]
        self.score_treasure   = meta.dynamics['score_treasure'  ]

        self.ost_bgcolor = meta.appearance['ost_bgcolor']
        self.ost_fgcolor = meta.appearance['ost_fgcolor']

        self.sound_music     = meta.sound['music'    ]
        self.sound_collision = meta.sound['collision']
        self.sound_treasure  = meta.sound['treasure' ]

    #--------------------------------------------------------------------------#
    def set_dimensions(self, width, height):
        '''Configure the GameWorld to actual screen size.

        Convert all measurements from thousandths of screen to pixels
        and complete the GameWorld configuration.
        '''

        # Screen size in pixels
        self.size = (width, height)

        SF.init(self.size)

        self.player_speed = SF.height_to_pixels( self.meta.dynamics['player_speed'] )
        
        self.param_player   = GameObjectParam( self.meta.appearance['player'  ] )
        self.param_obstacle = GameObjectParam( self.meta.appearance['obstacle'] )
        self.param_treasure = GameObjectParam( self.meta.appearance['treasure'] )

        # TODO Compute ost size properly
        self.ost_area = pygame.Rect( self.meta.appearance['ost_position'], (100,100) )
        
        # Background and track images
        self.background = surface_from_meta_image( self.meta.appearance['background'], self.size )
        # self.track    = surface_from_meta_image( self.meta.appearance['track'     ], self.size )

        # Geting constant track rectangle
        margins    = SF.width_to_pixels(self.meta.margins.eval(0))
        self.track = pygame.Rect(margins[0],0,margins[1]-margins[0],height)

        # Old method of drawing track on background
        color = self.meta.appearance['track'].color 
        pygame.draw.rect( self.background, color, self.track )

    #--------------------------------------------------------------------------#
    def eval_speed(self, time):
        return SF.height_to_pixels( self.meta.speed.eval(time) )

    #--------------------------------------------------------------------------#
    def get_track_boundaries(self):

        return { 
            'top':    [self.track.top,    self.track.left, self.track.right],
            'bottom': [self.track.bottom, self.track.left, self.track.right],
        }

#------------------------------------------------------------------------------#

