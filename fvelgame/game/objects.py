#------------------------------------------------------------------------------#

import random
import pygame

from pygame.locals import *
from pygame        import sprite

import game.game_params as gp
from   game.sound_mixer import SoundMixer

#------------------------------------------------------------------------------#
class GameObjects():

    vertical     = True
    score        = 0

    player       = None
    sprites      = sprite.Group()
    obstacles    = sprite.Group()
    collectibles = sprite.Group()

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

        for sprt in GameObjects.sprites:
            sprt.kill()

    #--------------------------------------------------------------------------#
    def check_collision():

        sprt = sprite.spritecollideany(GameObjects.player,
                                       GameObjects.obstacles,
                                       sprite.collide_mask)

        if sprt:
            sprt.play_sound()

        return sprt

    #--------------------------------------------------------------------------#
    def check_collectible():

        sprt = sprite.spritecollideany(GameObjects.player,
                                       GameObjects.collectibles,
                                       sprite.collide_mask)

        if sprt:
            GameObjects.score += sprt.score
            sprt.play_sound()
            sprt.kill()

        return sprt

    #--------------------------------------------------------------------------#
    def create_player(object_param, speed, boundaries):

        GameObjects.player = Player(object_param, speed, boundaries)
        GameObjects.player.add(GameObjects.sprites)

        return GameObjects.player

    #--------------------------------------------------------------------------#
    def create_obstacle(object_param, boundaries):

        sprt = ScrollingObject(object_param, boundaries, True)

        sprt.add(GameObjects.sprites  )
        sprt.add(GameObjects.obstacles)

        return sprt

    #--------------------------------------------------------------------------#
    def create_collectible( object_param, boundaries ):

        sprt = ScrollingObject(object_param, boundaries)

        sprt.add(GameObjects.sprites     )
        sprt.add(GameObjects.collectibles)

        return sprt

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class GameObject(sprite.Sprite):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):
        '''Create a GameObject'''

        super().__init__()

        self.image  = object_param.image
        self.rect   = self.image.get_rect()
        self.mask   = pygame.mask.from_surface(self.image)
        self.score  = object_param.score

        if object_param.sound:
            self.sound  = SoundMixer.load_sound(object_param.sound)
            self.volume = object_param.volume
        else:
            self.sound = None

    #--------------------------------------------------------------------------#
    def play_sound(self):
        '''Play collision sound if it exists.'''

        if self.sound:
            SoundMixer.play_sound(self.sound, self.volume)

#------------------------------------------------------------------------------#
class Player(GameObject):

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, speed, boundaries):

        super().__init__(object_param)

        if GameObjects.vertical:
            self.rect.centerx = (boundaries[0]+boundaries[1]) // 2
            self.rect.bottom  = int( 0.99*gp.SCREEN_SIZE[1] )
        else:
            self.rect.centery = (boundaries[0]+boundaries[1]) // 2
            self.rect.left    = int( 0.03*gp.SCREEN_SIZE[0] )

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
            self.rect.left    = gp.SCREEN_SIZE[0]

    #--------------------------------------------------------------------------#
    def update(self):

        if GameObjects.vertical:
            self.rect.move_ip( 0, GameObjects.velocity )
            out = self.rect.top > gp.SCREEN_SIZE[1]
        else:
            self.rect.move_ip( -GameObjects.velocity, 0 )
            out = self.rect.right < 1

        if self.obstacle and out:
             GameObjects.score += self.score
             self.kill()

#------------------------------------------------------------------------------#
