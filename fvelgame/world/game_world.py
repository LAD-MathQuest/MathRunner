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

import game.game_params as gp
from world.meta_world import MetaWorld

#------------------------------------------------------------------------------#
def surface_from_meta_image(meta):
    '''Create a pygame surface from a MetaImage object'''

    if meta.image_path:
        surf = pygame.image.load(meta.image_path).convert_alpha()
        surf = pygame.transform.scale(surf, meta.size )
    else:
        surf = pygame.Surface(meta.size)
        surf.fill(meta.color)

    return surf

#------------------------------------------------------------------------------#
class GameObjectParam:
    '''Stores all parameters needed to create game objects (sprite).'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create game object parameters from a meta object.'''

        self.image = surface_from_meta_image(meta.image)

        self.collision_score = meta.score
        self.collision_sound = meta.sound

#------------------------------------------------------------------------------#
class GameWorld:
    '''Manages all parameters needed by the game Engine.'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create a GameWorld from MetaWorld.'''

        self.vertical = meta.dynamics['vertical']
        self.ambience_sound = meta.ambience_sound

        # TODO Replace uniform distribution for a arrivel distribution
        self.obstacles_frequency    = meta.dynamics['obstacles_frequency'   ]
        self.collectibles_frequency = meta.dynamics['collectibles_frequency']

        self.obstacles_min_time    =  100
        self.obstacles_max_time    = 1000
        self.collectibles_min_time =  500
        self.collectibles_max_time = 4000

        self.score_time_bonus = meta.dynamics['score_time_bonus']

        self.ost_bgcolor = meta.appearance['ost_bgcolor']
        self.ost_fgcolor = meta.appearance['ost_fgcolor']

        self.player_speed = meta.dynamics['player_speed']
        self.param_player = GameObjectParam( meta.objects['player'] )

        self.param_obstacles    = [ GameObjectParam(ob) for ob in meta.objects['obstacles'   ] ]
        self.param_collectibles = [ GameObjectParam(ob) for ob in meta.objects['collectibles'] ]

        # TODO Compute ost size properly
        self.ost_area = pygame.Rect( meta.appearance['ost_position'], (260,110) )
        
        # Background and track images
        self.background = surface_from_meta_image( meta.appearance['background'] )
        self.track      = surface_from_meta_image( meta.appearance['track'     ] )

        # Geting constant track rectangle
        min_, lenght = meta.margins.eval(0)

        if self.vertical:
            left  = int( gp.SCREEN_SIZE[0] * min_   )
            width = int( gp.SCREEN_SIZE[0] * lenght )
            self.track_rect = pygame.Rect( left, 0, width, gp.SCREEN_SIZE[1] )
        else:
            top    = int( gp.SCREEN_SIZE[1] * min_   )
            height = int( gp.SCREEN_SIZE[1] * lenght )
            self.track_rect = pygame.Rect( 0, top, gp.SCREEN_SIZE[0], height )

        # TODO implement image blits of track and background
        color = meta.appearance['track'].color 
        pygame.draw.rect( self.background, color, self.track_rect )

        self.velocity = meta.velocity

    #--------------------------------------------------------------------------#
    def eval_velocity(self, time):
        ''' Eval scrolling velocity in pixels'''

        return int( self.velocity.eval(time) )

    #--------------------------------------------------------------------------#
    def eval_margins(self, time):
        ''' Eval margins in pixels'''

        pass

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):

        if self.vertical:
            return [self.track_rect.left, self.track_rect.right]
        else:
            return [self.track_rect.top, self.track_rect.bottom]

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):

        if self.vertical:
            return [self.track_rect.left, self.track_rect.right]
        else:
            return [self.track_rect.top, self.track_rect.bottom]

#------------------------------------------------------------------------------#

