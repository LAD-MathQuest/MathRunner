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
        tools.draw_meta_image(ui.label_Image, meta.image)

        ui.spinBox_Width .setValue(meta.image.size[0])
        ui.spinBox_Height.setValue(meta.image.size[1])
        ui.checkBox_KeepAspectRatio.setChecked(True)

        # Score
        ui.doubleSpinBox_Points.setValue(meta.score)

        # Sound
        if meta.sound:

            ui.doubleSpinBox_Volume  .setEnabled(True)
            ui.pushButton_SoundRemove.setEnabled(True)
            ui.pushButton_SoundPlay  .setEnabled(True)

            ui.doubleSpinBox_Volume.setValue(meta.volume)

#------------------------------------------------------------------------------#
