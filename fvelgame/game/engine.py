#------------------------------------------------------------------------------#

import pygame
import random
import time

from   world.world  import World
import objects
from   onscreentext import OnScreenText

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__( self, world ):

        self.world = world
        
        # Create the display background
        self.display = pygame.display.set_mode( world.size, pygame.FULLSCREEN )

        # Create the on screen text to show the score
        self.ost = OnScreenText( world.ost_area, 3, 2, world.ost_fgcolor, world.ost_bgcolor )
        self.ost.column_width( ['Velocidade: ', '000 000'] )

        self.event_restart        = pygame.USEREVENT + 1
        self.event_increase_speed = pygame.USEREVENT + 2
        self.event_new_enemy      = pygame.USEREVENT + 3
        self.event_new_treasure   = pygame.USEREVENT + 4
    
        pygame.time.set_timer( self.event_increase_speed, 1000 )
        pygame.time.set_timer( self.event_new_enemy,    self.world.enemies_min_time )
        pygame.time.set_timer( self.event_new_treasure, self.world.treasures_min_time )

    #--------------------------------------------------------------------------#
    def wait( self ):
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

    #--------------------------------------------------------------------------#
    def game_loop( self ):

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
        
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
        
                elif event.type == self.event_restart:
                    return True
        
                elif event.type == self.event_increase_speed:
                    self.increase_speed()
        
                elif event.type == self.event_new_enemy:
                    self.new_enemy()
        
                elif event.type == self.event_new_treasure:
                    self.new_treasure()

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
            clock.tick( self.world.fps )
    
    #------------------------------------------------------------------------------#

    def start( self ):

        self.treasures = 0;
        objects.ScrollingObject.speed = self.world.speed
        objects.Enemy.killed = 0

        # Create initial sprites
        self.player = objects.Player( self.world, self.world.paramPlayer )
        self.draw()

        if self.wait():
            self.new_enemy()
            return True
        else:
            return False

    #--------------------------------------------------------------------------#
    def draw( self ):

        self.display.blit( self.world.background, (0,0) )

        # Writing the score
        self.display.fill( self.ost.bgcolor, self.ost.area )
        self.ost.draw( self.display, 0, 0, 'Pontos:'     )
        self.ost.draw( self.display, 1, 0, 'Velocidade:' )
        self.ost.draw( self.display, 2, 0, 'Tempo:'      )

        score = self.world.score_treasure * self.treasures       \
              + self.world.score_kill     * objects.Enemy.killed

        self.ost.draw( self.display, 0, 1, f'{score}', '>' )
        self.ost.draw( self.display, 1, 1, f'{objects.ScrollingObject.speed:.2f}', '>' )
        self.ost.draw( self.display, 2, 1, '?', '>' )

        objects.GameObject.sprites.draw( self.display )
        pygame.display.update()
        
    #--------------------------------------------------------------------------#
    def game_over( self ):

        self.display.fill( (60,60,60), None, pygame.BLEND_MULT )
        
        size = self.display.get_rect().height // 6
        font = pygame.freetype.Font( None, size )

        rect = font.get_rect( 'Game Over' )
        rect.center = self.display.get_rect().center
        font.render_to( self.display, rect, None, (200,20,20) )

        pygame.display.update()

        for entity in objects.GameObject.sprites:
            entity.kill() 

        if self.wait():
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(self.event_restart) )
        else:
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(pygame.QUIT) )

    #--------------------------------------------------------------------------#
    def show_help( self ):

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

        pygame.display.update()

        if not self.wait():
            pygame.event.clear()
            pygame.event.post( pygame.event.Event(pygame.QUIT) )

    #--------------------------------------------------------------------------#
    def update( self ):

        objects.GameObject.sprites.update()

        self.draw()
        self.check_collision()
        self.check_treasure()

    #--------------------------------------------------------------------------#
    def check_collision( self ):
        if pygame.sprite.spritecollideany( self.player, objects.GameObject.enemies ):
            self.game_over()            

    #--------------------------------------------------------------------------#
    def check_treasure( self ):
        if pygame.sprite.spritecollideany( self.player, objects.GameObject.treasures ):
            self.score_add_treasure()

    #--------------------------------------------------------------------------#
    def increase_speed( self ):
        objects.ScrollingObject.speed += self.world.increase_speed

    #--------------------------------------------------------------------------#
    def score_add_treasure( self ):
        self.treasures += 1

    #--------------------------------------------------------------------------#
    def new_enemy( self ):
        objects.Enemy( self.world, self.world.paramEnemy )
        # pygame.time.set_timer( self.event_new_treasure,    \
        #       random.randint( self.world.enemies_min_time, \
        #                       self.world.enemies_max_time) )

    #--------------------------------------------------------------------------#
    def new_treasure( self ):
        objects.Treasure( self.world, self.world.paramTreasure )
        # pygame.time.set_timer( self.event_new_treasure,       \
        #        random.randint( self.world.treasures_min_time, \
        #                        self.world.treasures_max_time) )

#------------------------------------------------------------------------------#
