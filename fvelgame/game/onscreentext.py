#------------------------------------------------------------------------------#

import pygame
import pygame.freetype

import game.game_params as gp

#------------------------------------------------------------------------------#
class OnScreenText:
    '''Encapsulates on screen text actions'''

    #--------------------------------------------------------------------------#
    def Table(*args, **kwargs):
        return OnScreenText_Table(*args, **kwargs)

    #--------------------------------------------------------------------------#
    def Paragraph(*args, **kwargs):
        return OnScreenText_Paragraph(*args, **kwargs)

#------------------------------------------------------------------------------#
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

    if len(widths) ==1:
        return widths[0]
    else:
        return widths


#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
class OnScreenText_Table:
    '''Creates a table to organize text on screen

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
        '''Create an object that can draw a text table on a surface

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
        '''Update table position

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

        self.cell_w[jj] = eval_width(self.font, column_widths)

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
#------------------------------------------------------------------------------#
class OnScreenText_Paragraph:
    '''Creates a text paragraph

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
                 width        = 100,
                 fgcolor      = (255,255,255),
                 bgcolor      = (0,0,0)):
        '''Create an object that can draw a text paragraph on a surface

        Args:
            font (path):           Font path, if None uses default font
            font_size (int):       Font size (default is 22)
            line_spacing (float):  Line spacing, proportional to font height (default is 1.5)
            position (int,int):    Position of left top paragraph corner
            width (int or str):    Column width information (default is 100)
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

        self.width = eval_width(self.font, width)

        # Computing first line origin Y and line skip

        self.first_line_y = self.font.get_sized_ascender()
        self.line_skip    = line_spacing * self.font.get_sized_height()
        self.descender    = 1 - self.font.get_sized_descender() 
        self.last_line    = 0

        self.height = self.first_line_y + self.descender

        # Text size and area

        self.size = (self.width, self.height)
        self.area = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def set_position(self, position):
        '''Update paragraph position

            Args:
                position (int,int): Position of left top corner
        '''

        self.position = position
        self.area     = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def set_width(self, width):
        '''Set new paragraph width'''

        self.width = eval_width(self.font, width)
        self.size  = (self.width, self.height)
        self.area  = pygame.Rect( self.position, self.size)

    #--------------------------------------------------------------------------#
    def _draw_line(self, surf, content, ii, align):

        xx = self.position[0] 
        yy = self.position[1] + self.first_line_y + ii*self.line_skip

        if align != '<':

            text_w = self.font.get_rect(content).width

            if align == '>':
                xx += self.width - text_w

            elif align == '^':
                xx += (self.width - text_w) // 2

            else:
                raise TypeError(f'Unknown alignment option: {align}')

        self.font.render_to( surf, (xx,yy), content, self.fgcolor, self.bgcolor )

        return ii+1

    #--------------------------------------------------------------------------#
    def _draw_str(self, surf, content, ii, align):

        text_w = self.font.get_rect(content).width
        
        if text_w <= self.width:
            ii = self._draw_line(surf, content, ii, align)
            return ii

        words  = content.split()
        word_w = [ self.font.get_rect(ww).width for ww in words ]

        # Last drawed word
        nn = 0

        while nn < len(words):

            line_width = 0
            jj = nn

            while line_width < self.width and jj < len(words):
                line_width += word_w[jj]
                jj += 1

            if  jj < len(words):
                jj -= 1
                
            line_str = ' '.join(words[nn:jj])
            nn = jj

            ii = self._draw_line(surf, line_str, ii, align)

        return ii

    #--------------------------------------------------------------------------#
    def _draw_full_str(self, surf, content, ii, align):

        if not '\n' in content:
            ii = self._draw_str(surf, content, ii, align)

        else:
            for cc in content.splitlines():
                ii = self._draw_str(surf, cc, ii, align)

        return ii

    #--------------------------------------------------------------------------#
    def draw(self, surf, content, line=None, align='<'):
        
        ii = self.last_line if not line else line

        if type(content) in (list, tuple):
            for cc in content:
                ii = self._draw_full_str(surf, cc, ii, align)

        else:
            ii = self._draw_full_str(surf, content, ii, align)

        if ii > self.last_line:
            self.last_line = ii
            self.height    = self.first_line_y + self.last_line*self.line_skip + self.descender
            self.size      = (self.width, self.height)
            self.area      = pygame.Rect( self.position, self.size)

#------------------------------------------------------------------------------#
