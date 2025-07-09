#------------------------------------------------------------------------------#

import pygame
import math

import game.game_params as gp

from game.tools import surface_tile_to_size

#------------------------------------------------------------------------------#
class BackgroundVertical:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world    = world
        self.boundary = world.boundary

        self.bg_scrolls = world.background_scrolls
        self.tr_scrolls = world.track_scrolls

        # Background initialization

        image  = self.world.background_image
        height = image.get_height()

        new_size = list(gp.SCREEN_SIZE)

        if self.bg_scrolls:
            new_size[1] += height

        self.bg_image     = surface_tile_to_size(image, new_size, True)
        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
        self.bg_top_start = height

        # Initializing track

        self.draw_track = bool(world.track_image)

        if self.draw_track:

            image  = self.world.track_image
            height = image.get_height()

            new_size = list(gp.SCREEN_SIZE)

            if self.tr_scrolls:
                new_size[1] += height

            self.tr_image     = surface_tile_to_size(image, new_size, True)
            self.tr_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
            self.tr_top_start = height

        # Initializing boundary

        tr_min, lenght = self.boundary.eval_length(0)

        left  = int(gp.SCREEN_SIZE[0] * tr_min/10.0)
        width = int(gp.SCREEN_SIZE[0] * lenght/10.0)

        self.bd_rect = pygame.Rect(left, 0, width, gp.SCREEN_SIZE[1])

        if self.draw_track:
            self.tr_show_rect.left  = left
            self.tr_show_rect.width = width

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        if self.bg_scrolls:
            self.bg_show_rect.top -= displacement
            if self.bg_show_rect.top < 0:
                self.bg_show_rect.top = self.bg_top_start + self.bg_show_rect.top

        if self.tr_scrolls:
            self.tr_show_rect.top -= displacement
            if self.tr_show_rect.top < 0:
                self.tr_show_rect.top = self.tr_top_start + self.tr_show_rect.top

    #--------------------------------------------------------------------------#
    def draw(self, surf):

        surf.blit(self.bg_image, (0,0), self.bg_show_rect)

        if self.draw_track:
            surf.blit(self.tr_image, self.bd_rect, self.tr_show_rect)

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):
        return [self.bd_rect.left, self.bd_rect.right]

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):
        return [self.bd_rect.left, self.bd_rect.right]

#------------------------------------------------------------------------------#
