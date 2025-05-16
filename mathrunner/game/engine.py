#------------------------------------------------------------------------------#
'''Defines game Engine class'''

import pygame
import random
import math

import game.game_params as gp

from game.objects     import GameObjects
from game.sound_mixer import SoundMixer
from game.scoreboard  import Scoreboard
from game.draw_help   import draw_help

from game.background_horizontal import BackgroundHorizontal
from game.background_vertical   import BackgroundVertical

#------------------------------------------------------------------------------#

# Game status
STATUS_WELCOME  = 0
STATUS_STARTING = 1
STATUS_PLAYING  = 2
STATUS_GAMEOVER = 3

# Exception used to quit the game
class QuitGame(Exception): pass

WAIT_FPS  = gp.FPS // 10
TIME_STEP = 1 / gp.FPS

#------------------------------------------------------------------------------#
class Engine:
    '''Game engine'''

    #--------------------------------------------------------------------------#
    def __init__(self, world):
        '''Initialization of Game Engine

        Args:
            world(GameWorld): The GameWorld that defines the game
        '''

        self.world      = world
        self.clock      = pygame.time.Clock()
        self.scoreboard = Scoreboard(world.param_scoreboard)

        if world.game_vertical:
            self.background         = BackgroundVertical(world)
            self.displacement_scale = gp.SCREEN_SIZE[1] * TIME_STEP
        else:
            self.background         = BackgroundHorizontal(world)
            self.displacement_scale = gp.SCREEN_SIZE[0] * TIME_STEP

        GameObjects.init(world.game_vertical)

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
        '''Initializes the display surface and remembers if it needs resize'''

        display = pygame.display.get_surface()
        size    = tuple(display.get_size())

        self.needs_resize = (size != gp.SCREEN_SIZE)

        if self.needs_resize:
            self.display = pygame.Surface(gp.SCREEN_SIZE)
        else:
            self.display = display

    #--------------------------------------------------------------------------#
    def flip(self):
        '''Resizes display if needed and calls pygame.display.flip'''

        if self.needs_resize:

            display = pygame.display.get_surface()
            size    = display.get_size()
            resized = pygame.transform.scale(self.display, size)

            display.blit(resized, (0,0))

        pygame.display.flip()

    #--------------------------------------------------------------------------#
    def run(self):
        '''Run the game'''

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
        '''Initializes a game instance

        Args:
            status(int): Game status, it can be STATUS_WELCOME or STATUS_STARTING
        '''

        self.status = status
        self.elapsed_time = 0
        self.eval_velocity()

        GameObjects.start()
        GameObjects.create_player(self.world.param_player,
                                  self.world.player_speed,
                                  self.background.get_player_boundaries(),
                                  self.world.track_kills)

        self.last_object_rect = pygame.Rect(0,0,0,0)

        self.draw()
        self.wait()
        self.new_obstacle()
        self.set_timer_collectibles()

    #--------------------------------------------------------------------------#
    def wait_for_focus(self):
        '''Waits for the process to receive focus

        Shows help screen on return
        '''

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
        '''Wait for user action

        This function is used when showing information screens

        Args:
            show_help(bool): True when showing help message
        '''

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
        '''The main game loop'''

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
        '''Main draw function'''

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
        '''Draws the welcome message'''

        self.display.fill((150,150,150), None, pygame.BLEND_MULT)

        size = self.display.get_rect().height // 10
        font = pygame.freetype.Font(gp.DEFAULT_FONT, size)

        rect = font.get_rect(self.world.soft_name)
        rect.center = self.display.get_rect().center
        font.render_to(self.display, rect, None, (200,200,200))

    #--------------------------------------------------------------------------#
    def draw_starting(self):
        '''Draws the game starting message'''

        self.display.fill((130,130,130), None, pygame.BLEND_MULT)

    #--------------------------------------------------------------------------#
    def draw_game_over(self):
        '''Draws the game over message'''

        self.display.fill((60,60,60), None, pygame.BLEND_MULT)

        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font(gp.DEFAULT_FONT, size)

        rect = font.get_rect('Game Over')
        rect.center = self.display.get_rect().center
        font.render_to(self.display, rect, None, (200,20,20))

    #--------------------------------------------------------------------------#
    def show_help(self):
        '''Draw help screen and enter wait mode'''

        draw_help(self.display,
                  self.world.soft_name,
                  self.world.soft_description,
                  self.world.game_vertical)

        self.flip()
        self.wait(showing_help=True)

    #--------------------------------------------------------------------------#
    def game_over(self):
        '''Handles game over'''

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
        '''Updates all game elements and checks for collisions'''

        self.eval_velocity()
        self.background.update(self.displacement)

        GameObjects.update(self.displacement, self.background.get_player_boundaries())
        GameObjects.check_collectible()

        if GameObjects.killed or GameObjects.check_collision():
            self.game_over()

    #--------------------------------------------------------------------------#
    def new_obstacle(self):
        '''Creates a new obstale object'''

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
        '''Creates a new collectible object'''

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
        '''Restarts timer to raise next obstacle creation event

        Args:
            delay(int): Delay value in milliseconds
        '''

        if not delay:
            rr = random.uniform(self.world.obstacles_min_delay,
                                self.world.obstacles_max_delay)

            delay = int(10000 / self.displacement * rr)

        pygame.time.set_timer(self.event_new_obstacle, delay)

    #--------------------------------------------------------------------------#
    def set_timer_collectibles(self, delay=None):
        '''Restarts timer to raise next collectible creation event

        Args:
            delay(int): Delay value in milliseconds
        '''

        if not delay:
            rr = random.uniform(self.world.collectibles_min_delay,
                                self.world.collectibles_max_delay)

            delay = int(10000 / self.displacement * rr)

        pygame.time.set_timer(self.event_new_collectible, delay)

    #--------------------------------------------------------------------------#
    def eval_velocity(self):
        '''Evals velocity and displacement values'''

        self.velocity     = self.world.velocity.eval(self.elapsed_time)
        self.displacement = math.ceil(self.velocity * self.displacement_scale)

#------------------------------------------------------------------------------#