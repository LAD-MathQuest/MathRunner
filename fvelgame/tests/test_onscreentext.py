#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import pygame
from game.onscreentext import OnScreenText 

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    #--------------------------------------------------------------------------#

    font         = None
    font_size    = 48
    line_spacing = 1.5
    position     = (100,100)
    fgcolor      = (20,20,200)
    bgcolor      = (70,70, 70)

    n_lin = 6
    n_col = 4

    # column_width = 100
    # column_width = [90, 99, 99, 10]
    column_width = ['Linha 0:'] + ['1'+'0'*5+'2']*(n_col-2) + ['|']

    ost = OnScreenText(font, 
                       font_size, 
                       line_spacing, 
                       position,
                       n_lin, 
                       n_col, 
                       column_width,
                       fgcolor, 
                       bgcolor)

    #--------------------------------------------------------------------------#

    display = pygame.display.set_mode((900,600))
    display.fill((100,100,100))

    ost_area = pygame.Rect(position, ost.size)
    pygame.draw.rect(display, (90,90,190), ost_area.inflate(10,10))
    pygame.draw.rect(display, (90,90,140), ost_area)

    #--------------------------------------------------------------------------#
    
    for ii in range(n_lin):

        ost.draw_cell( display, ii, 0,      f'Linha {ii+1}:', '<' )
        ost.draw_cell( display, ii, n_col-1, '|',             '>' )
        
        for jj in range(1,n_col-1):
            ost.draw_cell( display, ii, jj, f'{10**(ii+1) + jj+1}', '>' )

    #--------------------------------------------------------------------------#
    
    while True:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:

                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()
        clock.tick(5)

#------------------------------------------------------------------------------#
