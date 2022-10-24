#!/usr/bin/python

import sys
sys.path.append('..')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame
from onscreentext import OnScreenText 

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    pygame.init()
    clock = pygame.time.Clock()

    fgcolor  = (20,20,200)
    bgcolor  = (70,70,70)
    ost_area = pygame.Rect( 100, 150, 700, 200 )

    display = pygame.display.set_mode( (900,600) )
    display.fill( (100,100,100) )
    pygame.draw.rect( display, (90,90,90), ost_area )

    n_lin = 6
    n_col = 4
    ost = OnScreenText( ost_area, n_lin, n_col, fgcolor, bgcolor )

    ost.column_width( [ 'Linha 0: ' ] + [ 200 ]*(n_col-1) )
    ost.column_width( n_col-1, '|' )

    for ii in range(n_lin):

        ost.draw( display, ii, 0, f'Linha {ii+1}:', '<' )
        ost.draw( display, ii, n_col-1, '|', '>' )
        
        for jj in range(1,n_col-1):
            ost.draw( display, ii, jj, f'{10**(ii+1) + jj+1}', '<' )

    while True:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()
        clock.tick( 30 )

#------------------------------------------------------------------------------#
