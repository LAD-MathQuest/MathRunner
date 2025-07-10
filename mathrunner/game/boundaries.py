#------------------------------------------------------------------------------#

import pygame

import game.game_params as gp
import numpy as np

N_POINTS = 400

#------------------------------------------------------------------------------#
class Boundaries:

    #--------------------------------------------------------------------------#
    def __init__(self, function, vertical: bool):

        self.vertical = vertical
        self.function = function
        self.mask = pygame.Surface(gp.SCREEN_SIZE, pygame.SRCALPHA)

        if vertical:
            self.player_index = -1
            self.spawn_index  =  0

            self.x_index = 1
            self.y_index = 0

            direction = -1

        else:
            self.player_index =  0
            self.spawn_index  = -1

            self.x_index = 0
            self.y_index = 1

            direction = 1

        self.x_scale = direction * 10.0 / gp.SCREEN_SIZE[self.x_index]
        self.y_scale = gp.SCREEN_SIZE[self.y_index] / 10.0

        self.x = np.linspace(0, 10, N_POINTS)
        self.p = np.linspace(0, gp.SCREEN_SIZE[self.x_index], N_POINTS)

        self.eval_polygon()

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        self.x += displacement * self.x_scale

        self.eval_polygon()

    #--------------------------------------------------------------------------#
    def get_mask(self):

        self.mask.fill((0, 0, 0, 0))

        pygame.draw.polygon(self.mask, (255, 255, 255, 255), self.polygon)

        return self.mask

    #--------------------------------------------------------------------------#
    def player(self):
        return (
            int(self.p_min[self.player_index]),
            int(self.p_max[self.player_index])
        )

    #--------------------------------------------------------------------------#
    def spawn(self):
        return (
            int(self.p_min[self.spawn_index]),
            int(self.p_max[self.spawn_index])
        )

    #--------------------------------------------------------------------------#
    def eval_polygon(self):

        y_min, y_max = self.function.eval(self.x)

        self.p_min = y_min * self.y_scale
        self.p_max = y_max * self.y_scale

        if self.vertical:
            p_top    = list(zip(self.p_max, self.p))
            p_bottom = list(zip(self.p_min, self.p))
        else:
            p_top    = list(zip(self.p, self.p_max))
            p_bottom = list(zip(self.p, self.p_min))

        self.polygon = p_top + p_bottom[::-1]

#------------------------------------------------------------------------------#

