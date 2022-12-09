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
    def __init__( self, meta=MetaWorld() ):

        # Score computing
        self.score_kill     =  10
        self.score_treasure = 100

        # On screen text
        self.ost_area  = pygame.Rect( 100, 100, 400, 120 )
        self.ost_bgcolor = ( 55, 55, 55)
        self.ost_fgcolor = (255,255,255)
        self.ost_large = 200

        # Scrolling speed function
        self.speed          = 15
        self.increase_speed = 2

        # Player speed
        self.player_speed = 10

        # Time interval between spawns (milliseconds)
        self.enemies_min_time   = 700
        self.enemies_max_time   = 2000
        self.treasures_min_time = 3777
        self.treasures_max_time = 4000

    #--------------------------------------------------------------------------#
    def set_dimensions( self, size ):

        self.size = size

        # Sprite parameters
        self.paramPlayer   = GameObjectParam( (int(0.015*size[0]),int(0.05*size[1])), ( 20, 20,250) )
        self.paramEnemy    = GameObjectParam( (int(0.040*size[0]),int(0.02*size[1])), (250, 20, 20) )
        self.paramTreasure = GameObjectParam( (int(0.020*size[0]),int(0.06*size[1])), ( 20,250,250) )

        # Background image
        self.background = pygame.Surface( size )
        self.background.fill( (0,0,0) )

        # Track boundaries and background image
        self.track = pygame.Rect( int(0.35*size[0]), 0, int(0.3*size[0]), size[1] )
        pygame.draw.rect( self.background, (0,100,20), self.track )

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

