#------------------------------------------------------------------------------#

import pygame
import random

from pygame.locals import *

#------------------------------------------------------------------------------#
class GameObjects():

    track_top     = 0
    track_top_min = 0
    track_top_max = 0

    track_bottom     = 0
    track_bottom_min = 0
    track_bottom_max = 0

    player    = None
    sprites   = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    treasures = pygame.sprite.Group()

    obstacles_dodged   = 0
    treasures_colected = 0

    scrolling_velocity = 0

    #--------------------------------------------------------------------------#
    def init( boundaries, velocity ):

        GameObjects.track_top     = boundaries['top'][0]
        GameObjects.track_top_min = boundaries['top'][1]
        GameObjects.track_top_max = boundaries['top'][2]

        GameObjects.track_bottom     = boundaries['bottom'][0]
        GameObjects.track_bottom_min = boundaries['bottom'][1]
        GameObjects.track_bottom_max = boundaries['bottom'][2]

        GameObjects.obstacles_dodged   = 0
        GameObjects.treasures_colected = 0

        GameObjects.scrolling_velocity = velocity

    #--------------------------------------------------------------------------#
    def draw_sprites( display ):
        GameObjects.sprites.draw(display)

    #--------------------------------------------------------------------------#
    def update():
        GameObjects.sprites.update()

    #--------------------------------------------------------------------------#
    def kill_all():
        for sprite in GameObjects.sprites:
            sprite.kill() 

    #--------------------------------------------------------------------------#
    def check_collision():
        return pygame.sprite.spritecollideany( GameObjects.player, 
                                               GameObjects.obstacles )

    #--------------------------------------------------------------------------#
    def check_treasure():

        sprite = pygame.sprite.spritecollideany( GameObjects.player, 
                                                 GameObjects.treasures )

        if sprite:
            sprite.kill()
            GameObjects.treasures_colected += 1

        return sprite

    #--------------------------------------------------------------------------#
    def create_player( object_param, speed ):

        sprite = Player( object_param, speed )
        
        GameObjects.player = sprite
        
        sprite.add( GameObjects.sprites )
        
        return sprite

    #--------------------------------------------------------------------------#
    def create_obstacle( object_param ):

        sprite = Obstacle( object_param )
        
        sprite.add( GameObjects.sprites   )
        sprite.add( GameObjects.obstacles )
        
        return sprite

    #--------------------------------------------------------------------------#
    def create_treasure( object_param ):

        sprite = Treasure( object_param )
        
        sprite.add( GameObjects.sprites   )
        sprite.add( GameObjects.treasures )
        
        return sprite

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class GameObject(pygame.sprite.Sprite):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):

        super().__init__() 
        
        self.image = object_param.image
        self.rect  = self.image.get_rect()

#------------------------------------------------------------------------------#
class Player(GameObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, speed):

        super().__init__(object_param)

        self.rect.centerx = int( (GameObjects.track_bottom_min+GameObjects.track_bottom_max)/2 )
        self.rect.bottom  = int( 0.99*GameObjects.track_bottom )

        self.speed = speed

    #--------------------------------------------------------------------------#
    def update(self):

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT] or pressed_keys[K_a]:

            if self.rect.left-self.speed > GameObjects.track_bottom_min:
                self.rect.move_ip( -self.speed, 0 )

        elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
            
            if self.rect.right+self.speed < GameObjects.track_bottom_max:
                self.rect.move_ip( self.speed, 0 )

#------------------------------------------------------------------------------#
class ScrollingObject(GameObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):

        super().__init__(object_param)

        hw = int( self.rect.width / 2 )
        xx = random.randint( GameObjects.track_bottom_min + hw,
                             GameObjects.track_bottom_max - hw )
        
        self.rect.centerx = xx

    #--------------------------------------------------------------------------#
    def update(self):

        self.rect.move_ip( 0, GameObjects.scrolling_velocity )
        
        if self.rect.top > GameObjects.track_bottom:
            self.kill()

#------------------------------------------------------------------------------#
class Obstacle(ScrollingObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):
        super().__init__(object_param)

    #--------------------------------------------------------------------------#
    def kill(self):
        GameObjects.obstacles_dodged += 1
        super().kill()

#------------------------------------------------------------------------------#
class Treasure(ScrollingObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):
        super().__init__(object_param)

#------------------------------------------------------------------------------#
