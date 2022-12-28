#------------------------------------------------------------------------------#

import pygame
import pygame.freetype

import game.game_params as gp

#------------------------------------------------------------------------------#
class OnScreenText:
    '''Encapsulates on screen text actions'''

    #--------------------------------------------------------------------------#
    def __init__(self, 
                 font    = None, 
                 area    = pygame.Rect((0,0), gp.SCREEN_SIZE), 
                 n_lin   = 1, 
                 n_col   = 1, 
                 fgcolor = (255,255,255), 
                 bgcolor = (0,0,0)):

        self.fgcolor = fgcolor
        self.bgcolor = bgcolor

        self.area = area.copy()

        w = self.area.width  // n_col
        h = self.area.height // n_lin

        if not font:
            font = gp.DEFAULT_FONT

        self.font = pygame.freetype.Font(font, int(0.9*h))

        self.font.origin = True

        self.cell_w = [ w ] * n_col
        self.cell_h = h

        Xo = self.area.left
        Yo = self.area.top + self.font.get_sized_ascender() + int(0.05*h)

        self.cell_x = [ Xo + w * ii for ii in range(n_col) ]
        self.cell_y = [ Yo + h * ii for ii in range(n_lin) ]

    #--------------------------------------------------------------------------#
    def column_width( self, A, B=None ):
        '''Set column widths.

        Parameters can be:
        - A list of widths
        - A pair of column index and width

        Widths can be an integer os a string
        '''

        str_width = lambda x: x if type(x) is int else self.font.get_rect(x).width

        if type(A) in (list, tuple):
            for ii, aa in enumerate(A):
                self.cell_w[ii] = str_width(aa)
        else:
            self.cell_w[A] = str_width(B)

        for ii in range(1,len(self.cell_x)):
            self.cell_x[ii] = self.cell_x[ii-1] + self.cell_w[ii-1]
        
        ww = sum(self.cell_w)
        self.area.width = ww

        return self.area

    #--------------------------------------------------------------------------#
    def draw( self, surf, ii, jj, content, align='<' ):

        x = self.cell_x[jj]
        y = self.cell_y[ii]

        if align != '<':

            text_w = self.font.get_rect( content ).width

            if align == '>':
                x +=  self.cell_w[jj] - text_w
            elif align == '^':
                x += (self.cell_w[jj] - text_w ) // 2
            else:
                raise TypeError(f'Unknown alignment option: {align}')

        self.font.render_to( surf, (x,y), content, self.fgcolor, self.bgcolor )

#------------------------------------------------------------------------------#
