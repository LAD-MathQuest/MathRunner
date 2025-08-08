#------------------------------------------------------------------------------#

import sys
<<<<<<<< HEAD:src/math_runner/__main__.py
from . import gui

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    sys.exit(gui.main(sys.argv))
========
from pathlib import Path
sys.path.append(str(Path(__file__).parent / 'src'))

from infinite_run import game

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    sys.exit(game.main())
>>>>>>>> master:distribution/exec_infinite_run.py

#------------------------------------------------------------------------------#
