#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import argparse
import pygame

import game.game_params as gp

from world.game_world import GameWorld
from world.meta_world import MetaWorld
from game.engine      import Engine

#------------------------------------------------------------------------------#
def main(meta):
    '''
    This function runs the game

        meta: MetaWorld object
    '''

    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_mode( gp.FULLHD_SIZE, pygame.FULLSCREEN )

    world  = GameWorld(meta)
    engine = Engine  (world)
    
    while True:
    
        # Restart engine and waits for user press any key
        if not engine.start():
            break
    
        # Main game loop
        if not engine.game_loop():
            break

    return 0

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='FVelGame')
    parser.add_argument( 'world', help='Game World file name', nargs='?' )
    args = parser.parse_args()

    meta = MetaWorld.load(args.world) if args.world else MetaWorld()

    sys.exit( main(meta) )

#------------------------------------------------------------------------------#
