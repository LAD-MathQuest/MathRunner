#------------------------------------------------------------------------------#

import pygame

from game.onscreentext import OnScreenText

#------------------------------------------------------------------------------#
class Scoreboard:

    #--------------------------------------------------------------------------#
    def __init__(self, param):

        self.image      = param.image
        self.image_rect = param.image_rect

        self.text_rect    = param.text_rect
        self.text_bgcolor = param.text_bgcolor
        self.text_fgcolor = param.text_fgcolor

        self.ost = OnScreenText(self.text_rect, 3, 2, 
                                self.text_fgcolor, 
                                self.text_bgcolor)

        self.text_rect = self.ost.column_width(['Velocidade: ', '000000'])

    #--------------------------------------------------------------------------#
    def draw(self, surf, score, velocity, elapsed_time):

        surf.blit(self.image, self.image_rect)

        self.ost.draw( surf, 0, 0, 'Pontos:'     )
        self.ost.draw( surf, 1, 0, 'Velocidade:' )
        self.ost.draw( surf, 2, 0, 'Tempo:'      )

        self.ost.draw( surf, 0, 1, f'{score} ',            '>' )
        self.ost.draw( surf, 1, 1, f'{velocity:.2f} ',     '>' )
        self.ost.draw( surf, 2, 1, f'{elapsed_time:.2f} ', '>' )

#------------------------------------------------------------------------------#
