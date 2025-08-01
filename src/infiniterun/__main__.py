#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

import pygame
import pygame.freetype

from meta import MetaWorld, load_meta

from .world  import GameWorld
from .engine import Engine

#------------------------------------------------------------------------------#
def main():
    '''Runs the game'''

    parser = argparse.ArgumentParser(description='MathRunner')
    parser.add_argument('world', help='Game World file name', nargs='?')
    args = parser.parse_args()

    if not args.world:
        meta = MetaWorld()

    else:
        try:
            meta = load_meta(args.world)

        except FileNotFoundError:
            print(f"Error: The file {args.world} was not found.")
            sys.exit(1)

        except PermissionError:
            print(f"Error: You do not have permission to access file {args.world}.")
            sys.exit(1)

        except IOError:
            print(f"Error: An unexpected I/O error occurred while reading file {args.world}.")
            sys.exit(1)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)

    pygame.init()
    pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    pygame.mouse.set_visible(False)

    world  = GameWorld(meta)
    engine = Engine(world)

    engine.run()
    sys.exit()

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    main()

#------------------------------------------------------------------------------#
