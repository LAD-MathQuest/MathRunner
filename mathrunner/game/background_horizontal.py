#------------------------------------------------------------------------------#

import pygame
import math

import game.game_params as gp

from game.tools import surface_tile_to_size

#------------------------------------------------------------------------------#
class BackgroundHorizontal:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world    = world
        self.boundary = world.boundary

        self.bg_scrolls = world.background_scrolls
        self.tr_scrolls = world.track_scrolls

        # Background initialization

        image = self.world.background_image
        width = image.get_width()

        new_size = list(gp.SCREEN_SIZE)

        if self.bg_scrolls:
            new_size[0] += width

        self.bg_image     = surface_tile_to_size(image, new_size)
        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
        self.bg_max_width = new_size[0]

        # Initializing track

        self.draw_track = bool(world.track_image)

        if self.draw_track:

            image = self.world.track_image
            width = image.get_width()

            new_size = list(gp.SCREEN_SIZE)

            if self.tr_scrolls:
                new_size[0] += width

            self.tr_image     = surface_tile_to_size(image, new_size)
            self.tr_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
            self.tr_max_width = new_size[0]

        # Initializing boundary

        tr_min, lenght = self.boundary.eval_length(0)

        top    = int(gp.SCREEN_SIZE[1] * tr_min)
        height = int(gp.SCREEN_SIZE[1] * lenght)

        self.bd_rect = pygame.Rect(0, top, gp.SCREEN_SIZE[0], height)

        if self.draw_track:
            self.tr_show_rect.top    = top
            self.tr_show_rect.height = height

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        if self.bg_scrolls:
            self.bg_show_rect.right += displacement
            if self.bg_show_rect.right > self.bg_max_width:
                self.bg_show_rect.right += gp.SCREEN_SIZE[0] - self.bg_max_width

        if self.tr_scrolls:
            self.tr_show_rect.right += displacement
            if self.tr_show_rect.right > self.tr_max_width:
                self.tr_show_rect.right += gp.SCREEN_SIZE[0] - self.tr_max_width

    #--------------------------------------------------------------------------#
    def draw(self, surf):

        surf.blit(self.bg_image, (0,0), self.bg_show_rect)

        if self.draw_track:
            surf.blit(self.tr_image, self.bd_rect, self.tr_show_rect)

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):
        return [self.bd_rect.top, self.bd_rect.bottom]

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):
        return [self.bd_rect.top, self.bd_rect.bottom]

#------------------------------------------------------------------------------#
