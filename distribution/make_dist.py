#------------------------------------------------------------------------------#
'''Execute PyInstaller to build the distribution'''

import sys
import shutil

from pathlib import Path

import PyInstaller.__main__ as installer

from examples.__main__ import build_all as build_examples

#------------------------------------------------------------------------------#

dist_name = 'math-runner-0-1-0'

here = Path(__file__).parent
src  = here.parent / 'src'

#------------------------------------------------------------------------------#
def compile_math_runner(sep: str) -> None:

    print('Compiling MathRunner...')

    data = src / 'math_runner' / 'resources'

    installer.run([
        'exec_math_runner.py',
        '--name=MathRunner',
        f'--dist={dist_name}',
        f'--add-data={data}{sep}resources',
        '--noconfirm',
        '--windowed'
    ])

#------------------------------------------------------------------------------#
def compile_infinite_run(sep: str) -> None:

    print('Compiling InfiniteRun...')

    data = src / 'infinite_run' / 'resources'

    installer.run([
        'exec_infinite_run.py',
        '--name=InfiniteRun',
        f'--dist={dist_name}',
        f'--add-data={data}{sep}infinite_run/resources',
        '--noconfirm',
        '--windowed'
    ])

#------------------------------------------------------------------------------#
def compile_examples() -> None:
    print('Compiling Examples...')

    build_examples()

    source = src / 'games'
    dest   = here / dist_name / 'games'

    shutil.copytree(source, dest, dirs_exist_ok=True)

#------------------------------------------------------------------------------#
def zip_distribution() -> None:
    print(f'Creating {dist_name}.zip...')
    shutil.make_archive(dist_name, 'zip', dist_name)

#------------------------------------------------------------------------------#
def deploy() -> None:

    if sys.platform == 'linux':
        os_name = 'Linux'
        sep = ':'

    elif sys.platform == 'win32':
        os_name = 'Windows'
        sep = ';'

    else:
        print(f'Unknown platform {sys.platform}!')
        return

    print(f'Creating a distribution package for {os_name}...')

    compile_math_runner (sep)
    compile_infinite_run(sep)
    compile_examples()
    zip_distribution()

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    deploy()

#------------------------------------------------------------------------------#
