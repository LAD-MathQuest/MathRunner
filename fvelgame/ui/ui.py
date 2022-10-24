#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QApplication
from main_window       import MainWindow
from main_controler    import MainControler
from main_model        import MainModel

#------------------------------------------------------------------------------#
def main( argv ):

    app = QApplication(argv)

    window = MainWindow()
    window.show()

    main_controler = MainControler( MainModel(), window )

    return app.exec()

#------------------------------------------------------------------------------#
