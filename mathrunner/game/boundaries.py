#------------------------------------------------------------------------------#

import pygame

import game.game_params as gp
import numpy as np

N_POINTS = 800

#------------------------------------------------------------------------------#
class Boundaries:

    #--------------------------------------------------------------------------#
    def __init__(self, function, vertical: bool):

        self.vertical  = vertical
        self.function  = function
        self.min_color = (0,0,0)
        self.max_color = (0,0,0)
        self.min_width = 3
        self.max_width = 3

        self.mask_surf = pygame.Surface(gp.SCREEN_SIZE, pygame.SRCALPHA)

        if vertical:

            direction = -1

            self.x_index = 1
            self.y_index = 0

            self.i_min_index = np.arange(1,            2*N_POINTS+1, 2)
            self.i_max_index = np.arange(2*N_POINTS+1, 4*N_POINTS,   2)
            self.j_min_index = np.arange(0,            2*N_POINTS,   2)
            self.j_max_index = np.arange(2*N_POINTS,   4*N_POINTS,   2)

            self.player_min_index = self.j_min_index[-26]
            self.player_max_index = self.j_max_index[ 25]

            self.spawn_min_index = self.j_min_index[ 10]
            self.spawn_max_index = self.j_max_index[-11]

        else:

            direction = 1

            self.x_index = 0
            self.y_index = 1

            self.i_min_index = np.arange(0,            2*N_POINTS,   2)
            self.i_max_index = np.arange(2*N_POINTS,   4*N_POINTS,   2)
            self.j_min_index = np.arange(1,            2*N_POINTS+1, 2)
            self.j_max_index = np.arange(2*N_POINTS+1, 4*N_POINTS,   2)

            self.player_min_index = self.j_min_index[ 50]
            self.player_max_index = self.j_max_index[-51]

            self.spawn_min_index = self.j_min_index[-6]
            self.spawn_max_index = self.j_max_index[ 5]

        self.x_scale = direction * 10.0 / gp.SCREEN_SIZE[self.x_index]
        self.y_scale = gp.SCREEN_SIZE[self.y_index] / 10.0

        self.x = np.linspace(0, 10, N_POINTS)

        self.polygon = np.zeros((2*N_POINTS, 2))
        self.ravpoly = self.polygon.ravel() 

        p = np.linspace(0, gp.SCREEN_SIZE[self.x_index], N_POINTS)
        self.ravpoly[self.i_min_index] = p
        self.ravpoly[self.i_max_index] = p[::-1]

        self.eval_polygon()
        
        self.first = True

    #--------------------------------------------------------------------------#
    def eval_polygon(self):

        y_min, y_max = self.function.eval(self.x)

        u_min = y_min * self.y_scale
        u_max = y_max * self.y_scale
        
        self.ravpoly[self.j_min_index] = u_min
        self.ravpoly[self.j_max_index] = u_max[::-1]

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        self.x += displacement * self.x_scale

        self.eval_polygon()

    #--------------------------------------------------------------------------#
    def mask(self):

        self.mask_surf.fill((0, 0, 0, 0))

        pygame.draw.polygon(self.mask_surf, (255, 255, 255, 255), self.polygon)

        return self.mask_surf

    #--------------------------------------------------------------------------#
    def draw_lines(self, surf):
        pygame.draw.lines(surf, self.min_color, False, self.polygon[0:N_POINTS,:], self.min_width)
        pygame.draw.lines(surf, self.max_color, False, self.polygon[N_POINTS: ,:], self.max_width)

    #--------------------------------------------------------------------------#
    def player(self):
        return (
            int(self.ravpoly[self.player_min_index]),
            int(self.ravpoly[self.player_max_index])
        )

    #--------------------------------------------------------------------------#
    def spawn(self):
        return (
            int(self.ravpoly[self.spawn_min_index]),
            int(self.ravpoly[self.spawn_max_index])
        )

#------------------------------------------------------------------------------#
