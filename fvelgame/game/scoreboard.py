#------------------------------------------------------------------------------#

import pygame

from game.onscreentext import OnScreenText

#------------------------------------------------------------------------------#
class Scoreboard:

    #--------------------------------------------------------------------------#
    def __init__(self, param):

        self.title = param.title

        self.text_font      = param.text_font
        self.text_font_size = param.text_font_size
        self.text_spacing   = param.text_spacing
        self.text_position  = param.text_position
        self.text_bgcolor   = param.text_bgcolor
        self.text_fgcolor   = param.text_fgcolor

        self.show_points   = param.show_points  
        self.show_velocity = param.show_velocity
        self.show_time     = param.show_time    

        self.draw_image = param.draw_image
        self.image      = param.image
        self.image_rect = param.image_rect

        text_rect = pygame.Rect( self.text_position, (100,100))

        n_lin = 3
        n_col = 2

        self.ost = OnScreenText(self.text_font,
                                self.text_font_size,
                                self.text_spacing,
                                self.text_position,
                                n_lin, 
                                n_col, 
                                ['Velocidade: ', '000000'],
                                self.text_fgcolor, 
                                self.text_bgcolor)

        self.text_rect = pygame.Rect(self.text_position, self.ost.size)

    #--------------------------------------------------------------------------#
    def draw(self, surf, score, velocity, elapsed_time):

        if self.draw_image:
            surf.blit(self.image, self.image_rect)

        self.ost.draw_cell( surf, 0, 0, 'Pontos:'     )
        self.ost.draw_cell( surf, 1, 0, 'Velocidade:' )
        self.ost.draw_cell( surf, 2, 0, 'Tempo:'      )

        self.ost.draw_cell( surf, 0, 1, f'{score} ',            '>' )
        self.ost.draw_cell( surf, 1, 1, f'{velocity:.2f} ',     '>' )
        self.ost.draw_cell( surf, 2, 1, f'{elapsed_time:.2f} ', '>' )

#------------------------------------------------------------------------------#
