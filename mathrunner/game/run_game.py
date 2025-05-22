#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import pygame
import pygame.freetype

from world.meta_world import MetaWorld
from world.game_world import GameWorld
from game.engine      import Engine

#------------------------------------------------------------------------------#
def main():
    '''Runs the game'''

    import argparse

    parser = argparse.ArgumentParser(description='MathRunner')
    parser.add_argument( 'world', help='Game World file name', nargs='?' )
    args = parser.parse_args()

    pygame.init()
    pygame.display.set_mode( (0,0), pygame.FULLSCREEN )
    pygame.mouse.set_visible(False)

    meta   = MetaWorld.load(args.world) if args.world else MetaWorld()
    world  = GameWorld(meta)
    engine = Engine  (world)

    engine.run()

    sys.exit()

#------------------------------------------------------------------------------#
if __name__ == '__main__': main()

#------------------------------------------------------------------------------#
