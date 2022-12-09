#------------------------------------------------------------------------------#

import pygame
import random

from pygame.locals import *

#------------------------------------------------------------------------------#
class GameObjects(pygame.sprite.Sprite):

    track_top    = 0
    track_bottom = 0
    track_left   = 0
    track_right  = 0

    sprites   = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    treasures = pygame.sprite.Group()

    #--------------------------------------------------------------------------#
    def __init__( self, world, gameObjectParam ):

        super().__init__() 

        GameObjects.track_top    = world.get_track_top   ()
        GameObjects.track_bottom = world.get_track_bottom()
        GameObjects.track_left   = world.get_track_left  ()
        GameObjects.track_right  = world.get_track_right ()
        
        self.image = gameObjectParam.image()
        self.rect  = self.image.get_rect()

        self.add( GameObjects.sprites )

#------------------------------------------------------------------------------#
class Player(GameObjects):

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.rect.centerx = int( (GameObjects.track_right+GameObjects.track_left)/2 )
        self.rect.bottom  = int(0.99*GameObjects.track_bottom)

        self.speed = world.player_speed

    #--------------------------------------------------------------------------#
    def update(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:
            if self.rect.left-self.speed > GameObjects.track_left:
              self.rect.move_ip( -self.speed, 0 )

        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            if self.rect.right+self.speed < GameObjects.track_right:
                self.rect.move_ip( self.speed, 0 )

#------------------------------------------------------------------------------#
class ScrollingObject(GameObjects):

    speed = 0

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.rect.centerx = self.random_x()

    #--------------------------------------------------------------------------#
    def update(self):

        self.rect.move_ip( 0, ScrollingObject.speed )
        
        if self.rect.top > GameObjects.track_bottom:
            self.kill()

    #--------------------------------------------------------------------------#
    def random_x( self ):

        half_width = int( self.rect.width / 2 )

        return random.randint( GameObjects.track_left  + half_width, \
                               GameObjects.track_right - half_width )

#------------------------------------------------------------------------------#
class Obstacle(ScrollingObject):

    dodged = 0

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.add( GameObjects.obstacles )

    #--------------------------------------------------------------------------#
    def dodge( self ):

        Obstacle.dodged += 1

        super().kill()

#------------------------------------------------------------------------------#
class Treasure(ScrollingObject):

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.add( GameObjects.treasures )

#------------------------------------------------------------------------------#
