#------------------------------------------------------------------------------#

import sys, os, tempfile

from pathlib import Path
from world.meta_world import MetaWorld

#------------------------------------------------------------------------------#
class MainModel:
    def __init__(self):
        self.meta = MetaWorld()

    #--------------------------------------------------------------------------#
    def new(self):
        self.meta = MetaWorld()

    #--------------------------------------------------------------------------#
    def open(self, file_name):
        self.meta = MetaWorld.load(file_name)

    #--------------------------------------------------------------------------#
    def save(self, file_name):
        pass

    #--------------------------------------------------------------------------#
    def undo(self):
        pass

    #--------------------------------------------------------------------------#
    def redo(self):
        pass

    #--------------------------------------------------------------------------#
    def reset(self):
        pass

    #--------------------------------------------------------------------------#
    def run(self):
        temp_file = tempfile.NamedTemporaryFile( prefix='meta_', suffix='.game' )
        name = str(temp_file.name)

        self.meta.save(name)

        run_game = str(Path(__file__).parents[1]/'game'/'run_game.py')

        os.system( f'{sys.executable} {run_game} {name}')

    #--------------------------------------------------------------------------#
    def build(self, file_name):
        pass

#------------------------------------------------------------------------------#
