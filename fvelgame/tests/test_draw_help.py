#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import pygame
from game.draw_help import draw_help

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    name = 'Nome do Jogo'
    desc = '''Descição do Jogo.
É importante questionar o quanto o comprometimento entre as equipes estende o
alcance e a importância dos procedimentos normalmente adotados. 
'''

    pygame.init()
    clock = pygame.time.Clock()

    display = pygame.display.set_mode((0,0))
    display.fill((60,60,60))

    draw_help( display, name, desc, True )

    while True:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_q, pygame.K_ESCAPE ):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        clock.tick( 5 )

#------------------------------------------------------------------------------#
