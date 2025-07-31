#------------------------------------------------------------------------------#
'''This module defines the GameWorld class.

The GameWorld class stores all parameters defined by the game creator
using pygame structures to be used directly by de Engine.
An instance of GameWorld class is created from an instance of MetaWorld.

Here the lengths are measured in pixels.
'''

#------------------------------------------------------------------------------#

import pygame
from . import game_params as gp

#------------------------------------------------------------------------------#
def surface_from_meta_image(meta):
    '''Create a pygame surface from a MetaImage object'''

    if not meta:
        return None

    if meta.path:
        surf = pygame.image.load(meta.path).convert_alpha()

        if meta.size:
            surf = pygame.transform.scale(surf, meta.size)

    else:
        size = meta.size if meta.size else gp.SCREEN_SIZE
        surf = pygame.Surface(size)
        surf.fill(meta.color)

    return surf

#------------------------------------------------------------------------------#
class GameObjectParam:
    '''Stores all parameters needed to create game objects (sprite).'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create game object parameters from a meta object.'''

        self.image  = surface_from_meta_image(meta.image)
        self.score  = meta.score
        self.sound  = meta.sound
        self.volume = meta.volume

#------------------------------------------------------------------------------#
class ScoreboardParam:
    '''Describes the game scoreboard.'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):

        self.title = meta.title

        self.text_font      = meta.text_font
        self.text_font_size = meta.text_font_size
        self.text_spacing   = meta.text_spacing
        self.text_position  = meta.text_position
        self.text_bgcolor   = meta.text_bgcolor
        self.text_fgcolor   = meta.text_fgcolor

        self.show_points   = meta.show_points
        self.show_velocity = meta.show_velocity
        self.show_time     = meta.show_time

        self.draw_image = bool(meta.image)

        if self.draw_image:
            self.image      = surface_from_meta_image(meta.image)
            self.image_rect = pygame.Rect(meta.image_position, self.image.get_size())
        else:
            self.image      = None
            self.image_rect = pygame.Rect(0,0,0,0)

#------------------------------------------------------------------------------#
class GameWorld:
    '''Manages all parameters needed by the game Engine.'''

    #--------------------------------------------------------------------------#
    def __init__(self, meta):
        '''Create a GameWorld from MetaWorld.'''

        # Software
        #----------------------------------------------------------------------#

        self.soft_name        = meta.soft_name
        self.soft_author      = meta.soft_author
        self.soft_description = meta.soft_description
        self.soft_icon        = meta.soft_icon

        # Game
        #----------------------------------------------------------------------#

        self.game_vertical        = meta.game_vertical
        self.game_time_bonus      = meta.game_time_bonus
        self.game_ambience        = meta.game_ambience
        self.game_ambience_volume = meta.game_ambience_volume

        # Appearance
        #----------------------------------------------------------------------#

        # Background
        self.background_image   = surface_from_meta_image(meta.background_image)
        self.background_scrolls = meta.background_scrolls

        # Track
        self.track_image   = surface_from_meta_image(meta.track_image)
        self.track_scrolls = meta.track_scrolls
        self.track_kills   = meta.track_kills

        self.min_color = meta.min_color
        self.max_color = meta.max_color
        self.min_width = meta.min_width
        self.max_width = meta.max_width

        # Scoreboard
        self.param_scoreboard = ScoreboardParam(meta.scoreboard)

        # Player
        #----------------------------------------------------------------------#

        self.player_speed = round(meta.player_speed / gp.FPS)
        self.param_player = GameObjectParam( meta.player )

        # Obstacles
        #----------------------------------------------------------------------#

        mean = 1 / meta.obstacles_frequency

        self.obstacles_min_delay = mean / 4
        self.obstacles_max_delay = mean * 4

        self.param_obstacles = [ GameObjectParam(ob) for ob in meta.obstacles ]

        # Collectibles
        #----------------------------------------------------------------------#

        mean = 1 / meta.collectibles_frequency

        self.collectibles_min_delay = mean / 4
        self.collectibles_max_delay = mean * 4

        self.param_collectibles = [ GameObjectParam(ob) for ob in meta.collectibles ]

        # Functions
        #----------------------------------------------------------------------#

        self.velocity = meta.velocity
        self.boundary = meta.boundary

#------------------------------------------------------------------------------#

