#------------------------------------------------------------------------------#
"""Build all game examples and tests"""

import sys
import subprocess

from pathlib import Path

#------------------------------------------------------------------------------#
if __name__ == '__main__':

    here = Path(__file__).parent

    for build in here.glob('build*.py'):
        subprocess.run([sys.executable, build])

#------------------------------------------------------------------------------#
