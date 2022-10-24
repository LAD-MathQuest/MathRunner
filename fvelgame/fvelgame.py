#------------------------------------------------------------------------------#

import sys

from world.world import World
import game.game as game
import ui.ui     as ui

#------------------------------------------------------------------------------#
def main( argv ):

    N = len(argv)

    if N > 2:
        sys.exit('Too many parameters!')

    elif N == 2:
        sys.exit( game.main( World() ) )

    else:
        sys.exit( ui.main( sys.argv ) )

#------------------------------------------------------------------------------#
