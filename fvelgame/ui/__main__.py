# ./fvelgame/ui/__main__.py
#------------------------------------------------------------------------------#

import sys
sys.path.append('..')

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import ui.gui as gui

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    sys.exit( gui.main( sys.argv ) )

#------------------------------------------------------------------------------#
