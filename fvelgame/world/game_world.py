#------------------------------------------------------------------------------#

import pygame

from world.meta_world import MetaWorld

#------------------------------------------------------------------------------#
class GameObjectParam:

    #--------------------------------------------------------------------------#
    def __init__( self, size, color ):

        self.size  = size
        self.color = color

    #--------------------------------------------------------------------------#
    def image( self ):
        
        surf = pygame.Surface( self.size )
        surf.fill( self.color )
        
        return surf

#------------------------------------------------------------------------------#
class GameWorld:

    #--------------------------------------------------------------------------#
    def __init__( self, meta ):

        self.meta = meta

        # Score computing
        self.score_time_bonus = meta.score_time_bonus # Points per milliseconds
        self.score_dodge      = meta.score_dodge     
        self.score_treasure   = meta.score_treasure  

        # On screen text
        self.ost_area    = pygame.Rect(meta.ost.area)
        self.ost_bgcolor = meta.ost.bgcolor
        self.ost_fgcolor = meta.ost.fgcolor

        # Time interval between spawns (milliseconds)
        self.obstacles_min_time = 300
        self.obstacles_max_time = 1000
        self.treasures_min_time = 500
        self.treasures_max_time = 4000

    #--------------------------------------------------------------------------#
    def set_dimensions( self, width, height ):

        self.size = (width, height)

        self.width  = width
        self.height = height

        self.mw = width  / 1000
        self.mh = height / 1000

        # Player speed
        # TODO take direction in account
        self.player_speed = self.meta.player_speed * self.mw

        # Sprite parameters
        self.param_player   = GameObjectParam( (int(0.015*width),int(0.05*height)), ( 20, 20,250) )
        self.param_obstacle = GameObjectParam( (int(0.040*width),int(0.02*height)), (250, 20, 20) )
        self.param_treasure = GameObjectParam( (int(0.020*width),int(0.06*height)), ( 20,250,250) )

        # Background image
        self.background = pygame.Surface((width,height))
        self.background.fill((0,0,0))

        # Track boundaries and background image
        self.track = pygame.Rect( int(0.35*width), 0, int(0.3*width), height )
        pygame.draw.rect( self.background, (0,100,20), self.track )

    #--------------------------------------------------------------------------#
    def eval_speed( self, time ):
        # TODO take direction in account
        return self.meta.speed.eval(time) * self.mh

    #--------------------------------------------------------------------------#
    def get_track_top( self ):
        return self.track.top

    #--------------------------------------------------------------------------#
    def get_track_bottom( self ):
        return self.track.bottom

    #--------------------------------------------------------------------------#
    def get_track_left( self ):
        return self.track.left

    #--------------------------------------------------------------------------#
    def get_track_right( self ):
        return self.track.right

#------------------------------------------------------------------------------#

