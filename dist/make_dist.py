#------------------------------------------------------------------------------#
'''Uses PyInstaller to build the distribution'''

import sys
import shutil

from pathlib import Path

import PyInstaller.__main__ as installer

from examples.__main__ import build_all as build_examples

#------------------------------------------------------------------------------#

dist_name = 'math-runner'
version   = '0-1-0'

#------------------------------------------------------------------------------#
def compile_math_runner(src: Path, dist: str, sep: str) -> None:

    print('Compiling MathRunner...')

    data = src / 'math_runner' / 'resources'

    installer.run([
        'exec_math_runner.py',
        '--name=MathRunner',
        f'--dist={dist}',
        f'--add-data={data}{sep}resources',
        '--noconfirm',
        '--windowed'
    ])

#------------------------------------------------------------------------------#
def compile_infinite_run(src: Path, dist: str, sep: str) -> None:

    print('Compiling InfiniteRun...')

    data = src / 'infinite_run' / 'resources'

    installer.run([
        'exec_infinite_run.py',
        '--name=InfiniteRun',
        f'--dist={dist}',
        f'--add-data={data}{sep}infinite_run/resources',
        '--noconfirm',
        '--windowed'
    ])

#------------------------------------------------------------------------------#
def compile_examples(here: Path, src: Path, dist: str) -> None:

    print('Compiling Examples...')

    build_examples()

    source = src / 'games'
    dest   = here / dist / 'games'

    shutil.copytree(source, dest, dirs_exist_ok=True)

#------------------------------------------------------------------------------#
def zip_distribution(dist: str) -> None:

    print(f'Creating {dist}.zip...')

    shutil.make_archive(dist, 'zip', dist)

#------------------------------------------------------------------------------#
def main() -> None:

    if sys.platform == 'linux':
        sep = ':'

    elif sys.platform == 'win32':
        sep = ';'

    else:
        print(f'Unknown platform {sys.platform}!')
        return

    here = Path(__file__).parent
    src  = here.parent / 'src'
    dist = f'{dist_name}-{sys.platform}-{version}'

    print(f'Creating a distribution {dist}...')

    compile_math_runner (src, dist, sep)
    compile_infinite_run(src, dist, sep)
    compile_examples    (here, src, dist)
    zip_distribution    (dist)

    print('Done')

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    main()

#------------------------------------------------------------------------------#
