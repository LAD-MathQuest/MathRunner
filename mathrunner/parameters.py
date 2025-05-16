#------------------------------------------------------------------------------#

import sys

from pathlib import Path

# Working parameters
#------------------------------------------------------------------------------#

# User home directory

if sys.platform.startswith('win32'):
    HOME = Path.home() / 'Documents'
    if not HOME.is_dir():
        HOME = Path.home()
else:
    HOME = Path.home()

# Resources  parameters
#------------------------------------------------------------------------------#

# Resources path
RESOURCES = Path(__file__).resolve().parent / 'resources'

# Application  parameters
#------------------------------------------------------------------------------#

AUTHOR  = "Luis A. D'Afonseca"
VERSION = '0.0.1 - alpha'
TITLE   = 'MathRunner'
MYAPPID = 'Prof_Luis_A_DAfonseca.MathRunner.designer'

ABOUT = f"""
Desenvolvedor: {AUTHOR}
Versão: {VERSION}
Licença: GNU General Public License - Version 3""" 

#------------------------------------------------------------------------------#

PLOT_MAX_T = 5
PLOT_MAX_X = 10


#------------------------------------------------------------------------------#
