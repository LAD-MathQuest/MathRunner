#------------------------------------------------------------------------------#

import pygame

import game.game_params as gp
import numpy as np

from game.tools      import surface_tile_to_size
from scrolling_image import ScrollingImage
from boundaries      import Boundaries

#------------------------------------------------------------------------------#
class BackgroundHorizontal:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.background = ScrollingImage(world.background_image, world.background_scrolls)

        self.boundaries = Boundaries(world.boundary)

        self.draw_track = bool(world.track_image)

        if self.draw_track:
            self.track = ScrollingImage(world.track_image, world.track_scrolls)

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        self.background.update(displacement)
        self.boundaries.update(displacement)

        if self.draw_track:
            self.track.update(displacement)

    #--------------------------------------------------------------------------#
    def draw(self, surf):

        self.background.draw(surf)

        if self.draw_track:
            self.track.draw_with_mask(surf, self.boundaries.get_mask())

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):
        return self.boundaries.player()

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):
        return self.boundaries.spawn()

#------------------------------------------------------------------------------#
