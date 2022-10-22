#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
import sys

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame

from world  import World
from engine import Engine

#------------------------------------------------------------------------------#
def run_game( world ):

    pygame.init()
    
    pygame.mouse.set_visible( False )
    
    info = pygame.display.Info()
    
    world.init( (info.current_w, info.current_h) )

    engine = Engine( world )
    
    while True:
    
        if not engine.start():
            break
    
        if not engine.game_loop():
            break

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    world = World()

    run_game( world )

    sys.exit()

#------------------------------------------------------------------------------#
