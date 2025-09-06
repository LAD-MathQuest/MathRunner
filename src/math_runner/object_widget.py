#------------------------------------------------------------------------------#

from PySide6.QtWidgets import QWidget

from .form_object_widget import Ui_ObjectWidget
from .                   import tools

#------------------------------------------------------------------------------#
class ObjectWidget(QWidget):

    #--------------------------------------------------------------------------#
    def __init__(self, parent=None):

        super().__init__(parent)

        self.ui = Ui_ObjectWidget()
        self.ui.setupUi(self)

        self.sound = None

    #--------------------------------------------------------------------------#
    def meta_to_object(self, meta):

        ui = self.ui

        # Image
        tools.meta_image_to_label(ui.label_Image, meta.image)

        ui.spinBox_Width.blockSignals(True)
        ui.spinBox_Height.blockSignals(True)
        ui.spinBox_Width .setValue(meta.image.size[0])
        ui.spinBox_Height.setValue(meta.image.size[1])
        ui.spinBox_Width.blockSignals(False)
        ui.spinBox_Height.blockSignals(False)
        ui.checkBox_KeepAspectRatio.setChecked(True)

        # Score
        ui.doubleSpinBox_Points.setValue(meta.score)

        # Sound
        if meta.sound:

            ui.doubleSpinBox_Volume  .setEnabled(True)
            ui.pushButton_SoundRemove.setEnabled(True)
            ui.pushButton_SoundPlay  .setEnabled(True)

            ui.doubleSpinBox_Volume.setValue(meta.volume)


    #--------------------------------------------------------------------------#
    def object_to_meta(self, meta):

        ui = self.ui

        # Image
        tools.label_to_meta_image(ui.label_Image, meta.image)

        meta.image.size = [
            ui.spinBox_Width .value(),
            ui.spinBox_Height.value()
        ]

        # BUG: Corrigir o tamanho dos objetos
        if meta.image.size[0] < 10 or meta.image.size[1] < 10:
            print('Tamanho errado: ', meta.image.size)
            meta.image.size = [60, 60]
            print('Novo tamanho: ', meta.image.size)

        # Score
        meta.score = ui.doubleSpinBox_Points.value()

        # TODO: Sound

#------------------------------------------------------------------------------#
