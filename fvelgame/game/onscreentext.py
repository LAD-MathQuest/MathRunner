#------------------------------------------------------------------------------#

import pygame
import pygame.freetype

import game.game_params as gp

#------------------------------------------------------------------------------#
def eval_width(font, span, num_columns=1):
    '''Eval column widths

    Args:
        span(int) :    Width value in pixels for all columns
        span(string) : Template string
        span(list) :   List or tuple of ints and/or strings
    '''

    get_width = lambda ss : ss if type(ss) is int else font.get_rect(ss).width

    if type(span) in (list, tuple):

        widths = [0]*num_columns
        
        for ii, ss in enumerate(span):
            widths[ii] = get_width(ss)

    else:
        widths = [get_width(span)]*num_columns

    return widths

#------------------------------------------------------------------------------#
class OnScreenText:
    '''Encapsulates on screen text actions

    Attributes:
        position (int,int): Read only, top left position
        width (int):        Read only, total width
        height (int):       Read only, total height
        size (int,int):     Read only, total size
        area (Rect):        Read only, rectangle with the text area
    '''

    #--------------------------------------------------------------------------#
    def __init__(self, 
                 font         = None,
                 font_size    = 22,
                 line_spacing = 1.5,
                 position     = (0,0),
                 num_lines    = 1, 
                 num_columns  = 1, 
                 column_width = 100,
                 fgcolor      = (255,255,255),
                 bgcolor      = (0,0,0)):
        '''Create an OnScreenText that can draw a text table on a surface

        Args:
            font (path):           Font path, if None uses default font
            font_size (int):       Font size (default is 22)
            line_spacing (float):  Line spacing, proportional to font height (default is 1.5)
            position (int,int):    Position of left top table corner
            num_lines (int):       Number of lines   (default is 1)
            num_columns (int):     Number of columns (default is 1)
            column_width:          Column width information (default is 100)
                                   It can be a list of integers or strings.
                                   A integer is interpreted as number of pixels.
                                   If a string is provided its width is computed and used
                                   as column width.
            fgcolor (int,int,int): Foreground color
            bgcolor (int,int,int): Background color
        '''

        self.fgcolor = fgcolor
        self.bgcolor = bgcolor

        self.position = position

        if not font:
            font = gp.DEFAULT_FONT

        self.font        = pygame.freetype.Font(font, font_size)
        self.font.origin = True
        self.font.pad    = True

        # Computing cell origin X position

        self.num_columns = num_columns

        self.cell_w = eval_width(self.font, column_width, num_columns)
        self.cell_x = [0] * (num_columns+1)

        for ii in range(num_columns):
            self.cell_x[ii+1] = self.cell_x[ii] + self.cell_w[ii]

        self.width = self.cell_x[-1]

        # Computing cell origin Y position

        ascender  = self.font.get_sized_ascender()
        height    = self.font.get_sized_height  ()
        line_skip = line_spacing * height

        self.cell_y = [ ascender + line_skip * ii for ii in range(num_lines) ]
        self.height = self.cell_y[-1] - self.font.get_sized_descender() +1

        # Text size and area

        self.size = (self.width, self.height)
        self.area = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def set_position(self, position):
        '''Update position

            Args:
                position (int,int): Position of left top table corner
        '''

        self.position = position
        self.area     = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def set_column_widths(self, column_widths):
        '''Set width fot all columns

        Args:
        '''

        self.cell_w = eval_width(self.font, column_widths, self.num_columns)

        for ii in range(self.num_columns):
            self.cell_x[ii+1] = self.cell_x[ii] + self.cell_w[ii]

        self.width = self.cell_x[-1]
        self.size  = (self.width, self.height)
        self.area  = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def set_column_width(self, jj, column_width):
        '''Set width of column jj

        Args:
            ii (int) :          Column index
            span (int ou str) : Width in pixels or fitting string 
        '''

        self.cell_w[jj] = eval_width(self.font, column_widths)[0]

        for ii in range(jj,self.num_columns):
            self.cell_x[ii+1] = self.cell_x[ii] + self.cell_w[ii]

        self.width = self.cell_x[-1]
        self.size  = (self.width, self.height)
        self.area  = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def draw_cell(self, surf, ii, jj, content, align='<'):

        xx = (self.cell_x[jj]) + (self.position[0])
        yy = (self.cell_y[ii]) + (self.position[1])

        if align != '<':

            text_w = self.font.get_rect(content).width

            if align == '>':
                xx += self.cell_w[jj] - text_w

            elif align == '^':
                xx += (self.cell_w[jj] - text_w) // 2

            else:
                raise TypeError(f'Unknown alignment option: {align}')

        self.font.render_to( surf, (xx,yy), content, self.fgcolor, self.bgcolor )

    #--------------------------------------------------------------------------#
    def draw( self, surf, content, align='<' ):

        nn = len(align)

        for ii, line in enumerate(content):
            for jj, cell in enumerate(line):
                cell_align = align[-1] if jj >= nn else align[jj]
                self.draw_cell(surf, ii, jj, cell, cell_align)

#------------------------------------------------------------------------------#
