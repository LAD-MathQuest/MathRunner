#------------------------------------------------------------------------------#

import pygame

from world.game_world import GameWorld
from world.meta_world import MetaWorld, load_meta_world
from game.engine      import Engine

#------------------------------------------------------------------------------#
def main( arg ):
    '''
    This function runs the game

    arg can be a file name with a MetaWorld or a MetaWorld itself
    '''

    if type(arg) is MetaWorld:
        world = GameWorld( arg )
    else:
        world = GameWorld( load_meta_world(arg) )

    pygame.init()
    
    pygame.mouse.set_visible( False )
    
    info = pygame.display.Info()
    
    world.set_dimensions( (info.current_w, info.current_h) )

    engine = Engine(world)
    
    while True:
    
        if not engine.start():
            break
    
        if not engine.game_loop():
            break

    return 0

#------------------------------------------------------------------------------#
