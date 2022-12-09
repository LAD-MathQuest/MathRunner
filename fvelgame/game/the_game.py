#------------------------------------------------------------------------------#

import pygame

from world.the_world import World
from game.engine     import Engine

#------------------------------------------------------------------------------#
def main( world ):

    if type(world) is str:
        world = World(world)

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

    return 0

#------------------------------------------------------------------------------#
