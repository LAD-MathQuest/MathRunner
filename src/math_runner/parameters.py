#------------------------------------------------------------------------------#

import os
import sys

from pathlib import Path

production = getattr(sys, 'frozen', False)

if not production:
    games_path = Path(__file__).parents[1] / 'games'
    infinite_run_exe = None

else:
    dist_path  = Path(os.path.dirname(sys.executable)).parent
    games_path = dist_path / 'games'
    exe_name   = 'InfiniteRun.exe' if sys.platform == "win32" else 'InfiniteRun'
    infinite_run_exe = dist_path / 'InfiniteRun' / exe_name

# Application  parameters
#------------------------------------------------------------------------------#

author  = "Luis A. D'Afonseca"
version = '0.1.0 - alpha'
title   = 'MathRunner'
myappid = 'Prof_Luis_A_DAfonseca.MathRunner.designer'

about = f"""
Desenvolvedor: {author}
Versão: {version}
Licença: GNU General Public License - Version 3"""

#------------------------------------------------------------------------------#