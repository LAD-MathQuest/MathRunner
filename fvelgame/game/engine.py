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

#------------------------------------------------------------------------------#
def surface_tiling(surf, tile, vertical):

    t_width  = tile.get_width ()
    t_height = tile.get_height()

    s_width  = surf.get_width ()
    s_height = surf.get_height()

    rect   = pygame.Rect((0,0), (t_width,t_height))
    step_x = t_width
    step_y = t_height

    if vertical:
        rect.bottom = s_height
        step_y      = -step_y

    nh = math.ceil(s_height / t_height)
    nw = math.ceil(s_width  / t_width ) 

    rr = rect.copy()

    for ii in range(nh):
        for jj in range(nw):
            surf.blit(tile, rr)
            rr.move_ip(step_x, 0)

        rr.left = rect.left
        rr.move_ip(0, step_y)

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world = world
        self.clock = pygame.time.Clock()

        self.vertical = world.game_vertical

        self.set_display()
        self.set_background()

        SoundMixer.load_music(world.game_ambience, world.game_ambience_volume)

        self.scoreboard = Scoreboard(world.param_scoreboard)

        self.at_game_over = False

        # Blocks unused events
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
                                  pygame.TEXTINPUT  ])

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

        wait = True

        while wait:
            for event in pygame.event.get():
                if event.type == pygame.WINDOWFOCUSGAINED:
                    wait = False

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
        self.velocity     = self.world.eval_velocity(self.elapsed_time)

        GameObjects.init(self.vertical)

        GameObjects.create_player(self.world.param_player, 
                                  self.world.player_speed,
                                  self.world.get_player_boundaries())

        self.draw()

        if self.wait():
            self.new_obstacle()
            self.set_timer_collectibles()
            return True

        else:
            return False

    #--------------------------------------------------------------------------#
    def set_background(self):

        self.bg_scrolls = self.world.background_scrolls

        if self.bg_scrolls:
            self.set_background_scrolling()
        else:
            self.set_background_not_scrolling()

    #--------------------------------------------------------------------------#
    def set_background_not_scrolling(self):

        w_image  = self.world.background_image
        w_width  = w_image.get_width ()
        w_height = w_image.get_height()

        s_width  = gp.SCREEN_SIZE[0]
        s_height = gp.SCREEN_SIZE[1]

        bg_image = pygame.Surface(gp.SCREEN_SIZE)

        if w_width < s_width or w_height < s_height:

            surface_tiling(bg_image, w_image, self.vertical)

        else: # Background has same size or is larger than screen

            rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
            
            if self.vertical:
                rect.bottom = w_height

            bg_image.blit(w_image, (0,0), rect)

        self.bg_image     = bg_image    
        self.bg_show_rect = None

    #--------------------------------------------------------------------------#
    def set_background_scrolling(self):

        w_image  = self.world.background_image
        w_width  = w_image.get_width ()
        w_height = w_image.get_height()

        s_width  = gp.SCREEN_SIZE[0]
        s_height = gp.SCREEN_SIZE[1]

        if self.vertical:

            if w_width < s_width or w_height < s_height:

                n_height = math.ceil(s_height / w_height) * w_height
                n_image  = pygame.Surface((s_width, n_height))

                surface_tiling(n_image, w_image, self.vertical)

                w_image  = n_image
                w_width  = s_width
                w_height = n_height

            self.bg_top_start = w_height
            self.bg_image     = pygame.Surface((s_width, w_height+s_height))
            
            self.bg_image.blit(w_image, (0,s_height))
            self.bg_image.blit(w_image, (0,0), (0,w_height-s_height,s_width,s_height) )

        else: # Horizontal scrolling

            if w_width < s_width or w_height < s_height:

                n_width = math.ceil(s_width / w_width) * w_width
                n_image = pygame.Surface((n_width, s_height))

                surface_tiling(n_image, w_image, self.vertical)

                w_image  = n_image
                w_width  = n_width
                w_height = s_height

            self.bg_max_width = w_width + s_width
            self.bg_image     = pygame.Surface((self.bg_max_width, s_height))

            self.bg_image.blit(w_image, (0,0))
            self.bg_image.blit(w_image, (w_width,0), (0,0,s_width,s_height) )

        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)


        self.bg_scrolls = self.world.background_scrolls

        if not self.bg_scrolls:
            self.bg_image     = self.world.background_image
            self.bg_show_rect = None
            return

        w_bg_image  = self.world.background_image
        w_bg_width  = w_bg_image.get_width ()
        w_bg_height = w_bg_image.get_height()

        sc_width  = gp.SCREEN_SIZE[0]
        sc_height = gp.SCREEN_SIZE[1]

        if self.vertical:

            self.bg_top_start = w_bg_height
            self.bg_image     = pygame.Surface((sc_width, w_bg_height+sc_height))
            
            self.bg_image.blit(w_bg_image, (0,sc_height))
            self.bg_image.blit(w_bg_image, (0,0), (0,w_bg_height-sc_height,sc_width,sc_height) )

        else:
            self.bg_max_width = w_bg_width + sc_width
            self.bg_image     = pygame.Surface((self.bg_max_width, sc_height))

            self.bg_image.blit(w_bg_image, (0,0))
            self.bg_image.blit(w_bg_image, (sc_width+1,0), (0,0,sc_width,sc_height) )

        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

    #--------------------------------------------------------------------------#
    def update_background(self):

        if not self.bg_scrolls:
            return
        
        if self.vertical:
            self.bg_show_rect.top -= self.velocity

            if self.bg_show_rect.top < 0:
                self.bg_show_rect.top = self.bg_top_start + self.bg_show_rect.top

        else:
            self.bg_show_rect.right += self.velocity

            if self.bg_show_rect.right > self.bg_max_width:
                self.bg_show_rect.right += gp.SCREEN_SIZE[0] - self.bg_max_width

    #--------------------------------------------------------------------------#
    def draw_background(self):

        self.display.blit(self.bg_image, (0,0), self.bg_show_rect)

    #--------------------------------------------------------------------------#
    def draw_game_over(self):

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )
        
        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font( gp.DEFAULT_FONT, size )

        rect = font.get_rect('Game Over')
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,20,20) )

    #--------------------------------------------------------------------------#
    def draw(self):

        self.draw_background()

        score = GameObjects.score + int(self.world.game_time_bonus * self.elapsed_time)

        self.scoreboard.draw(self.display, score, self.velocity, self.elapsed_time)

        GameObjects.draw(self.display)

        if self.at_game_over:
            self.draw_game_over()

        self.flip()
        
    #--------------------------------------------------------------------------#
    def game_over(self):

        self.at_game_over = True

        SoundMixer.stop_music()
        self.draw()

        if self.wait():
            event = self.event_restart
        else:
            event = pygame.QUIT

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

        if not self.wait(showing_help=True):
            pygame.event.clear()
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    #--------------------------------------------------------------------------#
    def update(self):

        self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        self.velocity     = self.world.eval_velocity(self.elapsed_time)

        self.update_background()

        GameObjects.update(self.velocity, self.world.get_player_boundaries())

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

            delay = int(10000 / self.velocity * rr)
    
        pygame.time.set_timer(self.event_new_obstacle, delay)

    #--------------------------------------------------------------------------#
    def set_timer_collectibles(self, delay=None):

        if not delay:
            rr = random.uniform(self.world.collectibles_min_delay,
                                self.world.collectibles_max_delay)

            delay = int(10000 / self.velocity * rr)
    
        pygame.time.set_timer(self.event_new_collectible, delay)

#------------------------------------------------------------------------------#
