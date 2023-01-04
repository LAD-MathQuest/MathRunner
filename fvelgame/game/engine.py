#------------------------------------------------------------------------------#

import pygame
import random
import time
import math

import game.game_params as gp

from game.objects     import GameObjects
from game.sound_mixer import SoundMixer
from game.scoreboard  import Scoreboard
from game.draw_help   import draw_help
from game.background  import Background

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world        = world
        self.vertical     = world.game_vertical
        self.clock        = pygame.time.Clock()
        self.background   = Background(world)
        self.scoreboard   = Scoreboard(world.param_scoreboard)
        self.at_game_over = False

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
    def wait_for_focus(self):

        keep_waiting = True

        while keep_waiting:
            for event in pygame.event.get():
                if event.type == pygame.WINDOWFOCUSGAINED:
                    keep_waiting = False

            self.clock.tick(gp.FPS//10)

        self.show_help()
        self.show_help()

    #--------------------------------------------------------------------------#
    def wait(self, showing_help=False):

        pygame.event.clear()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.WINDOWFOCUSLOST:
                    self.wait_for_focus()

                elif event.type == pygame.KEYDOWN:
                    if event.key in [ pygame.K_q, pygame.K_ESCAPE ]:
                        return False

                    elif event.key in [ pygame.K_h, pygame.K_F1, pygame.K_SPACE ]:
                        if showing_help:
                            self.draw()
                            return True
                        else:
                            self.show_help()

                    elif event.key == pygame.K_m:
                        SoundMixer.toggle_mute()

                    elif event.key == pygame.K_n:
                        SoundMixer.toggle_play_music()

                    elif event.key in [ pygame.K_PLUS, pygame.K_EQUALS ]:
                        SoundMixer.volume_up()

                    elif event.key == pygame.K_MINUS:
                        SoundMixer.volume_down()

                    else:
                        return True

            self.clock.tick(gp.FPS//10)

    #--------------------------------------------------------------------------#
    def game_loop(self):

        SoundMixer.play_music()

        pygame.event.clear()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    SoundMixer.stop_music()
                    pygame.quit()
                    return False

                elif event.type == pygame.WINDOWFOCUSLOST:
                    self.wait_for_focus()

                elif event.type == self.event_restart:
                    SoundMixer.stop_music()
                    return True

                elif event.type == self.event_new_obstacle:
                    self.new_obstacle()

                elif event.type == self.event_new_collectible:
                    self.new_collectible()

                elif event.type == pygame.KEYDOWN:

                    if event.key in [ pygame.K_q, pygame.K_ESCAPE ]:
                        SoundMixer.stop_music()
                        pygame.quit()
                        return False

                    elif event.key in [ pygame.K_h, pygame.K_F1, pygame.K_SPACE ]:
                        SoundMixer.stop_music()
                        self.show_help()
                        SoundMixer.play_music()

                    elif event.key == pygame.K_m:
                        SoundMixer.toggle_mute()

                    elif event.key == pygame.K_n:
                        SoundMixer.toggle_play_music()

                    elif event.key in [ pygame.K_PLUS, pygame.K_EQUALS ]:
                        SoundMixer.volume_up()

                    elif event.key == pygame.K_MINUS:
                        SoundMixer.volume_down()

            self.update()
            self.clock.tick(gp.FPS)

    #------------------------------------------------------------------------------#
    def start(self):

        self.last_object_rect = pygame.Rect(0,0,0,0)

        self.start_time   = pygame.time.get_ticks()
        self.elapsed_time = 0

        self.update_velocity()

        GameObjects.init(self.vertical)
        GameObjects.create_player(self.world.param_player,
                                  self.world.player_speed,
                                  self.get_player_boundaries())

        self.draw()
        play = self.wait()

        if play:
            self.new_obstacle()
            self.set_timer_collectibles()

        return play

    #--------------------------------------------------------------------------#
    def draw(self):

        score = GameObjects.score + int(self.world.game_time_bonus * self.elapsed_time)

        self.background.draw(self.display)
        self.scoreboard.draw(self.display, score, self.velocity, self.elapsed_time)
        GameObjects    .draw(self.display)

        if self.at_game_over:
            self.draw_game_over()

        self.flip()

    #--------------------------------------------------------------------------#
    def draw_game_over(self):

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )

        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font( gp.DEFAULT_FONT, size )

        rect = font.get_rect('Game Over')
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,20,20) )

    #--------------------------------------------------------------------------#
    def game_over(self):

        self.at_game_over = True

        SoundMixer.stop_music()
        self.draw()

        play  = self.wait()
        event = self.event_restart if play else pygame.QUIT

        GameObjects.kill_all()

        pygame.event.clear()
        pygame.event.post(pygame.event.Event(event))

        self.at_game_over = False

    #--------------------------------------------------------------------------#
    def show_help(self):

        draw_help(self.display,
                  self.world.soft_name,
                  self.world.soft_description,
                  self.vertical)

        self.flip()

        play = self.wait(showing_help=True)

        if not play:
            pygame.event.clear()
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    #--------------------------------------------------------------------------#
    def update(self):

        self.update_velocity()

        self.background.update(self.displacement)

        GameObjects.update(self.displacement, self.get_player_boundaries())

        self.draw()

        GameObjects.check_collectible()

        if GameObjects.check_collision():
            self.game_over()

    #--------------------------------------------------------------------------#
    def new_obstacle(self):

        ob = random.choice(self.world.param_obstacles)
        sb = self.world.get_spawn_boundaries()

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
        sb = self.world.get_spawn_boundaries()

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
    def get_player_boundaries(self):

        return self.world.get_player_boundaries()

    #--------------------------------------------------------------------------#
    def update_velocity(self):

        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.velocity     = self.world.eval_velocity(self.elapsed_time)
        self.displacement = self.velocity

#------------------------------------------------------------------------------#
