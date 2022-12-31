#------------------------------------------------------------------------------#

import pygame

import game.game_params as gp

from game.onscreentext import OnScreenText

#------------------------------------------------------------------------------#
def draw_help(surf, name, description, vertical):

    if vertical:
        ll = [ '←', 'A', 'a esquerda' ]
        rr = [ '→', 'D', 'a direita'  ]
    else:
        ll = [ '↑', 'W', 'cima'  ]
        rr = [ '↓', 'S', 'baixo' ]

    info = [ [ name ],
             [ description ],
             [ '' ],
             [f'Mover para {ll[2]}',     f'{ll[0]}   ou   {ll[1]}' ],
             [f'Mover para {rr[2]}',     f'{rr[0]}   ou   {rr[1]}' ],
             [ 'Pausar e mostrar ajuda',  'F1,   H   ou   Espaço'  ],
             [ 'Alternar mudo',           'M'                      ],
             [ 'Alternar música',         'N'                      ],
             [ 'Ajustar volume',          '+  −'                   ],
             [ 'Sair',                    'Q   ou   Esc'           ] ]

    surf.fill( (40,40,40), None, pygame.BLEND_MULT )

    color = (255,255,255)

    font         = None
    font_size    = 40
    line_spacing = 2
    position     = (0,0)
    num_lines    = len(info)
    num_columns  = 2
    column_width = ['M'*15, 'M'*12]
    fgcolor      = (255,255,255)
    bgcolor      = None

    ost = OnScreenText(font,
                       font_size,
                       line_spacing,
                       position,
                       num_lines,
                       num_columns,
                       column_width,
                       fgcolor,
                       bgcolor)

    area = ost.area.copy()
    area.center = (gp.SCREEN_SIZE[0]//2, gp.SCREEN_SIZE[1]//2)

    ost.set_position(area.topleft)

    ost.draw(surf, info)         

#------------------------------------------------------------------------------#
