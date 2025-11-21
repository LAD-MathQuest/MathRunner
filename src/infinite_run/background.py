#------------------------------------------------------------------------------#

from .scrolling_image import ScrollingImage
from .boundaries      import Boundaries

#------------------------------------------------------------------------------#
class Background:

    #--------------------------------------------------------------------------#
    def __init__(self, world, vertical: bool):

        self.background = ScrollingImage(
            world.background_image,
            world.background_scrolls,
            vertical
        )

        self.draw_boundary = bool(world.boundary_image)

        if self.draw_boundary:
            self.boundary = ScrollingImage(
                world.boundary_image,
                world.boundary_scrolls,
                vertical
            )

        self.min_color = world.min_color
        self.max_color = world.max_color
        self.min_width = world.min_width
        self.max_width = world.max_width

        self.boundaries = Boundaries(world.boundary, vertical)

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        self.background.update(displacement)
        self.boundaries.update(displacement)

        if self.draw_boundary:
            self.boundary.update(displacement)

    #--------------------------------------------------------------------------#
    def draw(self, surf):

        self.background.draw(surf)

        if self.draw_boundary:
            self.boundary.draw_with_mask(surf, self.boundaries.mask())

        if self.min_color: 
            self.boundaries.draw_min_line(
                surf, 
                self.min_color, 
                self.min_width
            )

        if self.max_color: 
            self.boundaries.draw_max_line(
                surf, 
                self.max_color, 
                self.max_width
            )

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):
        return self.boundaries.player()

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):
        return self.boundaries.spawn()

#------------------------------------------------------------------------------#
