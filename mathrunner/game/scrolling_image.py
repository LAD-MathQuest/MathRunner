#------------------------------------------------------------------------------#

import pygame
import game.game_params as gp

from game.tools import surface_tile_to_size

#------------------------------------------------------------------------------#
class ScrollingImage:

    #--------------------------------------------------------------------------#
    def __init__(self, image, scrolls: bool):

        self.scrolls = scrolls

        width = image.get_width()

        new_size = list(gp.SCREEN_SIZE)

        if self.scrolls:
            new_size[0] += width

        self.image     = surface_tile_to_size(image, new_size)
        self.show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
        self.max_width = new_size[0]

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        if not self.scrolls: return

        self.show_rect.right += displacement

        if self.show_rect.right > self.max_width:
            self.show_rect.right += gp.SCREEN_SIZE[0] - self.max_width

    #--------------------------------------------------------------------------#
    def draw(self, surf):

        surf.blit(self.image, (0,0), self.show_rect)

    #--------------------------------------------------------------------------#
    def draw_with_mask(self, surf, mask):

        aux = pygame.Surface(gp.SCREEN_SIZE, pygame.SRCALPHA)
        aux.blit(self.image, (0,0), self.show_rect)
        aux.blit(mask, (0,0), None, pygame.BLEND_RGBA_MULT)

        surf.blit(aux, (0,0))

#------------------------------------------------------------------------------#
