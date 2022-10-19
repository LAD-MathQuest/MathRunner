#------------------------------------------------------------------------------#

import sys
import pygame
from   pygame.locals import *
import random
import time

from   world  import World
import objects

#------------------------------------------------------------------------------#
class Engine:

    #--------------------------------------------------------------------------#
    def __init__( self, world ):

        self.world = world

        # Create the display background
        self.display = pygame.display.set_mode( world.size, pygame.FULLSCREEN )

        self.font = pygame.font.SysFont( self.world.ost_font, self.world.ost_small )
        
        self.event_game_over      = pygame.USEREVENT + 1
        self.event_increase_speed = pygame.USEREVENT + 2
        self.event_new_enemy      = pygame.USEREVENT + 3
        self.event_new_treasure   = pygame.USEREVENT + 4
    
        pygame.time.set_timer( self.event_increase_speed, 2000 )
        pygame.time.set_timer( self.event_new_enemy,       500 )
        pygame.time.set_timer( self.event_new_treasure,   3777 )

    #--------------------------------------------------------------------------#
    def wait( self ):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.event.post( pygame.event.Event(QUIT) )
                    return
                if event.type == KEYDOWN:
                    return

    #--------------------------------------------------------------------------#
    def game_loop( self ):

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
        
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        
                elif event.type == self.event_game_over:
                    return
        
                elif event.type == self.event_increase_speed:
                    self.increase_speed()
        
                elif event.type == self.event_new_enemy:
                    self.new_enemy()
        
                elif event.type == self.event_new_treasure:
                    self.new_treasure()
        
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
        self.wait()

    #--------------------------------------------------------------------------#
    def draw( self ):

        self.display.blit( self.world.background, (0,0) )

        # Writing the score
        score = self.world.score_treasure * self.treasures       \
              + self.world.score_kill     * objects.Enemy.killed

        score_str  = f'pontos: {score}'
        score_surf = self.font.render( score_str, True, self.world.ost_color )

        pos = score_surf.get_rect()

        pos.left = int( 0.05 * self.world.size[0])
        pos.top  = int( 0.10 * self.world.size[1])

        self.display.blit( score_surf, pos )

        # Writing the speed
        speed_str  = f'velocidade: {objects.ScrollingObject.speed:.2f}'
        speed_surf = self.font.render( speed_str, True, self.world.ost_color )

        pos.top = pos.bottom + int( 0.01 * self.world.size[1])

        self.display.blit( speed_surf, pos )

        objects.GameObject.sprites.draw( self.display )
        pygame.display.update()
        
    #--------------------------------------------------------------------------#
    def game_over( self ):
        
        font = pygame.font.SysFont( self.world.ost_font, self.world.ost_large)
        game_over = font.render("Game Over", True, (150,0,0) )

        rect = game_over.get_rect()
        rect.center = self.display.get_rect().center

        self.display.blit( game_over, rect ) 

        pygame.display.update()

        for entity in objects.GameObject.sprites:
            entity.kill() 

        self.wait()
        
        pygame.event.post( pygame.event.Event(self.event_game_over) )

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

    #--------------------------------------------------------------------------#
    def new_treasure( self ):
        objects.Treasure( self.world, self.world.paramTreasure )

#------------------------------------------------------------------------------#
