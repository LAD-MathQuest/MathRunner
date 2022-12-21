#------------------------------------------------------------------------------#

import pygame
import pygame.freetype

import game.game_params as gp

#------------------------------------------------------------------------------#
class OnScreenText:

    margin = lambda x: max( 1, int( 0.05 * x ) )

    #--------------------------------------------------------------------------#
    def __init__( self, area, n_lin, n_col, fgcolor, bgcolor ):

        self.fgcolor = fgcolor
        self.bgcolor = bgcolor

        self.area = area.copy()

        mx = -OnScreenText.margin( self.area.width  )
        my = -OnScreenText.margin( self.area.height )
        self.area.inflate_ip( mx, my )

        w = self.area.width  // n_col
        h = self.area.height // n_lin

        # TODO check if font exists
        self.font = pygame.freetype.SysFont( gp.FONT, int(0.9*h) )
        self.font.origin = True

        self.cell_w = [ w ] * n_col
        self.cell_h = h

        Xo = self.area.left
        Yo = self.area.top + self.font.get_sized_ascender() + int(0.05*h)

        self.cell_x = [ Xo + w * ii for ii in range(n_col) ]
        self.cell_y = [ Yo + h * ii for ii in range(n_lin) ]

    #--------------------------------------------------------------------------#
    def column_width( self, A, B=None ):

        W = lambda x: x if type(x) is int else self.font.get_rect(x).width

        if type(A) in [ list, tuple ]:
            for ii in range(len(self.cell_w)):
                self.cell_w[ii] = W(A[ii])
        else:
            self.cell_w[A] = W(B)

        for ii in range(1,len(self.cell_x)):
            self.cell_x[ii] = self.cell_x[ii-1] + self.cell_w[ii-1]
        
        w = sum(self.cell_w)
        self.area.width = w
        self.area.inflate_ip(OnScreenText.margin(w), 0)

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
