#------------------------------------------------------------------------------#

from PySide6.QtGui     import QUndoCommand
from PySide6.QtWidgets import QLineEdit, QPlainTextEdit, QTextEdit, QLabel
from PySide6.QtCore    import Qt

#--------------------------------------------------------------------------------#
class HideObjectCommand(QUndoCommand):
    def __init__(
        self,
        object,
        ui,
        position,
        engine,
        description="Alterar imagem"
    ):
        super().__init__(description)

        self.position = position
        self.ui = ui
        self.object = object
        self.engine = engine

    def undo(self):
        self.ui.insertWidget(self.position, self.object)
        self.object.show()
        self.engine.num_obstacles += 1
        self.engine.obstacles.insert(self.position, self.object)
        

    def redo(self):
        self.ui.removeWidget(self.object)
        self.object.hide()
        self.engine.num_obstacles -= 1
        self.engine.obstacles.pop(self.position)
class AddObjectCommand(QUndoCommand):
    def __init__(
        self,
        object,
        ui,
        position,
        engine,
        description="Alterar imagem"
    ):
        super().__init__(description)

        self.position = position
        self.ui = ui
        self.object = object
        self.engine = engine

    def undo(self):
        self.ui.removeWidget(self.object)
        self.object.hide()
        self.engine.num_obstacles -= 1
        self.engine.obstacles.pop(self.position)
        

    def redo(self):
        self.ui.insertWidget(self.position, self.object)
        self.object.show()
        self.engine.num_obstacles += 1
        self.engine.obstacles.insert(self.position, self.object)

#--------------------------------------------------------------------------------#
class ChangeImageCommand(QUndoCommand):

    def __init__(
        self,
        label,
        new_image,
        description="Alterar imagem"
    ):
        super().__init__(description)
        self.label = label
        self.new_image = new_image

    def undo(self):
        self.label.setPixmap(self.old_image) # Mudar o nome para
        self.label.setProperty('original_pixmap', self.original_image)


    def redo(self):
        self.old_image = self.label.pixmap()
        self.original_image = self.label.property('original_pixmap')

        size = self.label.size().boundedTo(self.new_image.size())
        self.label.setPixmap(self.new_image.scaled(size, aspectMode=Qt.KeepAspectRatio))
        self.label.setProperty('original_pixmap', self.new_image)

#--------------------------------------------------------------------------------#

class ChangeImageSpinBoxCommand(QUndoCommand):
    def __init__(
            self,
            label,
            spin_width,
            spin_height,
            old_value_width,
            old_value_height,
            description
    ):
        super().__init__(description)
        self.label = label
        self.spin_width = spin_width
        self.spin_height = spin_height
        self.old_value_width = old_value_width
        self.old_value_height = old_value_height
        self.new_value_width = self.spin_width.value()
        self.new_value_height = self.spin_height.value()

    def undo(self):
        self.spin_width.blockSignals(True)
        self.spin_height.blockSignals(True)

        self.spin_width.setValue(self.old_value_width)
        self.spin_height.setValue(self.old_value_height)

        self.spin_width.blockSignals(False)
        self.spin_height.blockSignals(False)

        image_scaled = self.label.property('original_pixmap').scaled(self.old_value_width, self.old_value_height, Qt.IgnoreAspectRatio)
        self.label.setPixmap(image_scaled)


    def redo(self):
        self.spin_width.blockSignals(True)
        self.spin_height.blockSignals(True)

        self.spin_width.setValue(self.new_value_width)
        self.spin_height.setValue(self.new_value_height)

        self.spin_width.blockSignals(False)
        self.spin_height.blockSignals(False)

        image_scaled = self.label.property('original_pixmap').scaled(self.new_value_width, self.new_value_height, Qt.IgnoreAspectRatio)
        self.label.setPixmap(image_scaled)
        
#--------------------------------------------------------------------------------#
class ChangeValueCommand(QUndoCommand):

    def __init__(
        self,
        target,
        old_value,
        new_value,
        engine,
        description="Alterar valor"
    ):
        super().__init__(description)
        self.target = target
        self.old_value = old_value
        self.new_value = new_value
        self.engine = engine  #referência para chamar update_image_size, para o tamanho mudar quando fizer undo tbm


    def undo(self):
        self._set_value(self.old_value)


    def redo(self):
        self._set_value(self.new_value)


    def _set_value(self, value):
        self.target.blockSignals(True)
        self.target.setValue(value)
        self.target.blockSignals(False)

        if self.target == self.engine.ui.doubleSpinBox_AmbienceSoundVolume:
            self.engine.ambience_set_volume(value)
        else:
            self.engine.update_image_size()


#--------------------------------------------------------------------------------#
class ChangeCheckedCommand(QUndoCommand):

    def __init__(
        self,
        target,
        old_value,
        new_value,
        engine,
        description="Alterar valor checkbox/radioButton"
    ):
        super().__init__(description)
        self.target = target
        self.old_value = old_value
        self.new_value = new_value
        self.engine = engine


    def undo(self):
        self.__set_checkBox(self.old_value)


    def redo(self):
        self.__set_checkBox(self.new_value)


    def __set_checkBox(self, value):
        self.target.blockSignals(True)
        self.target.setChecked(value)
        self.target.blockSignals(False)
        self.engine.update_image_size()

#--------------------------------------------------------------------------------#
class ChangeTextCommand(QUndoCommand):

    def __init__(self, controller, widget, old_text, new_text, description=""):
        super().__init__(description)
        self.controller = controller
        self.widget = widget
        self.old_text = old_text
        self.new_text = new_text


    def undo(self):
        self._set_text(self.old_text)


    def redo(self):
        self._set_text(self.new_text)


    def _set_text(self, text):
        self.widget.blockSignals(True)
        if isinstance(self.widget, (QLineEdit, QLabel)):
            self.widget.setText(text)
        elif isinstance(self.widget, QPlainTextEdit):
            self.widget.setPlainText(text)
        elif isinstance(self.widget, QTextEdit):
            self.widget.setHtml(text)
        self.widget.blockSignals(False)


#--------------------------------------------------------------------------------#
class ChangeSoundCommand(QUndoCommand):

    def __init__(
            self,
            controller,
            old_sound,
            new_sound,
            old_volume,
            new_volume,
            description
        ):
        super().__init__(description)
        self.controller = controller
        self.old_sound  = old_sound
        self.new_sound  = new_sound
        self.old_volume = old_volume
        self.new_volume = new_volume


    def undo(self):
        self._apply_change(self.old_sound, self.old_volume)
        self.controller.audio_manager.stop()


    def redo(self):
        self._apply_change(self.new_sound, self.new_volume)


    def _apply_change(self, sound, volume):
        self.controller.model.meta.game_ambience = sound
        self.controller.model.meta.game_ambience_volume = volume

        # Atualiza UI
        if sound:
            self.controller.ui.pushButton_AmbienceSoundPlay.setEnabled(True)
            self.controller.ui.pushButton_AmbienceSoundRemove.setEnabled(True)
            self.controller.ui.doubleSpinBox_AmbienceSoundVolume.setEnabled(True)
            self.controller.ui.doubleSpinBox_AmbienceSoundVolume.setValue(volume)
        else:
            self.controller.ui.pushButton_AmbienceSoundPlay.setEnabled(False)
            self.controller.ui.pushButton_AmbienceSoundRemove.setEnabled(False)
            self.controller.ui.doubleSpinBox_AmbienceSoundVolume.setEnabled(False)

        # Para o som atual se necessário
        if self.controller.audio_manager.current_sound != sound:
            self.controller.audio_manager.stop()

        self.controller.changed = True

#------------------------------------------------------------------------------#
