# ./fvelgame/game/__main__.py
#------------------------------------------------------------------------------#

import sys
sys.path.append('..')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import game.the_game as game

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    sys.exit( game.main( 'world' ) )

#------------------------------------------------------------------------------#
