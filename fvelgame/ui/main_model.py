#------------------------------------------------------------------------------#

from world.world import World
import game.game as game

#------------------------------------------------------------------------------#
class MainModel:
    def __init__(self):
        self._world = World()

    #--------------------------------------------------------------------------#
    def new(self):
        self._world = World()

    #--------------------------------------------------------------------------#
    def open(self, file_name):
        print(f'Model: Open not yet implemented ({file_name})!')

    #--------------------------------------------------------------------------#
    def save(self, file_name):
        print(f'Model: Save not yet implemented ({file_name})!')

    #--------------------------------------------------------------------------#
    def undo(self):
        print('Model: Undo not yet implemented!')

    #--------------------------------------------------------------------------#
    def redo(self):
        print('Model: Redo not yet implemented!')

    #--------------------------------------------------------------------------#
    def reset(self):
        print('Model: Reset not yet implemented!')

    #--------------------------------------------------------------------------#
    def run(self):
        game.main( self._world )

    #--------------------------------------------------------------------------#
    def build(self, file_name):
        print(f'Model: Build not yet implemented ({file_name})!')

#------------------------------------------------------------------------------#
