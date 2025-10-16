#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication

from .main_window     import MainWindow
from .main_controller import MainController

#------------------------------------------------------------------------------#
def main( argv ):

    app = QApplication(argv)

    window = MainWindow()

    _ = MainController(window)

    window.resize(900, 1)
    window.show()

    return app.exec()

#------------------------------------------------------------------------------#
