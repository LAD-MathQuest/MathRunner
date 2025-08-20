#------------------------------------------------------------------------------#

from PySide6.QtGui     import QPalette, QPixmap, QUndoCommand, QUndoGroup, QUndoStack
from PySide6.QtWidgets import (QApplication,
                               QFileDialog,
                               QMessageBox,
                               QVBoxLayout,
                               QLineEdit,
                               QPlainTextEdit,
                               QTextEdit,
                               QLabel,
                               QTabWidget,
                               QSpinBox)
from PySide6.QtCore import Qt

from . import parameters
from . import tools

from pathlib import Path

from meta import MetaWorld, save_meta, load_meta
from meta.meta_world import MetaWorld, MetaImage, MetaObject, MetaScoreboard

from .main_model    import MainModel
from .object_widget import ObjectWidget
from .plot_velocity import PlotVelocity
from .plot_track    import PlotTrack

import sys

from PySide6.QtGui import QUndoCommand, QPixmap
from PySide6.QtCore import Qt, QTimer
from pathlib import Path
from io import BytesIO
import pygame, os, tempfile
sys.path.append(str(Path(__file__).parents[1]))

#--------------------------------------------------------------------------------#
class ChangeImageCommand(QUndoCommand):
    def __init__(self, label, old_image, new_image, description="Alterar imagem"):
        super().__init__(description)
        self.label = label
        self.old_image = old_image
        self.new_image = new_image

    def undo(self):
        self._set_image(self.old_image)
    def redo(self):
        self._set_image(self.new_image)

    def _set_image(self, image):
        if image:
            pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)
        else:
            self.label.clear()

class ChangeValueCommand(QUndoCommand):
    def __init__(self, target, old_value, new_value, engine, description="Alterar valor"):
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
    
class ChangeCheckedCommand(QUndoCommand):
    def __init__(self, target, old_value, new_value, engine, description="Alterar valor checkbox/radioButton"):
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

class ChangeSoundCommand(QUndoCommand):
    def __init__(self, controller, old_sound, new_sound, old_volume, new_volume, description):
        super().__init__(description)
        self.controller = controller
        self.old_sound = old_sound
        self.new_sound = new_sound
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

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_sound = None
        self.temp_files = []
        
    def load_sound(self, sound_source):
        self.stop()

        if isinstance(sound_source, BytesIO):
            temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
            temp_file.write(sound_source.getvalue())
            temp_file.close()
            self.temp_files.append(temp_file.name)
            pygame.mixer.music.load(temp_file.name)
        else:
            sound_path = str(sound_source) if hasattr(sound_source, 'fspath') else sound_source
            pygame.mixer.music.load(sound_path)
    
    def play(self, loop=False, volume=1.0):
        if pygame.mixer.music.get_busy():
            self.stop()
        
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1 if loop else 0)
    
    def stop(self):
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
    
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))
    
    def cleanup(self):
        self.stop()
        for temp_file in self.temp_files: 
            os.unlink(temp_file)
        self.temp_files = []

#------------------------------------------------------------------------------#
class MainController:

    path_resources = Path(__file__).parents[1]/'examples/resources'
    path_games = Path(__file__).parents[1]/'games'

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.win = window
        self.ui  = window.ui

        self.model = MainModel(self)
        self.audio_manager = AudioManager()

        color = self.win.palette().color(QPalette.Window)

        self.plot_velocity = PlotVelocity(
            self.ui.plotVelocity,
            color,
            self.model.get_velocity_function()
        )
        self.plot_track= PlotTrack(
            self.ui.plotBoundary,
            color,
            self.model.get_boundary_functions()
        )

        self.init_objects()

        self.last_dir  = str(parameters.games_path)
        self.file_name = ''

        self.start_new()

        # Iniciando as variáveis de imagem com a imagem padrao 
        self.background_image = self.ui.label_BackgroundImage.pixmap().toImage()
        self.track_image = self.ui.label_TrackImage.pixmap().toImage()
        self.player_image = self.ui.label_PlayerImage.pixmap().toImage()
        self.player_width = self.ui.spinBox_PlayerWidth.value()
        self.player_height = self.ui.spinBox_PlayerHeight.value()
        self.player_speed = self.ui.spinBox_PlayerSpeed.value()
        self.player_keep_aspect = self.ui.checkBox_PlayerKeepAspectRatio.isChecked()

        # Inicializa os valores dos textos para undo/redo
        widgets = [(self.ui.lineEdit_GameName, self.model.meta.soft_name), (self.ui.lineEdit_Author, self.model.meta.soft_author),(self.ui.plainTextEdit_GameDescription, self.model.meta.soft_description),
                   (self.ui.lineEdit_FunctionVelocity, self.model.meta.velocity.get_function_orig()), (self.ui.lineEdit_FunctionTrackMinimum, self.model.meta.boundary.get_function_min_orig()),
                   (self.ui.lineEdit_FunctionTrackMaximum, self.model.meta.boundary.get_function_max_orig())]
        for widget, default in widgets:
            if not hasattr(widget, '_last_text'):
               widget._last_text = default

        # define _last_value para undo funcionar na primeira alteração
        self.ui.spinBox_PlayerWidth._last_value = self.player_width
        self.ui.spinBox_PlayerHeight._last_value = self.player_height
        self.ui.spinBox_PlayerSpeed._last_value = self.player_speed
        self.ui.checkBox_PlayerKeepAspectRatio._last_value = self.player_keep_aspect
        self.ui.doubleSpinBox_AmbienceSoundVolume._last_value = self.ui.doubleSpinBox_AmbienceSoundVolume.value()
        self.ui.doubleSpinBox_ScoreTimeBonus._last_value = self.ui.doubleSpinBox_ScoreTimeBonus.value()
        self.ui.checkBox_TrackMaximumKills._last_value = self.ui.checkBox_TrackMaximumKills.isChecked()
        self.ui.checkBox_TrackMinimumKills._last_value = self.ui.checkBox_TrackMinimumKills.isChecked()
        self.ui.radioButton_HorizontalScrolling._last_value = self.ui.radioButton_HorizontalScrolling.isChecked()
        self.ui.radioButton_VerticalScrolling._last_value = self.ui.radioButton_VerticalScrolling.isChecked()

        # Criação do Undo Group
        self.undo_group = QUndoGroup(self.win)

        self.connect_signals_and_slots()

        # Criação das pilhas de Undo
        self.undo_stacks = []
        for i in range(self.ui.tabWidget_Game.count()):
            self.undo_stacks.append(QUndoStack(self.win))
            self.undo_group.addStack(self.undo_stacks[i])
        self.undo_group.setActiveStack(self.undo_stacks[0])

    #--------------------------------------------------------------------------#
    def init_objects(self):

        #--- Obstacles --------------------------------------------------------#

        self.obstacles_area = self.ui.scrollArea_Obstacles
        self.obstacles_box  = self.obstacles_area.findChild(QVBoxLayout)
        self.num_obstacles  = 0
        self.obstacles      = []

        self.new_obstacle_widget()

        #--- Collectibles -----------------------------------------------------#

        self.collectibles_area = self.ui.scrollArea_Collectibles
        self.collectibles_box  = self.collectibles_area.findChild(QVBoxLayout)
        self.num_collectibles  = 0
        self.collectibles      = []

        self.new_collectible_widget()

    #--------------------------------------------------------------------------#
    def connect_signals_and_slots(self):

        ui = self.ui

        #--- Menu signals -----------------------------------------------------#

        ui.action_New     .triggered.connect( self.new     )
        ui.action_Open    .triggered.connect( self.open    )
        self.ui.action_Save.triggered.connect(self.save)
        self.ui.action_Save.setEnabled(True)
        ui.action_Save_as .triggered.connect( self.save_as )
        ui.action_Exit    .triggered.connect( self.exit    )
        # ui.action_Undo    .triggered.connect( self.undo    )
        self.ui.action_Undo.triggered.connect(self.undo_group.undo)
        self.ui.action_Redo.triggered.connect(self.undo_group.redo)

        self.ui.action_Undo.setEnabled(True)
        self.ui.action_Redo.setEnabled(True)


        self.ui.menuEdit.addAction(self.ui.action_Undo)
        self.ui.menuEdit.addAction(self.ui.action_Redo)

        # ui.action_Redo    .triggered.connect( self.redo    )
        # ui.action_Reset   .triggered.connect( self.reset   )
        ui.action_Run     .triggered.connect( self.run     )
        ui.action_Build   .triggered.connect( self.build   )
        ui.action_About   .triggered.connect( self.about   )
        ui.action_Contents.triggered.connect( self.help    )

        #--- Game Tab signals -------------------------------------------------#

        ui.lineEdit_GameName.editingFinished.connect(lambda: self.change_text(ui.lineEdit_GameName))
        ui.lineEdit_Author  .editingFinished.connect(lambda: self.change_text(ui.lineEdit_Author))
        ui.plainTextEdit_GameDescription.textChanged.connect(lambda: self.change_text(ui.plainTextEdit_GameDescription))
        
        ui.pushButton_IconSelect.clicked.connect(self.select_icon)
        
        ui.radioButton_HorizontalScrolling.toggled.connect(lambda: self.select_checked(self.ui.radioButton_VerticalScrolling))
        ui.radioButton_VerticalScrolling.toggled.connect(lambda: self.select_checked(self.ui.radioButton_HorizontalScrolling))
        ui.checkBox_TrackMaximumKills.stateChanged.connect(lambda value: self.select_checked(self.ui.checkBox_TrackMaximumKills))
        ui.checkBox_TrackMinimumKills.stateChanged.connect(lambda value: self.select_checked(self.ui.checkBox_TrackMinimumKills))
        ui.doubleSpinBox_ScoreTimeBonus.valueChanged.connect(lambda value: self.select_value(self.ui.doubleSpinBox_ScoreTimeBonus))

        ui.pushButton_AmbienceSoundSelect.clicked.connect(self.select_ambience_sound)
        ui.pushButton_AmbienceSoundRemove.clicked.connect(self.ambience_remove)
        ui.pushButton_AmbienceSoundPlay.clicked.connect( self.ambience_play )
        ui.doubleSpinBox_AmbienceSoundVolume.valueChanged.connect(lambda value: self.select_value(self.ui.doubleSpinBox_AmbienceSoundVolume))

        #--- Appearance Tab signals -------------------------------------------#

        ui.pushButton_SelectBackgroundImage.clicked.connect(self.select_image)
        
        # ui.checkBox_BackgroundScrolls

        # ui.checkBox_DrawTrack
        ui.pushButton_SelectTrackImage.clicked.connect(self.select_track_image)

        ui.pushButton_SelectScoreboardImage.clicked.connect(self.select_scoreboard_image)
        # ui.spinBox_ScoreboardImagePositionX
        # ui.spinBox_ScoreboardImagePositionY
        # ui.spinBox_ScoreboardImageWidth
        # ui.spinBox_ScoreboardImageHeight
        # ui.checkBox_ScoreboardImageKeepAspectRatio
        # ui.spinBox_ScoreboardTextPositionX
        # ui.spinBox_ScoreboardTextPositionY
        # ui.spinBox_ScoreboardTextWidth
        # ui.spinBox_ScoreboardTextHeight
        # ui.pushButton_ChoseScoreboardBgColor
        # ui.pushButton_ChoseScoreboardFgColor

        #--- Objects Tab signals ----------------------------------------------#

        ui.pushButton_NewObstacle   .clicked.connect(self.new_obstacle_widget   )
        ui.pushButton_NewCollectible.clicked.connect(self.new_collectible_widget)

        ui.doubleSpinBox_ObstaclesFrequency.   valueChanged.connect(self.obstacles_frequency_changed   )
        ui.doubleSpinBox_CollectiblesFrequency.valueChanged.connect(self.collectibles_frequency_changed)

        ui.pushButton_SelectPlayerImage.clicked.connect(self.select_player_image)
        ui.spinBox_PlayerWidth.valueChanged.connect(lambda value: self.select_value(self.ui.spinBox_PlayerWidth))
        ui.spinBox_PlayerHeight.valueChanged.connect(lambda value: self.select_value(self.ui.spinBox_PlayerHeight))
        ui.checkBox_PlayerKeepAspectRatio.stateChanged.connect(lambda value: self.select_checked(self.ui.checkBox_PlayerKeepAspectRatio))
        
        ui.spinBox_PlayerSpeed.valueChanged.connect(lambda value: self.select_value(self.ui.spinBox_PlayerSpeed))

        #--- Velocity and Boundary Tabs signals -------------------------------#

        ui.lineEdit_FunctionVelocity    .editingFinished.connect(self.function_velocity_changed     )
        ui.lineEdit_FunctionTrackMinimum.editingFinished.connect(self.function_track_minimum_changed)
        ui.lineEdit_FunctionTrackMaximum.editingFinished.connect(self.function_track_maximum_changed)

        ui.tabWidget_Game.currentChanged.connect(self.update_undo_stack)
    #--------------------------------------------------------------------------#
    # Actions
    #--------------------------------------------------------------------------#

    def update_undo_stack(self, index):
        self.undo_group.setActiveStack(self.undo_stacks[index])

    #--------------------------------------------------------------------------#
    def new(self):

        if not self.confirm_deletion():
            return

        self.file_name = ''
        self.start_new()

    #--------------------------------------------------------------------------#
    def open(self):
        fname = self.get_open_fname(
            'Choose a game description',
            self.last_dir,
            'game'
        )

        if fname:
            # TODO try:
            labelBackground = self.ui.label_BackgroundImage
            labelTrack = self.ui.label_TrackImage
            old_backgroundoImage = getattr(self, 'background_image', '')
            old_trackImage = getattr(self, 'track_image', '')

            self.file_name = fname
            self.model.open(self.file_name)
            
            self.start_view_from_model()

            self.add_image_undo(labelBackground, old_backgroundoImage, labelBackground.pixmap().toImage(), 'Alterar imagem de fundo')
            self.add_image_undo(labelTrack, old_trackImage, labelTrack.pixmap().toImage(), 'Alterar imagem do caminho de fundo')
            self.background_image = labelBackground.pixmap().toImage()
            self.track_image = labelTrack.pixmap().toImage()


    #--------------------------------------------------------------------------#
    def save(self):
        meta = MetaWorld()

        #dados de texto
        meta.soft_name = self.ui.lineEdit_GameName.text()
        meta.soft_author = self.ui.lineEdit_Author.text()
        meta.soft_description = self.ui.plainTextEdit_GameDescription.toPlainText()

        #Som ambiente
        if hasattr(self, 'ambience_sound_file'):
            try:
                with open(self.ambience_sound_file, "rb") as f:
                    meta.game_ambience = f.read()
                meta.game_ambience_volume = 0.7
            except Exception as e:
                self.error_box("Erro", f"Falha ao carregar som de ambiente:\n{e}")

        #Imagem de fundo em bytes
        meta.background_image = MetaImage()
        tools.label_to_meta_image(self.ui.label_BackgroundImage, meta.background_image)

        #Imagem da pista em bytes
        meta.track_image = MetaImage()
        tools.label_to_meta_image(self.ui.label_TrackImage, meta.track_image)

        #Imagem do Scoreboard em bytes
        meta.scoreboard.image = MetaImage()
        meta.scoreboard.image.size = (100,100) #remover essa linha depois
        tools.label_to_meta_image(self.ui.label_ScoreboardImage, meta.scoreboard.image)



        # TODO: coletar outros dados da interface, ex:
        # - scoreboard_image
        # - obstáculos
        # - colecionáveis
        # - funções de velocidade e limites

        save_path = self.get_save_fname("Salvar jogo", "game", suggestion=str(self.path_games))

        if save_path:
            save_meta(meta, save_path)
            QMessageBox.information(self.win, "Sucesso", f"Jogo salvo em:\n{save_path}")
            self.changed = False
            self.ui.action_Save.setEnabled(True)

        self.ui.action_Save.setEnabled(True)

    #--------------------------------------------------------------------------#
    def save_as(self):
        self.file_name = 'get_file_name'
        self.model.save(self.file_name)
        self.changed = False

    #--------------------------------------------------------------------------#
    def exit(self):
        if self.confirm_deletion():
            QApplication.quit()

    #--------------------------------------------------------------------------#
    def run(self):
        self.block_ui()
        self.model.update_meta()
        self.model.run()

    #--------------------------------------------------------------------------#
    def build(self):
        # self.exe_file_name = 'get_file_name'
        # self.block_ui()
        # self.model.build( self.exe_file_name )
        pass

    #--------------------------------------------------------------------------#
    def about(self):
        QMessageBox.about(
            self.win,
            parameters.title + ' - About',
            parameters.about
        )

    #--------------------------------------------------------------------------#
    def help(self):
        QMessageBox.about(
            self.win,
            parameters.title + ' - Help',
            parameters.about
        )

    #--------------------------------------------------------------------------#
    # Slots
    #--------------------------------------------------------------------------#

    def select_image(self):
        path_backgrounds = self.path_resources / 'backgrounds'
        fname = self.get_open_fname('Escolha uma Imagem', path_backgrounds, 'png')
        
        if fname:
            label = self.ui.label_BackgroundImage

            old_image = getattr(self, 'background_image', '')
            
            tools.path_image_to_label(label, fname)

            new_image = label.pixmap().toImage()
            
            self.add_image_undo(label, old_image, new_image, "Alterar imagem do fundo")
            self.background_image = new_image
            self.changed = True

    #--------------------------------------------------------------------------#
    def select_track_image(self):
        path_backgrounds = self.path_resources / 'backgrounds'
        fname = self.get_open_fname('Escolha uma Imagem', path_backgrounds, 'png')

        if fname:
            label = self.ui.label_TrackImage

            old_image = getattr(self, 'track_image', '')
            tools.path_image_to_label(label, fname)
            new_image = label.pixmap().toImage()

            self.add_image_undo(label, old_image, new_image, "Alterar imagem do caminho de fundo")

            self.track_image = new_image
            self.changed = True

    #--------------------------------------------------------------------------#
  
    def select_scoreboard_image(self):
        path_scoreboards = self.path_resources / 'scoreboards'
        fname = self.get_open_fname('Escolha uma Imagem', path_scoreboards, 'png')
        
        if fname:
            label = self.ui.label_ScoreboardImage  
            old_image = getattr(self, 'scoreboard_image', '')  
            tools.path_image_to_label(label, fname)

            new_image = label.pixmap().toImage()

            self.add_image_undo(label, old_image, new_image, "Alterar imagem do placar")
            self.scoreboard_image = new_image  
            self.changed = True



    #--------------------------------------------------------------------------#
    def select_player_image(self):
        path_icon = self.path_resources / 'icons'
        fname = self.get_open_fname('Escolha uma Imagem', path_icon, 'png')
        
        if fname:
            label = self.ui.label_PlayerImage
            old_image = getattr(self, 'player_image_original', None)
            if old_image is not None:
                old_image = old_image.toImage()

            #guarda a imagem original como QPixmap
            self.player_image_original = QPixmap(fname)

            #coloca no label a primeira versão
            label.setScaledContents(False)
            label.setAlignment(Qt.AlignCenter)
            label.setPixmap(self.player_image_original)

            #atualiza spinBoxes
            self.ui.spinBox_PlayerWidth.setValue(self.player_image_original.width())
            self.ui.spinBox_PlayerHeight.setValue(self.player_image_original.height())

            self.player_image = self.player_image_original
            self.add_image_undo(label, old_image, self.player_image_original.toImage(), "Alterar imagem do fundo")
            self.changed = True
    #--------------------------------------------------------------------------#
    def update_image_size(self):    
        width = self.ui.spinBox_PlayerWidth.value()
        height = self.ui.spinBox_PlayerHeight.value()
        keep = self.ui.checkBox_PlayerKeepAspectRatio.isChecked()

        if hasattr(self, "player_image_original") and not self.player_image_original.isNull():
            pixmap = self.player_image_original

            if keep:
                scaled = pixmap.scaledToWidth(width, Qt.SmoothTransformation)
                self.ui.spinBox_PlayerHeight.blockSignals(True)
                self.ui.spinBox_PlayerHeight.setValue(scaled.height())
                self.ui.spinBox_PlayerHeight.blockSignals(False)
            else:
                scaled = pixmap.scaled(width, height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

            self.ui.label_PlayerImage.setPixmap(scaled)
            self.player_image = scaled
    #--------------------------------------------------------------------------#
    def select_value(self, spinBox):
        new_value = spinBox.value()
        old_value = getattr(spinBox, "_last_value", spinBox.value())  

        if old_value != new_value:
            self.add_value_undo(spinBox, old_value, new_value, "ALterar valor")
        spinBox._last_value = new_value
    
    #--------------------------------------------------------------------------#
    def select_checked(self, target):
        new_value = target.isChecked()
        old_value = getattr(target, "_last_value", new_value)

        if old_value != new_value:
            self.add_checked_undo(target, old_value, new_value, "Alterar seleção")
        target._last_value = new_value

    #--------------------------------------------------------------------------#
    def change_text(self, widget):
        new_text = widget.text() if hasattr(widget, 'text') else widget.toPlainText()
        old_text = getattr(widget, '_last_text', '')

        if new_text != old_text:
            self.add_text_undo(self, widget, old_text, new_text, "Alterar texto")
            widget._last_text = new_text
            self.changed = True

    #--------------------------------------------------------------------------#
    def select_icon(self):
        path_icons = self.path_resources / 'icons'
        fname = self.get_open_fname('Escolha um Icone', path_icons, 'png')
        
        if fname:
            label = self.ui.label_GameIcon 

            old_image = getattr(self, 'icon_image', '')
            tools.path_image_to_label(label, fname)
            new_image = label.pixmap().toImage()

            self.add_image_undo(label, old_image, new_image, "Alterar imagem do icone")
            self.icons_image = new_image
            self.changed = True

    #--------------------------------------------------------------------------#
    def select_ambience_sound(self):
        path_sounds = self.path_resources/'sounds'
        fname = self.get_open_fname('Escolha um som ambiente', path_sounds, 'mp3')
    
        if fname:
            controller = self
            old_sound=self.model.meta.game_ambience
            new_sound=fname
            old_volume=self.model.meta.game_ambience_volume
            new_volume=self.ui.doubleSpinBox_AmbienceSoundVolume.value()
            
            self.add_sound_undo(controller, old_sound, new_sound, old_volume, new_volume, "Alterar som ambiente")
            self.changed = True
    
    #--------------------------------------------------------------------------#
    def ambience_remove(self):
        controller = self
        old_sound=self.model.meta.game_ambience
        new_sound=None
        old_volume=self.model.meta.game_ambience_volume
        new_volume=0.5

        self.add_sound_undo(controller, old_sound, new_sound, old_volume, new_volume, "Remover som ambiente")
    
        self.audio_manager.stop()
        self.changed = True

    #--------------------------------------------------------------------------#
    def ambience_play(self):
        if hasattr(self.model.meta, 'game_ambience') and self.model.meta.game_ambience:
            volume = self.ui.doubleSpinBox_AmbienceSoundVolume.value()
        
            # Verifica se é um BytesIO ou um caminho de arquivo
            if isinstance(self.model.meta.game_ambience, BytesIO):
                self.audio_manager.load_sound(self.model.meta.game_ambience)
            else:
                sound_path = self.path_resources / str(self.model.meta.game_ambience)
                self.audio_manager.load_sound(sound_path)
        
            self.audio_manager.play(loop=True, volume=volume)
            # Agenda para parar a música após 10 segundos (10.000 milissegundos)
            timer = QTimer(self.win)
            timer.setSingleShot(True)
            timer.timeout.connect(self.audio_manager.stop)
            timer.start(10000)
            self.changed = False

    #--------------------------------------------------------------------------#
    def ambience_set_volume(self, volume):
        self.audio_manager.set_volume(volume)
        if hasattr(self.model.meta, 'game_ambience_volume'):
            self.model.meta.game_ambience_volume = volume
    
    #--------------------------------------------------------------------------#
    def cleanup(self):
        self.audio_manager.cleanup()

    #--------------------------------------------------------------------------#
    def obstacles_frequency_changed(self):
        pass

    #--------------------------------------------------------------------------#
    def collectibles_frequency_changed(self):
        pass

    #--------------------------------------------------------------------------#
    def new_obstacle_widget(self):

        widget = ObjectWidget(self.obstacles_area)

        self.obstacles_box.insertWidget(self.num_obstacles, widget)

        bar = self.obstacles_area.verticalScrollBar()
        bar.setValue(bar.maximum())

        self.obstacles.append(widget)
        self.num_obstacles += 1

        return widget

    #--------------------------------------------------------------------------#
    def new_collectible_widget(self):

        widget = ObjectWidget(self.collectibles_area)

        self.collectibles_box.insertWidget(self.num_collectibles, widget)

        bar = self.collectibles_area.verticalScrollBar()
        bar.setValue(bar.maximum())

        self.collectibles.append(widget)
        self.num_collectibles += 1

        return widget

    #--------------------------------------------------------------------------#
    def remove_obstacle_widget(self, obj_id):

        item = self.obstacles_box.takeAt(obj_id)
        item.widget().deleteLater()

        self.obstacles.pop(obj_id)
        self.num_obstacles -= 1

    #--------------------------------------------------------------------------#
    def remove_collectible_widget(self, obj_id):

        item = self.collectibles_box.takeAt(obj_id)
        item.widget().deleteLater()

        self.collectibles.pop(obj_id)
        self.num_collectibles -= 1

    #--------------------------------------------------------------------------#
    def function_velocity_changed(self):

        func = self.ui.lineEdit_FunctionVelocity.text()
        old_text = getattr(self.ui.lineEdit_FunctionVelocity, "_last_text", "")
        
        self.add_text_undo(self, self.ui.lineEdit_FunctionVelocity, old_text, func, "Alterar velocidade")
        try:
            self.model.change_velocity_function(func)
            self.plot_velocity.update_velocity(
                self.model.get_velocity_function()
            )
        except(KeyError):
            QMessageBox.critical(None, "Erro", f"O texto contem variaveis diferentes de t")
            self.ui.lineEdit_FunctionVelocity.setText(old_text)
            return
        except(SyntaxError):
            QMessageBox.critical(None, "Erro", f"A operação digitada não exite")
            self.ui.lineEdit_FunctionVelocity.setText(old_text)
            return
        except(ZeroDivisionError):
            QMessageBox.critical(None, "Erro", f"Não é permitido Divisões por 0")
            self.ui.lineEdit_FunctionVelocity.setText(old_text)
            return
        self.ui.lineEdit_FunctionVelocity._last_text = func


    #--------------------------------------------------------------------------#
    def function_track_minimum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMinimum.text()
        old_text = getattr(self.ui.lineEdit_FunctionTrackMinimum, "_last_text", "")
        self.add_text_undo(self, self.ui.lineEdit_FunctionTrackMinimum, old_text, func, "Alterar mínimo")
        
        try:
            self.model.change_track_minimum_function(func)
            self.plot_track.update_boundary(
            self.model.get_boundary_functions()
            )
        except(KeyError):
            QMessageBox.critical(None, "Erro", f"O texto contem variaveis diferentes de x")
            self.ui.lineEdit_FunctionTrackMinimum.setText(old_text)
            return
        except(SyntaxError):
            QMessageBox.critical(None, "Erro", f"A operação digitada não exite")
            self.ui.lineEdit_FunctionTrackMinimum.setText(old_text)
            return
        except(ZeroDivisionError):
            QMessageBox.critical(None, "Erro", f"Não é permitido Divisões por 0")
            self.ui.lineEdit_FunctionTrackMinimum.setText(old_text)
            return
        
        self.ui.lineEdit_FunctionTrackMinimum._last_text = func


    #--------------------------------------------------------------------------#
    def function_track_maximum_changed(self):
        func = self.ui.lineEdit_FunctionTrackMaximum.text()
        old_text = getattr(self, self.ui.lineEdit_FunctionTrackMaximum, "_last_text", "")

        self.add_text_undo(self.ui.lineEdit_FunctionTrackMaximum, old_text, func, "Alterar máximo")
        try:
            self.model.change_track_maximum_function(func)
            self.plot_track.update_boundary(
            self.model.get_boundary_functions()
            )
        except(KeyError):
            QMessageBox.critical(None, "Erro", f"O texto contem variaveis diferentes de x")
            self.ui.lineEdit_FunctionTrackMaximum.setText(old_text)
            return
        except(SyntaxError):
            QMessageBox.critical(None, "Erro", f"A operação digitada não exite")
            self.ui.lineEdit_FunctionTrackMaximum.setText(old_text)
            return
        except(ZeroDivisionError):
            QMessageBox.critical(None, "Erro", f"Não é permitido Divisões por 0")
            self.ui.lineEdit_FunctionTrackMaximum.setText(old_text)
            return
  
        self.ui.lineEdit_FunctionTrackMaximum._last_text = func

    #--------------------------------------------------------------------------#
    # Internal tasks
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def start_new(self):
        self.model.new()
        self.ui.tabWidget_Game   .setCurrentIndex(0)
        self.ui.tabWidget_Objects.setCurrentIndex(0)
        self.start_view_from_model()

    #--------------------------------------------------------------------------#
    def start_view_from_model(self):

        #self.ui.tabWidget_Game   .setCurrentIndex(0)
        #self.ui.tabWidget_Objects.setCurrentIndex(0)

        self.ui.doubleSpinBox_AmbienceSoundVolume.setEnabled(False)
        self.model.update_ui()

        self.plot_velocity.update_velocity(
            self.model.get_velocity_function()
        )
        self.plot_track.update_boundary(
            self.model.get_boundary_functions()
        )

        self.changed = False

    #--------------------------------------------------------------------------#
    def confirm_deletion(self):
        if self.changed:
            return False
        return True

    #--------------------------------------------------------------------------#
    def block_ui(self):
        pass

    #--------------------------------------------------------------------------#
    def clear_obstacle_widgets(self):
        nn = self.num_obstacles
        for _ in range(nn):
            self.remove_obstacle_widget(0)

    #--------------------------------------------------------------------------#
    def clear_collectible_widgets(self):
        nn = self.num_collectibles
        for _ in range(nn):
            self.remove_collectible_widget(0)

    #--------------------------------------------------------------------------#
    # Tools
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def error_box( self, title, message ):
        QMessageBox.critical( self.win, title, message,
                              buttons=QMessageBox.StandardButton.Ok )

    #--------------------------------------------------------------------------#
    def get_open_fname( self, title, path, ext ):
        fname, _ = QFileDialog.getOpenFileName( parent  = self.win,
                                                caption = title,
                                                dir     = str(path),
                                                filter  = '*.' + ext )
        return fname

    #--------------------------------------------------------------------------#
    def get_save_fname( self, title, ext, suggestion = '' ):

        if not suggestion:
            suggestion = self.last_dir

        fname, _ = QFileDialog.getSaveFileName( parent  = self.win,
                                                caption = title,
                                                dir     = suggestion,
                                                filter  = '*.' + ext )
        if fname:
            ee = '.' + ext
            nn = len(ee)
            if len(fname) < nn or fname[-nn:] != ee:
                fname += ee

        return fname
    #--------------------------------------------------------------------------#
    def add_image_undo(self, label, old_image, new_image, description):
        command = ChangeImageCommand(label, old_image, new_image, description)
        stack = self.undo_group.activeStack()
        stack.push(command)
        
    #--------------------------------------------------------------------------#
    def add_value_undo(self, target, old_value, new_value, description):
        command = ChangeValueCommand(target, old_value, new_value, self, description)
        stack = self.undo_group.activeStack()
        stack.push(command)
        
    #--------------------------------------------------------------------------#
    def add_checked_undo(self, target, old_value, new_value, description):
        command = ChangeCheckedCommand(target, old_value, new_value, self, description)
        stack = self.undo_group.activeStack()
        stack.push(command)
    
     #--------------------------------------------------------------------------#
    def add_sound_undo(self, controller, old_sound, new_sound, old_volume, new_volume, description):
        command = ChangeSoundCommand(controller, old_sound, new_sound, old_volume, new_volume, description)
        stack = self.undo_group.activeStack()
        stack.push(command)

    #--------------------------------------------------------------------------#
    def add_text_undo(self, controller, widget, old_text, new_text, description): 
        command = ChangeTextCommand(controller, widget, old_text, new_text, description)
        stack = self.undo_group.activeStack()
        stack.push(command)


#------------------------------------------------------------------------------#
