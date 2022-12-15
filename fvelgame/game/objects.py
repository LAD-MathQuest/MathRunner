#------------------------------------------------------------------------------#

import pygame
import random

from pygame.locals import *

import game.game_params as gp

#------------------------------------------------------------------------------#
class GameObjects():

    vertical     = True
    score        = 0

    player       = None
    sprites      = pygame.sprite.Group()
    obstacles    = pygame.sprite.Group()
    collectibles = pygame.sprite.Group()

    #--------------------------------------------------------------------------#
    def init(vertical):
        GameObjects.vertical = vertical
        GameObjects.score    = 0

    #--------------------------------------------------------------------------#
    def draw(display):
        GameObjects.sprites.draw(display)

    #--------------------------------------------------------------------------#
    def update(velocity, boundaries):
        GameObjects.velocity          = velocity
        GameObjects.player_boundaries = boundaries
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
    def create_player(object_param, speed, boundaries):

        GameObjects.player = Player( object_param, speed, boundaries )
        GameObjects.player.add( GameObjects.sprites )
        
        return GameObjects.player

    #--------------------------------------------------------------------------#
    def create_obstacle(object_param, boundaries):

        sprite = ScrollingObject(object_param, boundaries, True)
        
        sprite.add( GameObjects.sprites   )
        sprite.add( GameObjects.obstacles )
        
        return sprite

    #--------------------------------------------------------------------------#
    def create_collectible( object_param, boundaries ):

        sprite = ScrollingObject(object_param, boundaries)
        
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
    def __init__(self, object_param, speed, boundaries):

        super().__init__(object_param)

        if GameObjects.vertical:
            self.rect.centerx = int( (boundaries[0]+boundaries[1]) / 2 )
            self.rect.bottom  = int( 0.99*gp.FULLHD_SIZE[1] )
        else:
            self.rect.centery = int( (boundaries[0]+boundaries[1]) / 2 )
            self.rect.left    = int( 0.03*gp.FULLHD_SIZE[0] )

        self.speed = speed

    #--------------------------------------------------------------------------#
    def update(self):

        pressed_keys = pygame.key.get_pressed()

        min_ = GameObjects.player_boundaries[0]
        max_ = GameObjects.player_boundaries[1]

        if GameObjects.vertical:

            if pressed_keys[K_LEFT] or pressed_keys[K_a]:
                if self.rect.left-self.speed > min_:
                    self.rect.move_ip( -self.speed, 0 )

            elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
                if self.rect.right+self.speed < max_:
                    self.rect.move_ip( self.speed, 0 )

        else:

            if pressed_keys[K_UP] or pressed_keys[K_w]:
                if self.rect.top-self.speed > min_:
                    self.rect.move_ip( 0, -self.speed )

            elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
                if self.rect.bottom+self.speed < max_:
                    self.rect.move_ip( 0, self.speed )

#------------------------------------------------------------------------------#
class ScrollingObject(GameObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, boundaries, obstacle=False):
        '''Create a ScrollingObject'''

        super().__init__(object_param)

        self.obstacle = obstacle

        if GameObjects.vertical:

            aa = self.rect.width // 2
            
            if aa > boundaries[1] - boundaries[0]:
                xx = ( boundaries[1] + boundaries[0] ) // 2
            else:
                xx = random.randint( boundaries[0]+aa, boundaries[1]-aa )

            self.rect.centerx = xx
            self.rect.bottom  = 0

        else:

            aa = self.rect.height // 2
            
            if aa > boundaries[1] - boundaries[0]:
                yy = ( boundaries[1] + boundaries[0] ) // 2
            else:
                yy = random.randint( boundaries[0]+aa, boundaries[1]-aa )

            self.rect.centery = yy
            self.rect.left    = gp.FULLHD_SIZE[0]

    #--------------------------------------------------------------------------#
    def update(self):

        if GameObjects.vertical:
            self.rect.move_ip( 0, GameObjects.velocity )
            out = self.rect.top > gp.FULLHD_SIZE[1]
        else:
            self.rect.move_ip( -GameObjects.velocity, 0 )
            out = self.rect.right < 1

        if self.obstacle and out:
             GameObjects.score += self.score
             self.kill()

#------------------------------------------------------------------------------#
