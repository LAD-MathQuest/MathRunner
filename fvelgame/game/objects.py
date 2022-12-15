#------------------------------------------------------------------------------#

import pygame
import random

from pygame.locals import *

import game.game_params as gp

#------------------------------------------------------------------------------#
class GameObjects():

    track_top_min = 0
    track_top_max = 0

    track_bottom_min = 0
    track_bottom_max = 0

    player       = None
    sprites      = pygame.sprite.Group()
    obstacles    = pygame.sprite.Group()
    collectibles = pygame.sprite.Group()

    scrolling_velocity = 0

    #--------------------------------------------------------------------------#
    def init(boundaries, velocity):

        GameObjects.track_top_min = boundaries['top'][0]
        GameObjects.track_top_max = boundaries['top'][1]

        GameObjects.track_bottom_min = boundaries['bottom'][0]
        GameObjects.track_bottom_max = boundaries['bottom'][1]

        GameObjects.track_bottom = int( 0.99*gp.FULLHD_SIZE[1] )

        GameObjects.score = 0

        GameObjects.scrolling_velocity = velocity

    #--------------------------------------------------------------------------#
    def draw(display):
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
        sprite = pygame.sprite.spritecollideany( GameObjects.player, 
                                                 GameObjects.obstacles )

        if sprite:
            sprite.play_sound()

        return sprite

    #--------------------------------------------------------------------------#
    def check_collectible():

        sprite = pygame.sprite.spritecollideany( GameObjects.player, 
                                                 GameObjects.collectibles )

        if sprite:
            GameObjects.score += sprite.score
            sprite.play_sound()
            sprite.kill()

        return sprite

    #--------------------------------------------------------------------------#
    def create_player(object_param, speed):

        sprite = Player( object_param, speed )
        
        GameObjects.player = sprite
        
        sprite.add( GameObjects.sprites )
        
        return sprite

    #--------------------------------------------------------------------------#
    def create_obstacle(object_param):

        sprite = ScrollingObject(object_param, True)
        
        sprite.add( GameObjects.sprites   )
        sprite.add( GameObjects.obstacles )
        
        return sprite

    #--------------------------------------------------------------------------#
    def create_collectible( object_param ):

        sprite = ScrollingObject(object_param)
        
        sprite.add( GameObjects.sprites      )
        sprite.add( GameObjects.collectibles )
        
        return sprite

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class GameObject(pygame.sprite.Sprite):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):
        '''Create a GameObject'''

        super().__init__() 
        
        self.image = object_param.image
        self.rect  = self.image.get_rect()
        
        self.score = object_param.collision_score
        self.sound = object_param.collision_sound

    #--------------------------------------------------------------------------#
    def play_sound(self):
        '''Play collision sound if it exists.'''

        if self.sound:
            pygame.mixer.Sound(self.sound).play()

#------------------------------------------------------------------------------#
class Player(GameObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, speed):

        super().__init__(object_param)

        self.rect.centerx = int( (GameObjects.track_bottom_min+GameObjects.track_bottom_max)/2 )
        self.rect.bottom  = GameObjects.track_bottom

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
    def __init__(self, object_param, obstacle=False):
        '''Create a ScrollingObject'''

        super().__init__(object_param)

        self.obstacle = obstacle

        # Initial position
        hw = int( self.rect.width / 2 )
        xx = random.randint( GameObjects.track_bottom_min + hw,
                             GameObjects.track_bottom_max - hw )
        
        self.rect.centerx = xx
        self.rect.bottom  = -20

    #--------------------------------------------------------------------------#
    def update(self):

        self.rect.move_ip( 0, GameObjects.scrolling_velocity )
        
        if self.rect.top > gp.FULLHD_SIZE[1]:

            if self.obstacle:
                GameObjects.score += self.score

            self.kill()

#------------------------------------------------------------------------------#
