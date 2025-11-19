#------------------------------------------------------------------------------#

import os
import sys
import tempfile
import subprocess

from meta import MetaWorld, save_meta, load_meta

from .parameters          import production, infinite_run_exe
from .update_meta_from_ui import update_meta_from_ui
from .update_ui_from_meta import update_ui_from_meta

from meta.math_function import EvalFunctionError
from PySide6.QtWidgets import QMessageBox
import numpy as np


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
        # Antes de rodar, valida as funções
        try:
        # verifica se gera erro 
            self.meta.velocity.eval(np.array([0.0]))
            self.meta.boundary.eval_min(np.array([0.0]))
            self.meta.boundary.eval_max(np.array([0.0]))

        except EvalFunctionError as e:
            QMessageBox.critical(self.win, "Erro", e.message)
            return  # impede o jogo de rodar
        
        temp = tempfile.NamedTemporaryFile(
            mode   = 'wb',
            prefix = 'meta_',
            suffix = '.game',
            delete = False
        )

        save_meta(self.meta, temp)
        temp.close()

        if production:
            subprocess.run([str(infinite_run_exe), temp.name])
        else:
            subprocess.run([sys.executable, '-m', 'infinite_run', temp.name])

        os.remove(temp.name)

    #--------------------------------------------------------------------------#
    def change_velocity_function(self, func) -> None:
        self.meta.velocity.set_function(func)

    #--------------------------------------------------------------------------#
    def change_boundary_minimum_function(self, func) -> None:
        self.meta.boundary.set_function_min(func)

    #--------------------------------------------------------------------------#
    def change_boundary_maximum_function(self, func) -> None:
        self.meta.boundary.set_function_max(func)

    #--------------------------------------------------------------------------#
    def get_velocity_function(self):
        return self.meta.velocity

    #--------------------------------------------------------------------------#
    def get_boundary_functions(self):
        return self.meta.boundary

#------------------------------------------------------------------------------#
