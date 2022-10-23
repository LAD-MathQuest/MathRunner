#!/usr/bin/python
#------------------------------------------------------------------------------#

import __init__
import sys
import pygame

from world  import World
from engine import Engine

#------------------------------------------------------------------------------#
def run( world ):

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

    run( world )

    sys.exit()

#------------------------------------------------------------------------------#
