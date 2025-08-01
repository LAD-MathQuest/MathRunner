#------------------------------------------------------------------------------#
'''Describes the game scoreboard'''

from .meta_image import MetaImage

#------------------------------------------------------------------------------#
class MetaScoreboard:

    #--------------------------------------------------------------------------#
    def __init__(
            self,
            title: str | None   = None,
            text_font           = None,
            text_font_size: int = 32,
            text_spacing: float = 1.5,
            text_position       = (100,100),
            text_bgcolor        = None,
            text_fgcolor        = (255,255,255),
            show_points         = True,
            show_velocity       = True,
            show_time           = True,
            image: MetaImage    = None,
            image_position      = None
        ) -> None:

        self.title  = title

        self.text_font      = text_font
        self.text_font_size = text_font_size
        self.text_spacing   = text_spacing
        self.text_position  = text_position
        self.text_bgcolor   = text_bgcolor
        self.text_fgcolor   = text_fgcolor

        self.show_points   = show_points
        self.show_velocity = show_velocity
        self.show_time     = show_time

        self.image          = image
        self.image_position = text_position if not image_position else image_position

#------------------------------------------------------------------------------#

