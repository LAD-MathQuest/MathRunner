#------------------------------------------------------------------------------#

import pygame
import random
import math

import game.game_params as gp

from game.objects     import GameObjects
from game.sound_mixer import SoundMixer
from game.scoreboard  import Scoreboard
from game.draw_help   import draw_help
from game.background  import Background

#------------------------------------------------------------------------------#

# Game status
STATUS_WELCOME  = 0
STATUS_STARTING = 1
STATUS_PLAYING  = 2
STATUS_GAMEOVER = 3

# Exception used to quit the game
class QuitGame(Exception):
    '''Raised to quit the game'''
    pass

WAIT_FPS = gp.FPS // 10
TIME_STEP = 1 / gp.FPS

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world      = world
        self.clock      = pygame.time.Clock()
        self.background = Background(world)
        self.scoreboard = Scoreboard(world.param_scoreboard)

        ii = 1 if self.world.game_vertical else 0
        self.velocity_to_displacement_scale = gp.SCREEN_SIZE[ii] * TIME_STEP

        self.set_display()

        SoundMixer.load_music(world.game_ambience, world.game_ambience_volume)

        # Block unused events
        pygame.event.set_blocked([pygame.MOUSEMOTION,
                                  pygame.MOUSEBUTTONUP,
                                  pygame.MOUSEBUTTONDOWN,
                                  pygame.JOYAXISMOTION,
                                  pygame.JOYBALLMOTION,
                                  pygame.JOYHATMOTION,
                                  pygame.JOYBUTTONUP,
                                  pygame.JOYBUTTONDOWN,
                                  pygame.VIDEORESIZE,
                                  pygame.VIDEOEXPOSE,
                                  pygame.AUDIODEVICEADDED,
                                  pygame.AUDIODEVICEREMOVED,
                                  pygame.FINGERMOTION,
                                  pygame.FINGERDOWN,
                                  pygame.FINGERUP,
                                  pygame.MOUSEWHEEL,
                                  pygame.MULTIGESTURE,
                                  pygame.TEXTEDITING,
                                  pygame.TEXTINPUT])

        self.event_restart         = pygame.USEREVENT + 1
        self.event_new_obstacle    = pygame.USEREVENT + 2
        self.event_new_collectible = pygame.USEREVENT + 3

    #--------------------------------------------------------------------------#
    def set_display(self):

        display = pygame.display.get_surface()
        size    = tuple(display.get_size())

        self.needs_resize = (size != gp.SCREEN_SIZE)

        if self.needs_resize:
            self.display = pygame.Surface(gp.SCREEN_SIZE)
        else:
            self.display = display

    #--------------------------------------------------------------------------#
    def flip(self):

        if self.needs_resize:

            display = pygame.display.get_surface()
            size    = display.get_size()
            resized = pygame.transform.scale(self.display, size)

            display.blit(resized, (0,0))

        pygame.display.flip()

    #--------------------------------------------------------------------------#
    def run(self):

        try:
            self.start(STATUS_WELCOME)

            while True:
                self.game_loop()
                self.start(STATUS_STARTING)

        except QuitGame:
            SoundMixer.stop_music()
            pygame.quit()

    #------------------------------------------------------------------------------#
    def start(self, status):

        self.status = status
        self.elapsed_time = 0
        self.eval_velocity()

        GameObjects.init(self.world.game_vertical)
        GameObjects.create_player(self.world.param_player,
                                  self.world.player_speed,
                                  self.background.get_player_boundaries())

        self.last_object_rect = pygame.Rect(0,0,0,0)

        self.draw()
        self.wait()
        self.new_obstacle()
        self.set_timer_collectibles()

    #--------------------------------------------------------------------------#
    def wait_for_focus(self):

        SoundMixer.stop_music()

        while True:

            event = pygame.event.wait()

            if   event.type == pygame.QUIT:              raise QuitGame
            elif event.type == pygame.WINDOWFOCUSGAINED: break

            self.clock.tick(WAIT_FPS)

        self.draw()
        self.show_help()
        SoundMixer.play_music()

    #--------------------------------------------------------------------------#
    def wait(self, showing_help=False):

        SoundMixer.stop_music()
        pygame.event.clear()

        while True:

            event = pygame.event.wait()

            if   event.type == pygame.QUIT:            raise QuitGame
            elif event.type == pygame.WINDOWFOCUSLOST: self.wait_for_focus()
            elif event.type == pygame.KEYDOWN:

                SoundMixer.parse_key(event.key)

                if   event.key in [pygame.K_q, pygame.K_ESCAPE]: raise QuitGame
                elif event.key in [pygame.K_h, pygame.K_F1, pygame.K_SPACE]:

                    if showing_help: # exit help
                        self.draw()
                        break
                    else:
                        self.show_help()
                else:
                    break

            self.clock.tick(WAIT_FPS)

        SoundMixer.play_music()

    #--------------------------------------------------------------------------#
    def game_loop(self):

        self.status = STATUS_PLAYING

        SoundMixer.play_music()

        pygame.event.clear()

        while True:
            for event in pygame.event.get():

                if   event.type == pygame.QUIT:                raise QuitGame
                elif event.type == pygame.WINDOWFOCUSLOST:     self.wait_for_focus()
                elif event.type == self.event_restart:         return
                elif event.type == self.event_new_obstacle:    self.new_obstacle()
                elif event.type == self.event_new_collectible: self.new_collectible()
                elif event.type == pygame.KEYDOWN:

                    SoundMixer.parse_key(event.key)

                    if   event.key in [pygame.K_q, pygame.K_ESCAPE]:             raise QuitGame
                    elif event.key in [pygame.K_h, pygame.K_F1, pygame.K_SPACE]: self.show_help()

            self.update()
            self.draw  ()

            self.clock.tick(gp.FPS)
            self.elapsed_time += TIME_STEP

    #--------------------------------------------------------------------------#
    def draw(self):

        score = GameObjects.score + int(self.world.game_time_bonus * self.elapsed_time)

        self.background.draw(self.display)
        self.scoreboard.draw(self.display, score, self.velocity, self.elapsed_time)
        GameObjects    .draw(self.display)

        if   self.status == STATUS_WELCOME:  self.draw_welcome  ()
        elif self.status == STATUS_STARTING: self.draw_starting ()
        elif self.status == STATUS_GAMEOVER: self.draw_game_over()

        self.flip()

    #--------------------------------------------------------------------------#
    def draw_welcome(self):

        self.display.fill( (150,150,150), None, pygame.BLEND_MULT )

        size = self.display.get_rect().height // 10
        font = pygame.freetype.Font( gp.DEFAULT_FONT, size )

        rect = font.get_rect(self.world.soft_name)
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,200,200) )

    #--------------------------------------------------------------------------#
    def draw_starting(self):

        self.display.fill( (150,150,150), None, pygame.BLEND_MULT )

        size = self.display.get_rect().height // 14
        font = pygame.freetype.Font( gp.DEFAULT_FONT, size )

        rect = font.get_rect('Pressione qualquer tecla')
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,200,200) )

    #--------------------------------------------------------------------------#
    def draw_game_over(self):

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )

        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font( gp.DEFAULT_FONT, size )

        rect = font.get_rect('Game Over')
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,20,20) )

    #--------------------------------------------------------------------------#
    def show_help(self):

        draw_help(self.display,
                  self.world.soft_name,
                  self.world.soft_description,
                  self.world.game_vertical)

        self.flip()
        self.wait(showing_help=True)

    #--------------------------------------------------------------------------#
    def game_over(self):

        self.status = STATUS_GAMEOVER

        SoundMixer.stop_music()

        self.draw()
        self.wait()

        GameObjects.kill_all()

        pygame.event.clear()
        pygame.event.post(pygame.event.Event(self.event_restart))

        self.status = STATUS_PLAYING

    #--------------------------------------------------------------------------#
    def update(self):

        self.eval_velocity()
        self.background.update(self.displacement)

        GameObjects.update(self.displacement, self.background.get_player_boundaries())
        GameObjects.check_collectible()

        if GameObjects.check_collision(): self.game_over()

    #--------------------------------------------------------------------------#
    def new_obstacle(self):

        ob = random.choice(self.world.param_obstacles)
        sb = self.background.get_spawn_boundaries()

        sprite = GameObjects.create_obstacle(ob, sb)
        rect   = sprite.rect

        # Discart the sprite if it overlaps with the last one
        if pygame.Rect.colliderect(self.last_object_rect, rect):
            sprite.kill()
            self.set_timer_obstacles(100)
            return

        self.last_object_rect = rect
        self.set_timer_obstacles()

    #--------------------------------------------------------------------------#
    def new_collectible(self):

        ob = random.choice(self.world.param_collectibles)
        sb = self.background.get_spawn_boundaries()

        sprite = GameObjects.create_collectible(ob, sb)
        rect   = sprite.rect

        # Discart the sprite if it overlaps with the last one
        if pygame.Rect.colliderect(self.last_object_rect, rect):
            sprite.kill()
            self.set_timer_collectibles(100)
            return

        self.last_object_rect = rect
        self.set_timer_collectibles()

    #--------------------------------------------------------------------------#
    def set_timer_obstacles(self, delay=None):

        if not delay:
            rr = random.uniform(self.world.obstacles_min_delay,
                                self.world.obstacles_max_delay)

            delay = int(10000 / self.displacement * rr)

        pygame.time.set_timer(self.event_new_obstacle, delay)

    #--------------------------------------------------------------------------#
    def set_timer_collectibles(self, delay=None):

        if not delay:
            rr = random.uniform(self.world.collectibles_min_delay,
                                self.world.collectibles_max_delay)

            delay = int(10000 / self.displacement * rr)

        pygame.time.set_timer(self.event_new_collectible, delay)

    #--------------------------------------------------------------------------#
    def eval_velocity(self):

        self.velocity     = self.world.velocity.eval(self.elapsed_time)
        self.displacement = math.ceil(self.velocity * self.velocity_to_displacement_scale)

#------------------------------------------------------------------------------#
