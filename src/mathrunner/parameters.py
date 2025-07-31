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

# Default games path
# TODO Definir qual vai ser o path default na versão final
games_path = Path(__file__).parents[1] / 'games'

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