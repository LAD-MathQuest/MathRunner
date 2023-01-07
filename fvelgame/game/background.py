#------------------------------------------------------------------------------#

import pygame
import math

import game.game_params as gp

#------------------------------------------------------------------------------#
def surface_tiling(surf, tile, vertical):

    t_width  = tile.get_width ()
    t_height = tile.get_height()

    s_width  = surf.get_width ()
    s_height = surf.get_height()

    rect   = pygame.Rect((0,0), (t_width,t_height))
    step_x = t_width
    step_y = t_height

    if vertical:
        rect.bottom = s_height
        step_y      = -step_y

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
class Background:

    #--------------------------------------------------------------------------#
    def __init__(self, world):

        self.world    = world
        self.vertical = world.game_vertical
        self.velocity = world.velocity
        self.margins  = world.margins

        self.bg_scrolls = world.background_scrolls

        if self.bg_scrolls: self.set_background_scrolling    ()
        else:               self.set_background_not_scrolling()

        # Initializing track

        self.tr_image   = world.track_image
        self.tr_scrolls = world.track_scrolls
        self.tr_kills   = world.track_kills

        min_, lenght = self.margins.eval_length(0)

        if self.vertical:
            left  = int(gp.SCREEN_SIZE[0] * min_  )
            width = int(gp.SCREEN_SIZE[0] * lenght)
            self.tr_rect = pygame.Rect(left, 0, width, gp.SCREEN_SIZE[1])
        else:
            top    = int(gp.SCREEN_SIZE[1] * min_  )
            height = int(gp.SCREEN_SIZE[1] * lenght)
            self.tr_rect = pygame.Rect(0, top, gp.SCREEN_SIZE[0], height)

        if self.tr_image:
            self.bg_image.blit(self.tr_image, self.tr_rect, self.tr_rect)

    #--------------------------------------------------------------------------#
    def set_background_not_scrolling(self):

        w_image  = self.world.background_image
        w_width  = w_image.get_width ()
        w_height = w_image.get_height()

        s_width  = gp.SCREEN_SIZE[0]
        s_height = gp.SCREEN_SIZE[1]

        bg_image = pygame.Surface(gp.SCREEN_SIZE)

        if w_width < s_width or w_height < s_height:

            surface_tiling(bg_image, w_image, self.vertical)

        else: # Background has same size or is larger than screen

            rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

            if self.vertical:
                rect.bottom = w_height

            bg_image.blit(w_image, (0,0), rect)

        self.bg_image     = bg_image
        self.bg_show_rect = None

    #--------------------------------------------------------------------------#
    def set_background_scrolling(self):

        w_image  = self.world.background_image
        w_width  = w_image.get_width ()
        w_height = w_image.get_height()

        s_width  = gp.SCREEN_SIZE[0]
        s_height = gp.SCREEN_SIZE[1]

        if self.vertical:

            if w_width < s_width or w_height < s_height:

                n_height = math.ceil(s_height / w_height) * w_height
                n_image  = pygame.Surface((s_width, n_height))

                surface_tiling(n_image, w_image, self.vertical)

                w_image  = n_image
                w_width  = s_width
                w_height = n_height

            self.bg_top_start = w_height
            self.bg_image     = pygame.Surface((s_width, w_height+s_height))

            self.bg_image.blit(w_image, (0,s_height))
            self.bg_image.blit(w_image, (0,0), (0,w_height-s_height,s_width,s_height) )

        else: # Horizontal scrolling

            if w_width < s_width or w_height < s_height:

                n_width = math.ceil(s_width / w_width) * w_width
                n_image = pygame.Surface((n_width, s_height))

                surface_tiling(n_image, w_image, self.vertical)

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

        if self.vertical:

            self.bg_top_start = w_bg_height
            self.bg_image     = pygame.Surface((sc_width, w_bg_height+sc_height))

            self.bg_image.blit(w_bg_image, (0,sc_height))
            self.bg_image.blit(w_bg_image, (0,0), (0,w_bg_height-sc_height,sc_width,sc_height) )

        else:
            self.bg_max_width = w_bg_width + sc_width
            self.bg_image     = pygame.Surface((self.bg_max_width, sc_height))

            self.bg_image.blit(w_bg_image, (0,0))
            self.bg_image.blit(w_bg_image, (sc_width+1,0), (0,0,sc_width,sc_height) )

        self.bg_show_rect = pygame.Rect((0,0), gp.SCREEN_SIZE)

    #--------------------------------------------------------------------------#
    def update(self, velocity):

        if not self.bg_scrolls:
            return

        if self.vertical:
            self.bg_show_rect.top -= velocity

            if self.bg_show_rect.top < 0:
                self.bg_show_rect.top = self.bg_top_start + self.bg_show_rect.top

        else:
            self.bg_show_rect.right += velocity

            if self.bg_show_rect.right > self.bg_max_width:
                self.bg_show_rect.right += gp.SCREEN_SIZE[0] - self.bg_max_width

    #--------------------------------------------------------------------------#
    def draw(self, surf):

        surf.blit(self.bg_image, (0,0), self.bg_show_rect)

    #--------------------------------------------------------------------------#
    def get_player_boundaries(self):

        if self.vertical: return [self.tr_rect.left, self.tr_rect.right]
        else:             return [self.tr_rect.top, self.tr_rect.bottom]

    #--------------------------------------------------------------------------#
    def get_spawn_boundaries(self):

        if self.vertical: return [self.tr_rect.left, self.tr_rect.right]
        else:             return [self.tr_rect.top, self.tr_rect.bottom]

#------------------------------------------------------------------------------#
