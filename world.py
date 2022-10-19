#------------------------------------------------------------------------------#

import pygame
import random
# import time
import objects

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
class World:

    #--------------------------------------------------------------------------#
    def __init__( self, size ):
        
        self.size = size

        self.paramPlayer   = GameObjectParam( (int(0.015*size[0]),int(0.05*size[1])), ( 20, 20,250) )
        self.paramEnemy    = GameObjectParam( (int(0.040*size[0]),int(0.02*size[1])), (250, 20, 20) )
        self.paramTreasure = GameObjectParam( (int(0.020*size[0]),int(0.06*size[1])), ( 20,250,250) )

        self.track = pygame.Rect( int(0.35*size[0]), 0, int(0.3*size[0]), size[1] )

        self.background = pygame.Surface( size )
        self.background.fill( (0,0,0) )

        pygame.draw.rect( self.background, (0,100,20), self.track )

        # Score scaling
        self.score_kill     =  10
        self.score_treasure = 100

        # On screen text
        self.ost_font  = None
        self.ost_small = 30
        self.ost_large = 200
        self.ost_color = (255,255,255)

        # Frames per second
        self.fps = 60

        # Speed
        self.speed          = 15
        self.increase_speed = 2

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

