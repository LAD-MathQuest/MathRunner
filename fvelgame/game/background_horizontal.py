#------------------------------------------------------------------------------#

import pygame
import math

import game.game_params as gp

#------------------------------------------------------------------------------#
def surface_tiling(surf, tile):

    t_width  = tile.get_width ()
    t_height = tile.get_height()

    s_width  = surf.get_width ()
    s_height = surf.get_height()

    rect = pygame.Rect((0,0), (t_width,t_height))


    step_x = t_width
    step_y = t_height

    nh = math.ceil(s_height / t_height)
    nw = math.ceil(s_width  / t_width )

    rr = rect.copy()

    for ii in range(nh):
        for jj in range(nw):
            surf.blit(tile, rr)
            rr.move_ip(step_x, 0)

        rr.left = rect.left
        rr.move_ip(0, step_y)

#------------------------------------------------------------------------------#
def fit_image_to_screen(image):

    im_width  = image.get_width ()
    im_height = image.get_height()

    sc_width  = gp.SCREEN_SIZE[0]
    sc_height = gp.SCREEN_SIZE[1]

    new_image = pygame.Surface(gp.SCREEN_SIZE)

    if im_width < sc_width or im_height < sc_height:
        surface_tiling(new_image, image)

    else: # Image has same size or is larger than screen

        rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

        new_image.blit(image, (0,0), rect)

    return new_image

#------------------------------------------------------------------------------#
class BackgroundHorizontal:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world    = world
        self.boundary = world.boundary

        self.bg_scrolls = world.background_scrolls

        if self.bg_scrolls:
            self.set_background_scrolling()
        else:
            self.bg_image     = fit_image_to_screen(world.background_image)
            self.bg_show_rect = None

        # Initializing track

        self.tr_image   = world.track_image
        self.tr_scrolls = world.track_scrolls

        tr_min, lenght = self.boundary.eval_length(0)

        top    = int(gp.SCREEN_SIZE[1] * tr_min)
        height = int(gp.SCREEN_SIZE[1] * lenght)
        self.tr_rect = pygame.Rect(0, top, gp.SCREEN_SIZE[0], height)

        if self.tr_image:
            self.bg_image.blit(self.tr_image, self.tr_rect, self.tr_rect)

    #--------------------------------------------------------------------------#
    def set_background_scrolling(self):

        w_image  = self.world.background_image
        w_width  = w_image.get_width ()
        w_height = w_image.get_height()

        s_width  = gp.SCREEN_SIZE[0]
        s_height = gp.SCREEN_SIZE[1]

        if w_width < s_width or w_height < s_height:

            n_width = math.ceil(s_width / w_width) * w_width
            n_image = pygame.Surface((n_width, s_height))

            surface_tiling(n_image, w_image)

            w_image  = n_image
            w_width  = n_width
            w_height = s_height

        self.bg_max_width = w_width + s_width
        self.bg_image     = pygame.Surface((self.bg_max_width, s_height))

        self.bg_image.blit(w_image, (0,0))
        self.bg_image.blit(w_image, (w_width,0), (0,0,s_width,s_height) )

        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)
        self.bg_scrolls   = self.world.background_scrolls

        if not self.bg_scrolls:
            self.bg_image     = self.world.background_image
            self.bg_show_rect = None
            return

        w_bg_image  = self.world.background_image
        w_bg_width  = w_bg_image.get_width ()
        w_bg_height = w_bg_image.get_height()

        sc_width  = gp.SCREEN_SIZE[0]
        sc_height = gp.SCREEN_SIZE[1]

        self.bg_max_width = w_bg_width + sc_width
        self.bg_image     = pygame.Surface((self.bg_max_width, sc_height))

        self.bg_image.blit(w_bg_image, (0,0))
        self.bg_image.blit(w_bg_image, (sc_width+1,0), (0,0,sc_width,sc_height) )

        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        if not self.bg_scrolls: return

        self.bg_show_rect.right += displacement

        if self.bg_show_rect.right > self.bg_max_width:
            self.bg_show_rect.right += gp.SCREEN_SIZE[0] - self.bg_max_width

    #--------------------------------------------------------------------------#
    def draw(self, surf):
        surf.blit(self.bg_image, (0,0), self.bg_show_rect)

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):
        return [self.tr_rect.top, self.tr_rect.bottom]

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):
        return [self.tr_rect.top, self.tr_rect.bottom]

#------------------------------------------------------------------------------#
