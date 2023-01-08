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
    rect.bottom = s_height

    step_x =  t_width
    step_y = -t_height

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
        rect.bottom = im_height
        new_image.blit(image, (0,0), rect)

    return new_image

#------------------------------------------------------------------------------#
class BackgroundVertical:

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

        left  = int(gp.SCREEN_SIZE[0] * tr_min)
        width = int(gp.SCREEN_SIZE[0] * lenght)
        self.tr_rect = pygame.Rect(left, 0, width, gp.SCREEN_SIZE[1])

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

            n_height = math.ceil(s_height / w_height) * w_height
            n_image  = pygame.Surface((s_width, n_height))

            surface_tiling(n_image, w_image)

            w_image  = n_image
            w_width  = s_width
            w_height = n_height

        self.bg_top_start = w_height
        self.bg_image     = pygame.Surface((s_width, w_height+s_height))

        self.bg_image.blit(w_image, (0,s_height))
        self.bg_image.blit(w_image, (0,0), (0,w_height-s_height,s_width,s_height) )

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

        self.bg_top_start = w_bg_height
        self.bg_image     = pygame.Surface((sc_width, w_bg_height+sc_height))

        self.bg_image.blit(w_bg_image, (0,sc_height))
        self.bg_image.blit(w_bg_image, (0,0), (0,w_bg_height-sc_height,sc_width,sc_height) )

        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

    #--------------------------------------------------------------------------#
    def update(self, displacement):

        if not self.bg_scrolls: return

        self.bg_show_rect.top -= displacement

        if self.bg_show_rect.top < 0:
            self.bg_show_rect.top = self.bg_top_start + self.bg_show_rect.top

    #--------------------------------------------------------------------------#
    def draw(self, surf):
        surf.blit(self.bg_image, (0,0), self.bg_show_rect)

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):
        return [self.tr_rect.left, self.tr_rect.right]

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):
        return [self.tr_rect.left, self.tr_rect.right]

#------------------------------------------------------------------------------#
