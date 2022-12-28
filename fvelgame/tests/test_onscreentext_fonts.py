#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from itertools import cycle

import pygame
from game.onscreentext import OnScreenText 

#------------------------------------------------------------------------------#
def draw_ost(surf, font):

    fgcolor  = (250,250,250)
    bgcolor  = (50,50,50)
    ost_area = pygame.Rect( 100, 150, 700, 300 )

    n_lin = 7
    n_col = 2
    ost = OnScreenText( font, ost_area, n_lin, n_col, fgcolor, bgcolor )

    ost.column_width( ['Velocidade: ', ' 0.123.456.789 '] )

    ost.draw( surf, 0, 0, str(Path(font).stem).replace('_',' '), '<' )

    ost.draw( surf, 2, 0, 'Pontos:'     )
    ost.draw( surf, 3, 0, 'Velocidade:' )
    ost.draw( surf, 4, 0, 'Tempo:'      )

    ost.draw( surf, 2, 1, '0.123.456.789', '>' )
    ost.draw( surf, 3, 1, '0.123.456.789', '>' )
    ost.draw( surf, 4, 1, '0.123.456.789', '>' )

    ost.draw( surf, 6, 0, 'ÁáàãâÉéÍíõôúüÇç ←↑↓→', '<' )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    pygame.init()

    display = pygame.display.set_mode( (1200,600) )
    clock   = pygame.time.Clock()

    font_paths = (Path(__file__).parents[1]/'resources'/'fonts').glob('*.*')
    font_names = [ str(path) for path in font_paths ]
    font_names.sort()

    nn = len(font_names)
    ii = 0

    while True:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.key == pygame.K_RIGHT:
                    ii += 1
                    if ii == nn:
                        ii = 0

                elif event.key == pygame.K_LEFT:
                    ii -= 1
                    if ii < 0:
                        ii = nn-1
        
        display.fill((50,50,50))
        draw_ost(display, font_names[ii])
        pygame.display.update()
        clock.tick( 5 )

#------------------------------------------------------------------------------#
