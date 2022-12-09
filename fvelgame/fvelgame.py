#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
sys.path.append('.')

import game.run_game as game
import ui.gui        as gui

#------------------------------------------------------------------------------#
def main( argv ):

    N = len(argv)

    if N > 2:
        sys.exit('Too many parameters!')

    elif N == 2:
        sys.exit( game.main( argv[1] ) )

    else:
        sys.exit( gui.main( sys.argv ) )

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    main( sys.argv )

#------------------------------------------------------------------------------#
