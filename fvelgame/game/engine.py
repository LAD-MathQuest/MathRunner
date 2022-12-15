#------------------------------------------------------------------------------#

import pygame
import random
import time

import game.game_params as gp

from game.objects      import GameObjects
from game.onscreentext import OnScreenText


#------------------------------------------------------------------------------#
class Music:
    '''pygame.mixer.music wrapper to encapsulate existence tests'''

    #--------------------------------------------------------------------------#
    def __init__( self, sound ):

        self.has_sound = bool(sound)

        if self.has_sound:
            pygame.mixer.music.load(sound)
            pygame.mixer.music.set_volume(1.0)

    #--------------------------------------------------------------------------#
    def play(self):
        if self.has_sound:
            pygame.mixer.music.play(-1)

    #--------------------------------------------------------------------------#
    def stop(self):
        if self.has_sound:
            pygame.mixer.music.stop()

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__( self, world ):

        self.world = world
        
        # Create the display background
        self.display = pygame.display.get_surface()
        self.clock   = pygame.time.Clock()

        # Create the on screen text to show the score
        self.ost = OnScreenText( world.ost_area, 3, 2, world.ost_fgcolor, world.ost_bgcolor )
        self.ost.column_width( ['Velocidade: ', '000 000 000'] )

        self.event_restart      = pygame.USEREVENT + 1
        self.event_new_obstacle = pygame.USEREVENT + 2
        self.event_new_collectible = pygame.USEREVENT + 3
    
        pygame.time.set_timer( self.event_new_obstacle, self.world.obstacles_min_time )
        pygame.time.set_timer( self.event_new_collectible, self.world.collectibles_min_time )

        self.music = Music(world.ambience_sound)

    #--------------------------------------------------------------------------#
    def wait(self):
        while True:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    return False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or \
                       event.key == pygame.K_ESCAPE:
                        return False
                    else:
                        return True

            self.clock.tick(gp.FPS)

    #--------------------------------------------------------------------------#
    def game_loop(self):

        self.music.play()

        while True:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    self.music.stop()
                    pygame.quit()
                    return False
        
                elif event.type == self.event_restart:
                    self.music.stop()
                    return True
        
                elif event.type == self.event_new_obstacle:
                    self.new_obstacle()
        
                elif event.type == self.event_new_collectible:
                    self.new_collectible()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q        or \
                       event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return False
                    elif event.key == pygame.K_h      or \
                         event.key == pygame.K_F1     or \
                         event.key == pygame.K_SPACE:
                        self.show_help()
        
            self.update()
            self.clock.tick(gp.FPS)
    
    #------------------------------------------------------------------------------#
    def start(self):

        self.last_rect = pygame.Rect(0,0,0,0)

        self.elapsed_time = 0
        self.velocity     = self.world.eval_velocity(self.elapsed_time)

        GameObjects.init( self.world.get_track_boundaries(), 
                          self.velocity )

        GameObjects.create_player( self.world.param_player, 
                                   self.world.player_speed )


        self.draw()

        if self.wait():
            self.new_obstacle()
            return True
        else:
            return False

    #--------------------------------------------------------------------------#
    def draw(self):

        self.display.blit( self.world.background, (0,0) )

        # Writing the score
        self.display.fill( self.ost.bgcolor, self.ost.area )
        self.ost.draw( self.display, 0, 0, 'Pontos:'     )
        self.ost.draw( self.display, 1, 0, 'Velocidade:' )
        self.ost.draw( self.display, 2, 0, 'Tempo:'      )

        # TODO create a coerent score system
        score = GameObjects.score + int(self.world.score_time_bonus * self.elapsed_time)

        self.ost.draw( self.display, 0, 1, f'{score} ',                 '>' )
        self.ost.draw( self.display, 1, 1, f'{self.velocity:.2f} ',     '>' )
        self.ost.draw( self.display, 2, 1, f'{self.elapsed_time:.2f} ', '>' )

        GameObjects.draw(self.display)

        pygame.display.flip()
        
    #--------------------------------------------------------------------------#
    def game_over(self):

        self.music.stop()

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )
        
        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font( None, size )

        rect = font.get_rect( 'Game Over' )
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,20,20) )

        pygame.display.flip()

        GameObjects.kill_all() 

        if self.wait():
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(self.event_restart) )
        else:
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(pygame.QUIT) )

    #--------------------------------------------------------------------------#
    def show_help(self):

        info = [ [ '<-  ou  a',          'Mover para a esquerda'  ], \
                 [ '->  ou  d',          'Mover para a direita'   ], \
                 [ 'F1,  h  ou  espaço', 'Pausar e mostrar ajuda' ], \
                 [ 'q  ou  esc',         'Sair'                   ]  ]

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

        pygame.display.flip()

        if not self.wait():
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(pygame.QUIT) )

    #--------------------------------------------------------------------------#
    def update(self):

        GameObjects.update()

        self.draw()

        GameObjects.check_collectible()
        
        if GameObjects.check_collision():
            self.game_over()            

        self.elapsed_time += 1 / gp.FPS
        self.velocity      = self.world.eval_velocity(self.elapsed_time)
        GameObjects.scrolling_velocity = self.velocity

    #--------------------------------------------------------------------------#
    def new_obstacle(self):

        sprite = GameObjects.create_obstacle( random.choice(self.world.param_obstacles) )

        rect = sprite.rect

        if pygame.Rect.colliderect( self.last_rect, rect ):
            sprite.kill()
            pygame.time.set_timer( self.event_new_obstacle, 100 )
            return

        self.last_rect = rect

        interval = random.randint( self.world.obstacles_min_time,
                                   self.world.obstacles_max_time )

        pygame.time.set_timer( self.event_new_obstacle, interval )

    #--------------------------------------------------------------------------#
    def new_collectible(self):

        sprite = GameObjects.create_collectible( random.choice(self.world.param_collectibles) )

        rect = sprite.rect

        if pygame.Rect.colliderect( self.last_rect, rect ):
            sprite.kill()
            pygame.time.set_timer( self.event_new_collectible, 100 )
            return

        self.last_rect = rect

        interval = random.randint( self.world.collectibles_min_time,
                                   self.world.collectibles_max_time )

        pygame.time.set_timer( self.event_new_collectible, interval )

#------------------------------------------------------------------------------#
