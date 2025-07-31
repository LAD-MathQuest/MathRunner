#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    help:      Show this message
    clean:     Remove temporary files
    distclean: Remove all files that can be rebuild by make.py
    default:   Build necessary files to execute the program

    dist:      Create ditribution package using PyInstaller
"""

#------------------------------------------------------------------------------#

import sys
import argparse
import shutil
import subprocess

from pathlib import Path

#------------------------------------------------------------------------------#
# Common functions and variables
#------------------------------------------------------------------------------#

here = Path(__file__).parent

#------------------------------------------------------------------------------#
def remove_dir(path: Path) -> None:
    '''Recurcively removes a directory'''

    if path.is_dir():
        print(f'Removing directory {path}')
        shutil.rmtree(path)
    else:
        print(f'{path} não existe')

#------------------------------------------------------------------------------#
def remove_files(path: Path, glob: str) -> None:
    '''Removes a list of files'''

    for file in Path(path).glob(glob):
        print(f'Removing {file}')
        file.unlink()

#------------------------------------------------------------------------------#
def run_python(cmd: str) -> None:
    '''Runs python script by system call'''

    subprocess.run([sys.executable, cmd])

#------------------------------------------------------------------------------#
# Targets
#------------------------------------------------------------------------------#

path_spec = here.parent / 'packaging'
path_work = path_spec   / 'work'
path_dist = path_spec   / 'dist'

#------------------------------------------------------------------------------#
def make_clean():
    '''Remove temporary files'''

    print(f'{here.name}: Cleaning...')

#------------------------------------------------------------------------------#
def make_distclean():
    '''Remove all files that can be rebuild by make.py'''

    make_clean()

    print(f'{here.name}: Hard cleaning...')
    remove_files(path_spec, '*.spec')
    remove_dir(path_work)
    remove_dir(path_dist)

#------------------------------------------------------------------------------#
def make_default():
    '''Build the default target'''

    print(f'{here.name}: Making default target...')

    for ui_file in (here/'ui').glob('*.ui'):
        py_file = ui_file.with_suffix('.py')
        subprocess.run(['pyside6-uic', f'-g python {ui_file} -o {py_file}'])

    subprocess.run(['pyside6-rcc', 'resources.qrc -o resources_rc.py'])

    run_python('./examples/make.py')

#------------------------------------------------------------------------------#
def make_dist():
    '''Execute PyInstaller to build a distribution'''

    import PyInstaller.__main__ as installer

    if sys.platform.startswith('linux'):
        os_name = 'Linux'
        sep = ':'

    elif sys.platform.startswith('win32'):
        os_name = 'Windows'
        sep = ';'

    else:
        print(f'Unkown platform {sys.platform}!')
        return

    print(f'{here.name}: Creating a distribution package for {os_name}...')

    path_app       = here           / 'mathrunner.py'
    path_resources = here           / 'resources'
    path_icon      = path_resources / 'icons' / 'mathrunner.ico'

    installer.run([ str(path_app),
                    '--name=MathRunner',
                   f'--icon={path_icon}',
                   f'--add-data={path_resources}{sep}resources',
                   f'--specpath={path_spec}',
                   f'--distpath={path_dist}',
                   f'--workpath={path_work}',
                    '--noconfirm',
                    '--windowed' ])

#------------------------------------------------------------------------------#
# Main function
#------------------------------------------------------------------------------#
if __name__ == '__main__':
    '''Main function'''

    parser = argparse.ArgumentParser()
    parser.add_argument( 'target', nargs='?', default='default', help='Make target' )
    args = parser.parse_args()

    if args.target == 'default':
        make_default()

    elif args.target == 'help':
        print(__doc__)

    elif args.target == 'clean':
        make_clean()

    elif args.target == 'distclean':
        make_distclean()

    elif args.target == 'dist':
        make_dist()

    else:
        print(f'Error: Unkown target {args.target}!')

#------------------------------------------------------------------------------#
