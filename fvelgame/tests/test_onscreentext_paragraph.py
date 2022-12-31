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
    font_size    = 24
    line_spacing = 1.5
    position     = (100,100)
    width        = 600
    fgcolor      = (255,255,255)
    bgcolor      = None

    ost = OnScreenText.Paragraph(font, 
                                 font_size, 
                                 line_spacing, 
                                 position,
                                 width,
                                 fgcolor, 
                                 bgcolor)

    #--------------------------------------------------------------------------#

    display = pygame.display.set_mode((900,600))
    display.fill((100,100,100))

    ost_area = pygame.Rect(position, (width,400))
    pygame.draw.rect(display, (50,50,50), ost_area)

    #--------------------------------------------------------------------------#
    
    text = ['Título',
            'Subtítulo',
            '', 
            'Percebemos, cada vez mais, que o comprometimento entre as equipes não pode mais se dissociar dos procedimentos normalmente adotados.',
            '', 
            '''String com várias linhas
Linha 1
Linha 2
Linha 3
Última linha
'''
            ]

    ost.draw( display, text )

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
