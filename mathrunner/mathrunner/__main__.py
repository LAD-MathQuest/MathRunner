#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from . import gui

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    sys.exit(gui.main(sys.argv))

#------------------------------------------------------------------------------#
