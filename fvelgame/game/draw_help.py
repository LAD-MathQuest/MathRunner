#------------------------------------------------------------------------------#

import pygame

from game.onscreentext import OnScreenText

#------------------------------------------------------------------------------#
def draw_help(surf, name, description, vertical):

    if vertical:
        ll = [ '←', 'A', 'a esquerda' ]
        rr = [ '→', 'D', 'a direita'  ]
    else:
        ll = [ '↑', 'W', 'cima'  ]
        rr = [ '↓', 'S', 'baixo' ]

    info = [ [f'Mover para {ll[2]}',     f'{ll[0]}   ou   {ll[1]}' ],
             [f'Mover para {rr[2]}',     f'{rr[0]}   ou   {rr[1]}' ],
             [ 'Pausar e mostrar ajuda',  'F1,   H   ou   Espaço'  ],
             [ 'Alternar mudo',           'M'                      ],
             [ 'Alternar música',         'N'                      ],
             [ 'Ajustar volume',          '+  −'                   ],
             [ 'Sair',                    'Q   ou   Esc'           ] ]

    n_lin = len(info)

    surf.fill( (40,40,40), None, pygame.BLEND_MULT )

    ww = surf.get_rect().width
    hh = surf.get_rect().height

    area = pygame.Rect( 0.1*ww, 0.15*hh, 0.6*ww, 0.6*hh )

    color = (255,255,255)

    nn = 5 + n_lin

    ost = OnScreenText( None, area, nn, 2, color, None )
    ost.column_width( [ 'M'*15, 'M'*25 ] )
             
    ost.draw( surf, 0, 0, name        )
    ost.draw( surf, 1, 0, description )

    for ii in range(n_lin):
        ost.draw( surf, ii+3, 0, info[ii][0] )
        ost.draw( surf, ii+3, 1, info[ii][1] )

#------------------------------------------------------------------------------#
