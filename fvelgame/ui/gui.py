#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication
from ui.main_window    import MainWindow
from ui.main_controler import MainControler
from ui.main_model     import MainModel

#------------------------------------------------------------------------------#
def main( argv ):

    app = QApplication(argv)

    window = MainWindow()
    window.show()

    main_controler = MainControler( MainModel(), window )

    return app.exec()

#------------------------------------------------------------------------------#
