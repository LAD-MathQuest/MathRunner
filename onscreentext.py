#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
import pygame
import pygame.freetype

#------------------------------------------------------------------------------#
class OnScreenText:

    margin = lambda x: max( 1, int( 0.05 * x ) )

    #--------------------------------------------------------------------------#
    def __init__( self, area, n_lin, n_col, fgcolor, bgcolor ):

        self.fgcolor = fgcolor
        self.bgcolor = bgcolor

        self.area   = area.copy()

        mx = -OnScreenText.margin( area.width  )
        my = -OnScreenText.margin( area.height )
        area.inflate_ip( mx, my )

        w = area.width  // n_col
        h = area.height // n_lin

        self.font = pygame.freetype.Font( None, int(0.9*h) )
        self.font.origin = True

        self.cell_w = [ w ] * n_col
        self.cell_h = h

        Xo = area.left
        Yo = area.top + self.font.get_sized_ascender() + int(0.05*h)

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
        self.area.width = w + OnScreenText.margin(w)

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
