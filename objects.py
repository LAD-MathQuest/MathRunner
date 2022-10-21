#------------------------------------------------------------------------------#

import pygame
import random

from pygame.locals import *

#------------------------------------------------------------------------------#
class GameObject(pygame.sprite.Sprite):

    track_top    = 0
    track_bottom = 0
    track_left   = 0
    track_right  = 0

    sprites   = pygame.sprite.Group()
    enemies   = pygame.sprite.Group()
    treasures = pygame.sprite.Group()

    #--------------------------------------------------------------------------#
    def __init__( self, world, gameObjectParam ):

        super().__init__() 

        GameObject.track_top    = world.get_track_top   ()
        GameObject.track_bottom = world.get_track_bottom()
        GameObject.track_left   = world.get_track_left  ()
        GameObject.track_right  = world.get_track_right ()
        
        self.image = gameObjectParam.image()
        self.rect  = self.image.get_rect()

        self.add( GameObject.sprites )

#------------------------------------------------------------------------------#
class Player(GameObject):

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.rect.centerx = int( (GameObject.track_right+GameObject.track_left)/2 )
        self.rect.bottom  = int(0.99*GameObject.track_bottom)

        self.speed = world.player_speed

    #--------------------------------------------------------------------------#
    def update(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_q] or pressed_keys[K_ESCAPE]:
            pygame.event.post(pygame.event.Event(QUIT))

        if pressed_keys[K_LEFT] and self.rect.left-self.speed > GameObject.track_left:
            self.rect.move_ip( -self.speed, 0 )

        if pressed_keys[K_RIGHT] and self.rect.right+self.speed < GameObject.track_right:
            self.rect.move_ip( self.speed, 0 )

#------------------------------------------------------------------------------#
class ScrollingObject(GameObject):

    speed = 0

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.rect.centerx = self.random_x()

    #--------------------------------------------------------------------------#
    def update(self):

        self.rect.move_ip( 0, ScrollingObject.speed )
        
        if self.rect.top > GameObject.track_bottom:
            self.kill()

    #--------------------------------------------------------------------------#
    def random_x( self ):

        half_width = int( self.rect.width / 2 )

        return random.randint( GameObject.track_left  + half_width, \
                               GameObject.track_right - half_width )

#------------------------------------------------------------------------------#
class Enemy(ScrollingObject):

    killed = 0

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.add( GameObject.enemies )

    #--------------------------------------------------------------------------#
    def kill( self ):

        Enemy.killed += 1

        super().kill()

#------------------------------------------------------------------------------#
class Treasure(ScrollingObject):

    #--------------------------------------------------------------------------#
    def __init__(self, world, gameObjectParam ):

        super().__init__( world, gameObjectParam )

        self.add( GameObject.treasures )

#------------------------------------------------------------------------------#
