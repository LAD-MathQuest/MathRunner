#!/usr/bin/python
# ./fvelgame/game/__main__.py
#------------------------------------------------------------------------------#

import sys
sys.path.append('..')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import game
from world.world import World

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    world = World()

    sys.exit( game.main( world ) )

#------------------------------------------------------------------------------#
