#------------------------------------------------------------------------------#
"""Build all game examples and tests"""

import sys
import subprocess

from pathlib import Path

#------------------------------------------------------------------------------#
def build_all() -> None:

    here = Path(__file__).parent

    games_path = here.parent / "games"
    games_path.mkdir(parents=True, exist_ok=True)

    for build in here.glob('build*.py'):
        subprocess.run([sys.executable, build])

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    build_all()

#------------------------------------------------------------------------------#
