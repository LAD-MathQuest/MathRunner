#------------------------------------------------------------------------------#

import pygame
import random
import time

import game.game_params as gp

from game.objects      import GameObjects
from game.onscreentext import OnScreenText
from game.sound_mixer  import SoundMixer

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__( self, world ):

        self.world = world
        self.clock = pygame.time.Clock()

        self.set_display()

        # Create the on screen text to show the score
        area = pygame.Rect( world.scoreboard_text_position, (100,100)) 
        self.ost = OnScreenText(area, 3, 2, 
                                world.scoreboard_text_fgcolor, 
                                world.scoreboard_text_bgcolor )
        self.ost.column_width(['Velocidade: ', '000000'])

        self.event_restart         = pygame.USEREVENT + 1
        self.event_new_obstacle    = pygame.USEREVENT + 2
        self.event_new_collectible = pygame.USEREVENT + 3

        self.mixer = SoundMixer(world.game_ambience)

    #--------------------------------------------------------------------------#
    def set_display(self):

        display = pygame.display.get_surface()
        size    = tuple(display.get_size())

        self.needs_resize = ( size != gp.SCREEN_SIZE )

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
    def wait(self):
        while True:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.KEYDOWN:
                    if event.key in [ pygame.K_q, pygame.K_ESCAPE ]:
                        return False
                    else:
                        return True

            self.clock.tick(gp.FPS)

    #--------------------------------------------------------------------------#
    def game_loop(self):

        self.mixer.play()

        while True:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    self.mixer.stop()
                    pygame.quit()
                    return False
        
                elif event.type == self.event_restart:
                    self.mixer.stop()
                    return True
        
                elif event.type == self.event_new_obstacle:
                    self.new_obstacle()
        
                elif event.type == self.event_new_collectible:
                    self.new_collectible()

                elif event.type == pygame.KEYDOWN:

                    if event.key in [ pygame.K_q, pygame.K_ESCAPE ]:
                        pygame.quit()
                        return False

                    elif event.key in [ pygame.K_h, pygame.K_F1, pygame.K_SPACE ]:
                        self.show_help()

                    elif event.key == pygame.K_m:
                        self.mixer.toggle_mute()
        
            self.update()
            self.clock.tick(gp.FPS)
    
    #------------------------------------------------------------------------------#
    def start(self):

        self.last_object_rect = pygame.Rect(0,0,0,0)

        self.elapsed_time = 0
        self.velocity     = self.world.eval_velocity(self.elapsed_time)

        GameObjects.init(self.world.game_vertical)

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
    def draw(self):

        self.display.blit(self.world.background_image, (0,0))

        # Writing the score
        self.display.fill( self.ost.bgcolor, self.ost.area )
        self.ost.draw( self.display, 0, 0, 'Pontos:'     )
        self.ost.draw( self.display, 1, 0, 'Velocidade:' )
        self.ost.draw( self.display, 2, 0, 'Tempo:'      )

        score = GameObjects.score + int(self.world.game_time_bonus * self.elapsed_time)

        self.ost.draw( self.display, 0, 1, f'{score} ',                 '>' )
        self.ost.draw( self.display, 1, 1, f'{self.velocity:.2f} ',     '>' )
        self.ost.draw( self.display, 2, 1, f'{self.elapsed_time:.2f} ', '>' )

        GameObjects.draw(self.display)

        self.flip()
        
    #--------------------------------------------------------------------------#
    def game_over(self):

        self.mixer.stop()

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )
        
        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font( None, size )

        rect = font.get_rect('Game Over')
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,20,20) )

        self.flip()

        GameObjects.kill_all() 

        if self.wait():
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(self.event_restart) )
        else:
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(pygame.QUIT) )

    #--------------------------------------------------------------------------#
    def show_help(self):

        info = [ [ '[<] ou [A]',            'Mover para a esquerda'  ], \
                 [ '[>] ou [D]',            'Mover para a direita'   ], \
                 [ '[F1], [H] ou [espaço]', 'Pausar e mostrar ajuda' ], \
                 [ '[M]',                   'Alternar mudo'          ], \
                 [ '[Q] ou [esc]',          'Sair'                   ]  ]

        n_lin = len(info)

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )

        w = self.display.get_rect().width
        h = self.display.get_rect().height

        area = pygame.Rect( 0, 0, w//3, h//4 )
        area.center = self.display.get_rect().center

        color = (255,255,255)

        ost = OnScreenText( area, 2*n_lin, 2, color, None )
        ost.column_width( [ 'M'*12, 'M'*25 ] )

        for ii in range(n_lin):
            ost.draw( self.display, 2*ii, 0, info[ii][0] )
            ost.draw( self.display, 2*ii, 1, info[ii][1] )

        self.flip()

        if not self.wait():
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(pygame.QUIT) )

    #--------------------------------------------------------------------------#
    def update(self):

        self.elapsed_time += 1 / gp.FPS
        self.velocity      = self.world.eval_velocity(self.elapsed_time)

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

        # Discart this sprite if it overlaps with the last one
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

        # Discart this sprite if it overlaps with the last one
        if pygame.Rect.colliderect(self.last_object_rect, rect):
            sprite.kill()
            self.set_timer_collectibles(100)
            return

        self.last_object_rect = rect

        self.set_timer_collectibles()

    #--------------------------------------------------------------------------#
    def set_timer_obstacles(self, delay=None):

        if not delay:
            delay = int( 1000 * random.uniform(self.world.obstacles_min_delay,
                                               self.world.obstacles_max_delay) )
    
        pygame.time.set_timer(self.event_new_obstacle, delay )

    #--------------------------------------------------------------------------#
    def set_timer_collectibles(self, delay=None):

        if not delay:
            delay = int( 1000 * random.uniform(self.world.collectibles_min_delay,
                                               self.world.collectibles_max_delay) )
    
        pygame.time.set_timer(self.event_new_collectible, delay )

#------------------------------------------------------------------------------#
