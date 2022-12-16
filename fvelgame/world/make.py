#------------------------------------------------------------------------------#

"""
This script replaces a Makefile to avoid dependencies
As the project is very simple it is possible to manage all building tasks manually.

Targets:
    help:      Show this message
    clean:     Remove temporary files
    distclean: Remove all files that can be rebuild by make.py
    default:   Build necessary files to execute the program
"""

#------------------------------------------------------------------------------#

import sys
import os
import argparse
import shutil
import PyInstaller.__main__ as installer

from pathlib import Path

#------------------------------------------------------------------------------#
# Common functions and variables
#------------------------------------------------------------------------------#
    
here = Path(__file__).parent

#------------------------------------------------------------------------------#
def remove_dir(path):
    '''Recurcively removes a directory'''

    if path.is_dir():
        print(f'Removing directory {path}')
        shutil.rmtree(path)
    else:
        print(f'{path} não existe')

#------------------------------------------------------------------------------#
def remove_files( path, glob ):
    '''Removes a list of files'''

    for file in Path(path).glob(glob):
        print(f'Removing {file}')
        file.unlink()

#------------------------------------------------------------------------------#
def run(cmd):
    '''Runs a system command'''

    print(cmd)
    os.system(cmd)

#------------------------------------------------------------------------------#
def run_python(cmd):
    '''Runs python script by system call'''

    run( f'{sys.executable} {cmd}' )

#------------------------------------------------------------------------------#
# Targets
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
def make_clean():
    '''Remove temporary files'''

    print(f'{here.name}: Cleaning...')

#------------------------------------------------------------------------------#
def make_distclean():
    '''Remove all files that can be rebuild by make.py'''

    make_clean()
    print(f'{here.name}: Hard cleaning...')
    remove_files( here.parent / 'resources' / 'games', '*.game' )

#------------------------------------------------------------------------------#
def make_default():
    '''Build the default target'''

    print(f'{here.name}: Making default target...')
    for file in here.glob('build_game-*.py'):
        run_python(file)

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

    else:
        print(f'Error: Unkown target {args.target}!')

#------------------------------------------------------------------------------#
