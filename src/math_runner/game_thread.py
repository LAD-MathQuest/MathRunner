from PySide6.QtCore import QThread, Signal

class GameThread(QThread):
    finished = Signal()

    def __init__(self, model):
        super().__init__()
        self.model = model

    def run(self):
        self.model.run()
        self.finished.emit()