#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication
from ui.main_window    import MainWindow
from ui.main_controler import MainControler

#------------------------------------------------------------------------------#
def main( argv ):

    app = QApplication(argv)

    window = MainWindow()

    main_controler = MainControler( window )

    window.show()

    return app.exec()

#------------------------------------------------------------------------------#
