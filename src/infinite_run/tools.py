#------------------------------------------------------------------------------#

import pygame
import math

#------------------------------------------------------------------------------#
def surface_tile_to_size(image, new_size, start_at_bottom=False):

    old_width  = image.get_width ()
    old_height = image.get_height()

    new_image  = pygame.Surface(new_size)
    new_width  = new_size[0]
    new_height = new_size[1]

    # If the original image size is equal or larger than the required new size

    if old_width >= new_width and old_height >= new_height:

        rect = pygame.Rect((0,0), new_size)

        if start_at_bottom:
             rect.bottom = old_height

        new_image.blit(image, (0,0), rect)

        return new_image

    # If the original image size smaller than the required new size

    rect   = pygame.Rect((0,0), (old_width,old_height))
    step_y = old_height

    if start_at_bottom:
        rect.bottom =  new_height
        step_y      = -old_height

    nw = math.ceil(new_width  / old_width )
    nh = math.ceil(new_height / old_height)

    for ii in range(nh):
        for jj in range(nw):
            new_image.blit(image, rect)
            rect.move_ip(old_width, 0)

        rect.left = 0
        rect.move_ip(0, step_y)

    return new_image

#------------------------------------------------------------------------------#
