
from PySide6.QtGui     import QPalette, QPixmap, QUndoGroup, QUndoStack, QFontDatabase, QFont, QColor
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox, QVBoxLayout, QColorDialog, QDialog

from .form_scoreboard import Ui_Dialog

from . import tools
from . import undo_commands as undo
from pathlib import Path


class ScoreboardDialog(QDialog, Ui_Dialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller             
        self.meta = controller.meta              

        self.spinBox.setValue(self.meta.text_font_size or 14)

        self._color = getattr(controller, "scoreboard_fg", QColor("black"))
        self._bg_color = getattr(controller, "scoreboard_bg", QColor("white"))

        # conecta botões da janela
        self.radioButton_3.toggled.connect(self.update_font_source_state)
        self.radioButton.toggled.connect(self.update_font_source_state)
        self.radioButton_2.toggled.connect(self.update_font_source_state)
        self.spinBox.valueChanged.connect(self.update_preview) 
        self.pushButton.clicked.connect(self.choose_font_color)     # Cor da fonte
        self.pushButton_2.clicked.connect(self.choose_bg_color)     # Cor de fundo
        self.spinBox.valueChanged.connect(self.update_preview)      # tamanho da fonte
        self.pushButton_3.clicked.connect(self.choose_font_file)  # Selecionar arquivo de fonte

        self.update_preview()

    
    #--------------------------------------------------------------------------#

    def choose_font_color(self):
        color = QColorDialog.getColor(self._color, self, "Escolher cor da fonte")
        if color.isValid():
            self._color = color
            self.update_preview()

    
    #--------------------------------------------------------------------------#

    def choose_bg_color(self):
        color = QColorDialog.getColor(self._bg_color, self, "Escolher cor de fundo")
        if color.isValid():
            self._bg_color = color
            self.update_preview()

    
    #--------------------------------------------------------------------------#
    
    def choose_font_file(self):
        fname, _ = QFileDialog.getOpenFileName(
            self,
            "Escolher arquivo de fonte",
            str(Path(__file__).parents[1]/'examples/resources/fonts'),
            "Fontes (*.ttf *.otf)"
        )
        if fname:
     
            self.controller.scoreboard_font_path = fname
            # força atualizar o preview no label principal
            self.update_preview()

    
    #--------------------------------------------------------------------------#

    def update_preview(self):
        self.controller.scoreboard_font_path = getattr(self.controller, "scoreboard_font_path", None)
        self.controller.scoreboard_font_size = self.spinBox.value()
        self.controller.scoreboard_fg = self._color
        self.controller.scoreboard_bg = self._bg_color

        # Atualiza o preview no MainWindow
        self.controller.update_scoreboard_preview()
    
    
    #--------------------------------------------------------------------------#

    def update_font_source_state(self):
        self.pushButton_3.setEnabled(self.radioButton_3.isChecked())
        self.fontComboBox.setEnabled(self.radioButton.isChecked())
        self.comboBox.setEnabled(self.radioButton_2.isChecked())
    
    
    #--------------------------------------------------------------------------#

    def accept(self):
        # Persiste no meta quando usuário clicar OK
        self.meta.text_font_size = self.spinBox.value()
        self.meta.text_fgcolor   = tools.qcolor_to_tuple(self._color)
        self.meta.text_bgcolor   = tools.qcolor_to_tuple(self._bg_color)
        super().accept()

