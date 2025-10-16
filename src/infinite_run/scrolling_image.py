#------------------------------------------------------------------------------#

import pygame

from .      import parameters as gp
from .tools import surface_tile_to_size

#------------------------------------------------------------------------------#
class ScrollingImage:

    #--------------------------------------------------------------------------#
    def __init__(self, image, scrolls: bool, vertical: bool):

        self.not_scrolls = not scrolls
        self.vertical    = vertical

        new_size = list(gp.SCREEN_SIZE)

        if scrolls:
            if vertical:
                new_size[1]   += image.get_height()
                self.top_start = image.get_height()
            else:
                new_size[0]   += image.get_width()
                self.max_width = new_size[0]

        self.image = surface_tile_to_size(image, new_size, vertical)
        self.aux   = pygame.Surface(gp.SCREEN_SIZE, pygame.SRCALPHA)

        self.show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        if self.not_scrolls:
            return

        if self.vertical:
            self.show_rect.top -= displacement
            if self.show_rect.top < 0:
                self.show_rect.top = self.top_start + self.show_rect.top

        else:
            self.show_rect.right += displacement
            if self.show_rect.right > self.max_width:
                self.show_rect.right += gp.SCREEN_SIZE[0] - self.max_width

    #--------------------------------------------------------------------------#
    def draw(self, surf):
        surf.blit(self.image, (0,0), self.show_rect)

    #--------------------------------------------------------------------------#
    def draw_with_mask(self, surf, mask):

        self.aux.blit(self.image, (0,0), self.show_rect)
        self.aux.blit(mask, (0,0), None, pygame.BLEND_RGBA_MULT)

        surf.blit(self.aux, (0,0))

#------------------------------------------------------------------------------#


















