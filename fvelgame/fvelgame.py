#!/usr/bin/python
#------------------------------------------------------------------------------#

import __init__
import sys

from world    import World
from game.run import run

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    N = len(sys.argv)

    if N > 2:
        sys.exit('Parâmetros demais')

    elif N == 2:
        run( World() )

    else:
        print('Interface gráfica')

    sys.exit()

#------------------------------------------------------------------------------#
