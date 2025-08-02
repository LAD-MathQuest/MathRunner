#------------------------------------------------------------------------------#

import os
import tempfile
import subprocess

from meta import MetaWorld, save_meta, load_meta

from .update_meta_from_ui import update_meta_from_ui
from .update_ui_from_meta import update_ui_from_meta

#------------------------------------------------------------------------------#
class MainModel:

    #--------------------------------------------------------------------------#
    def __init__(self, controller) -> None:

        self.meta = MetaWorld()

        self.con = controller
        self.win = controller.win
        self.ui  = controller.win.ui

    #--------------------------------------------------------------------------#
    def new(self) -> None:
        self.meta = MetaWorld()

    #--------------------------------------------------------------------------#
    def open(self, filename) -> None:
        self.meta = load_meta(filename)

    #--------------------------------------------------------------------------#
    def save(self, filename) -> None:
        save_meta(self.meta, filename)

    #--------------------------------------------------------------------------#
    def update_ui(self) -> None:
        update_ui_from_meta(self.meta, self.ui, self.con)

    #--------------------------------------------------------------------------#
    def update_meta(self) -> None:
        update_meta_from_ui(self.meta, self.ui, self.con)

    #--------------------------------------------------------------------------#
    def run(self) -> None:

        temp = tempfile.NamedTemporaryFile(
            mode   = 'wb',
            prefix = 'meta_',
            suffix = '.game',
            delete = False
        )

        save_meta(self.meta, temp)
        temp.close()

        subprocess.run(["python", '-m', 'infinite_run', temp.name])

        os.remove(temp.name)

    #--------------------------------------------------------------------------#
    def change_velocity_function(self, func) -> None:
        self.meta.velocity.set_function(func)

    #--------------------------------------------------------------------------#
    def change_track_minimum_function(self, func) -> None:
        self.meta.boundary.set_function_min(func)

    #--------------------------------------------------------------------------#
    def change_track_maximum_function(self, func) -> None:
        self.meta.boundary.set_function_max(func)

    #--------------------------------------------------------------------------#
    def get_velocity_function(self):
        return self.meta.velocity

    #--------------------------------------------------------------------------#
    def get_boundary_functions(self):
        return self.meta.boundary

#------------------------------------------------------------------------------#
