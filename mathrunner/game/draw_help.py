#------------------------------------------------------------------------------#

import pygame

from . import game_params as gp
from .onscreentext import OnScreenText

#------------------------------------------------------------------------------#
def draw_help(surf, name,author, description, vertical):
    '''Draw the help message on screen

    Args:
        surf(surface):    Surface to draw the help message to
        name(str):        Game name
        description(str): Game description
        vertical(bool):   True if game scrolls vertially
    '''

    surf.fill((40,40,40), None, pygame.BLEND_MULT)

    font         = None
    font_size    = 32
    line_spacing = 1.7
    fgcolor      = (255,255,255)
    bgcolor      = None
    top          = 300

    #--- Name and description -------------------------------------------------#

    width    = 800
    position = ((gp.SCREEN_SIZE[0]//2-width)//2, top)

    ost = OnScreenText.Paragraph(font,
                                 font_size,
                                 line_spacing,
                                 position,
                                 width,
                                 fgcolor,
                                 bgcolor)

    ## pygame.draw.rect(surf,(100,0,100),(position[0],0,width,1080))
    ## pygame.draw.rect(surf,(  0,0,100),ost.area)

    ost.draw(surf, name)
    ost.draw(surf, '')
    ost.draw(surf, description)
    ost.draw(surf, '')
    ost.draw(surf, 'Criador da fase: '+  author)
    ost.draw(surf, '')
    #--- Commands -------------------------------------------------------------#

    if vertical:
        ll = [ '←', 'A', 'a esquerda' ]
        rr = [ '→', 'D', 'a direita'  ]
    else:
        ll = [ '↑', 'W', 'cima'  ]
        rr = [ '↓', 'S', 'baixo' ]

    info = [ [ 'Controles' ],
             [ '' ],
             [f'Mover para {ll[2]}',     f'{ll[0]}   ou   {ll[1]}' ],
             [f'Mover para {rr[2]}',     f'{rr[0]}   ou   {rr[1]}' ],
             [ 'Pausar e mostrar ajuda',  'F1,   H   ou   Espaço'  ],
             [ 'Alternar mudo',           'M'                      ],
             [ 'Alternar música',         'N'                      ],
             [ 'Ajustar volume',          '+  −'                   ],
             [ 'Sair',                    'Q   ou   Esc'           ] ]

    position     = (int(0.52*gp.SCREEN_SIZE[0]), top)
    num_lines    = len(info)
    num_columns  = 2
    column_width = ['M'*15, 'M'*12]

    ost = OnScreenText.Table(font,
                             font_size,
                             line_spacing,
                             position,
                             num_lines,
                             num_columns,
                             column_width,
                             fgcolor,
                             bgcolor)

    ## pygame.draw.rect(surf,(0,0,100),ost.area)

    ost.draw(surf, info)

#------------------------------------------------------------------------------#

