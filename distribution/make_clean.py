#------------------------------------------------------------------------------#
'''Clean the dist folder'''

import shutil

from pathlib import Path

dist_name = 'math-runner-0-1-0'

#------------------------------------------------------------------------------#
def remove_dir(path: Path) -> None:
    '''Recursively removes a directory'''

    if path.is_dir():
        print(f'Removing directory {path}')
        shutil.rmtree(path)
    else:
        print(f"{path} don't exists")

#------------------------------------------------------------------------------#
def remove_files(path: Path, glob: str) -> None:
    '''Removes a list of files'''

    for file in Path(path).glob(glob):
        print(f'Removing {file}')
        file.unlink()

#------------------------------------------------------------------------------#
if __name__ == '__main__':
    '''Remove temporary files'''

    here = Path(__file__).parent

    remove_dir(here / 'build')
    remove_dir(here / dist_name)
    remove_files(here, '*.spec')

    print('Done')

#------------------------------------------------------------------------------#
