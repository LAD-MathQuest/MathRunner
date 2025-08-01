#------------------------------------------------------------------------------#
'''Defines classes to handle game objects

Only the GameObjects class should the imported from this module.
It handles all necessary object actions
'''

import random

import pygame
import pygame.locals as loc
from   pygame import sprite

from .            import parameters as gp
from .sound_mixer import SoundMixer

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class GameObjects():
    '''Class to handle all object actions through static functions'''

    score  = None
    killed = None

    player       = sprite.GroupSingle()
    obstacles    = sprite.Group()
    collectibles = sprite.Group()

    #--------------------------------------------------------------------------#
    def init(vertical):
        '''Initializes the object module

        Args:
            vertical(bool): True if the game scrolls vertically
        '''

        if vertical:
            GameObjects.PlayerClass    = PlayerVertical
            GameObjects.ScrollingClass = ScrollingObjectVertical
        else:
            GameObjects.PlayerClass    = PlayerHorizontal
            GameObjects.ScrollingClass = ScrollingObjectHorizontal

    #--------------------------------------------------------------------------#
    def start():
        '''Starts objects for a new game'''

        GameObjects.score  = 0
        GameObjects.killed = None

    #--------------------------------------------------------------------------#
    def draw(surface):
        '''Draws all objects on surface

        Args:
            surface (pygame.surface): Surface where the objects will be drawn
        '''

        GameObjects.collectibles.draw(surface)
        GameObjects.obstacles   .draw(surface)
        GameObjects.player      .draw(surface)

    #--------------------------------------------------------------------------#
    def update(displacement, boundary):
        '''Updates all objects

        Args:
            displacement(int): Scrolling objects displacement in pixels
            boundary(int,int): Minimum and maximum player positions
        '''

        GameObjects.displacement = displacement

        GameObjects.collectibles.update()
        GameObjects.obstacles   .update()

        GameObjects.killed = GameObjects.player.sprite.update(boundary)

    #--------------------------------------------------------------------------#
    def kill_all():
        '''Kill all sprites'''

        GameObjects.killed = False

        for sprt in GameObjects.collectibles:
            sprt.kill()

        for sprt in GameObjects.obstacles:
            sprt.kill()

        GameObjects().player.sprite.kill()

    #--------------------------------------------------------------------------#
    def check_collision():
        '''Check for collision between player and any obstacle

        Returns:
            The collided sprite
        '''

        sprt = sprite.spritecollideany(
            GameObjects.player.sprite,
            GameObjects.obstacles,
            sprite.collide_mask
        )

        if sprt:
            sprt.play_sound()

        return sprt

    #--------------------------------------------------------------------------#
    def check_collectible():
        '''Check for collision between player and any collectible

        Returns:
            The collided sprite
        '''

        sprt = sprite.spritecollideany(GameObjects.player.sprite,
                                       GameObjects.collectibles,
                                       sprite.collide_mask)

        if sprt:
            GameObjects.score += sprt.score
            sprt.play_sound()
            sprt.kill()

        return sprt

    #--------------------------------------------------------------------------#
    def create_player(object_param, speed, boundary, boundary_kills):
        '''Create the player sprite

        Args:
            object_param(ObjectParam): Parameters to create the player sprite
            speed(int): Speed in pixels the player can move sideways
            boundary(int,int): Track boundary
            boundary_kills(bool,bool): True if player dies touching the boundary
        '''

        GameObjects.player.sprite = GameObjects.PlayerClass(object_param,
                                                            speed,
                                                            boundary,
                                                            boundary_kills)
        GameObjects.killed = True

        return GameObjects.player.sprite

    #--------------------------------------------------------------------------#
    def create_obstacle(object_param, boundary):
        '''Creates a new obstacle

        Args:
            object_param(ObjectParam): Parameters to create the player sprite
            boundary(int,int): Track boundary
        '''

        sprt = GameObjects.ScrollingClass(object_param, boundary, obstacle=True)
        sprt.add(GameObjects.obstacles)

        return sprt

    #--------------------------------------------------------------------------#
    def create_collectible(object_param, boundary):
        '''Creates a new collectible

        Args:
            object_param(ObjectParam): Parameters to create the player sprite
            boundary(int,int): Track boundary
        '''

        sprt = GameObjects.ScrollingClass(object_param, boundary, obstacle=False)
        sprt.add(GameObjects.collectibles)

        return sprt

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class GameObject(sprite.Sprite):
    '''Class to define all game objects'''

    #--------------------------------------------------------------------------#
    def __init__(self, object_param):
        '''Create a new GameObject

        Args:
            object_param(ObjectParam): Parameters to create the player sprite
        '''

        super().__init__()

        self.image = object_param.image
        self.rect  = self.image.get_rect()
        self.mask  = pygame.mask.from_surface(self.image)
        self.score = object_param.score

        if object_param.sound:
            self.sound  = SoundMixer.load_sound(object_param.sound)
            self.volume = object_param.volume
        else:
            self.sound = None

    #--------------------------------------------------------------------------#
    def play_sound(self):
        '''Play collision sound if it exists'''

        if self.sound:
            SoundMixer.play_sound(self.sound, self.volume)

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class PlayerVertical(GameObject):
    '''Class to define the player object for a vertically scrolling game'''

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, speed, boundary, boundary_kills):
        '''Create the player object

        Args:
            object_param(ObjectParam): Parameters to create the player sprite
            speed(int): Speed in pixels the player can move sideways
            boundary(int,int): Track boundary
            boundary_kills(bool,bool): True if player dies touching the boundary
        '''

        super().__init__(object_param)

        self.speed = speed
        self.kills = boundary_kills

        self.rect.centerx = (boundary[0]+boundary[1]) // 2
        self.rect.bottom  = int( 0.99*gp.SCREEN_SIZE[1] )

    #--------------------------------------------------------------------------#
    def update(self, boundary):
        '''Updates player on a vertically scrolling game

        Args:
            boundary(int,int): Track boundary

        Returns:
            True if player was killed
        '''

        bd_min = boundary[0]
        bd_max = boundary[1]

        if self.kills[0] and self.rect.left  <= bd_min:
            return True

        if self.kills[1] and self.rect.right >= bd_max:
            return True

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[loc.K_LEFT] or pressed_keys[loc.K_a]:
            self.rect.move_ip(-self.speed, 0)

        elif pressed_keys[loc.K_RIGHT] or pressed_keys[loc.K_d]:
            self.rect.move_ip(self.speed, 0)

        if self.rect.left  < bd_min:
            self.rect.left  = bd_min

        if self.rect.right > bd_max:
            self.rect.right = bd_max

        return False

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class PlayerHorizontal(GameObject):
    '''Class to define the player object for a vertically scrolling game'''

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, speed, boundary, boundary_kills):
        '''Create the player object

        Args:
            object_param(ObjectParam): Parameters to create the player sprite
            speed(int): Speed in pixels the player can move sideways
            boundary(int,int): Track boundary
            boundary_kills(bool,bool): True if player dies touching the boundary
        '''

        super().__init__(object_param)

        self.speed = speed
        self.kills = boundary_kills

        self.rect.centery = (boundary[0]+boundary[1]) // 2
        self.rect.left    = int( 0.03*gp.SCREEN_SIZE[0] )

    #--------------------------------------------------------------------------#
    def update(self, boundary):
        '''Updates player on an horizontally scrolling game

        Args:
            boundary(int,int): Track boundary

        Returns:
            True if player was killed
        '''

        bd_min = boundary[0]
        bd_max = boundary[1]

        if self.kills[0] and self.rect.top <= bd_min:
            return True

        if self.kills[1] and self.rect.bottom >= bd_max:
            return True

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[loc.K_UP] or pressed_keys[loc.K_w]:
            self.rect.move_ip(0, -self.speed)

        elif pressed_keys[loc.K_DOWN] or pressed_keys[loc.K_s]:
            self.rect.move_ip(0, self.speed)

        if self.rect.top < bd_min:
            self.rect.top = bd_min

        if self.rect.bottom > bd_max:
            self.rect.bottom = bd_max

        return False

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
def eval_position(ob_lenght, boundary):

    bd_min = boundary[0]
    bd_max = boundary[1]

    aa = ob_lenght // 2

    if aa >= bd_max-bd_min:
        return (bd_max + bd_min) // 2
    else:
        return random.randint(bd_min+aa, bd_max-aa)

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class ScrollingObjectVertical(GameObject):
    '''Class to define scrolling objects for vertically scrolling games'''

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, boundary, obstacle=False):
        '''Create a scrolling object

        Args:
            boundary(int,int): Track boundary
            obstacle(bool): True if object is an obstacle
        '''

        super().__init__(object_param)

        self.obstacle     = obstacle
        self.rect.centerx = eval_position(self.rect.width, boundary)
        self.rect.bottom  = 0

    #--------------------------------------------------------------------------#
    def update(self):
        '''Updates object scrolling it by GameObjects.displacement'''

        self.rect.move_ip(0, GameObjects.displacement)
        out = self.rect.top > gp.SCREEN_SIZE[1]

        if self.obstacle and out:
             GameObjects.score += self.score
             self.kill()

#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class ScrollingObjectHorizontal(GameObject):
    '''Class to define scrolling objects for horizontally scrolling games'''

    #--------------------------------------------------------------------------#
    def __init__(self, object_param, boundary, obstacle=False):
        '''Create a scrolling object

        Args:
            boundary(int,int): Track boundary
            obstacle(bool): True if object is an obstacle
        '''

        super().__init__(object_param)

        self.obstacle     = obstacle
        self.rect.centery = eval_position(self.rect.height, boundary)
        self.rect.left    = gp.SCREEN_SIZE[0]

    #--------------------------------------------------------------------------#
    def update(self):
        '''Updates object scrolling it by GameObjects.displacement'''

        self.rect.move_ip(-GameObjects.displacement, 0)
        out = self.rect.right < 1

        if self.obstacle and out:
             GameObjects.score += self.score
             self.kill()

#------------------------------------------------------------------------------#
