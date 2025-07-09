#------------------------------------------------------------------------------#

import pygame

import game.game_params as gp
import numpy as np

#------------------------------------------------------------------------------#
class Boundaries:

    #--------------------------------------------------------------------------#
    def __init__(self, boundary):

        self.boundary = boundary
        self.mask = pygame.Surface(gp.SCREEN_SIZE, pygame.SRCALPHA)

        n_points = 600

        self.x_scale = 10.0 / gp.SCREEN_SIZE[0]
        self.y_scale = gp.SCREEN_SIZE[1] / 10.0

        self.x = np.linspace(0,   10, n_points)
        self.p = np.linspace(0, 1920, n_points)

        self.eval_polygon()

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        self.x += displacement * self.x_scale

        self.eval_polygon()

    #--------------------------------------------------------------------------#
    def eval_polygon(self):

        y_min, y_max = self.boundary.eval(self.x)

        self.p_min = (y_min * self.y_scale).astype(int)
        self.p_max = (y_max * self.y_scale).astype(int)

        p_top    = list(zip(self.p, self.p_max))
        p_bottom = list(zip(self.p, self.p_min))

        self.polygon = p_top + p_bottom[::-1]

    #--------------------------------------------------------------------------#
    def get_mask(self):

        self.mask.fill((0, 0, 0, 0))

        pygame.draw.polygon(self.mask, (255, 255, 255, 255), self.polygon)

        return self.mask

    #--------------------------------------------------------------------------#
    def player(self):
        return (self.p_min[0], self.p_max[0])

    #--------------------------------------------------------------------------#
    def spawn(self):
        return (self.p_min[-1], self.p_max[-1])


#------------------------------------------------------------------------------#
