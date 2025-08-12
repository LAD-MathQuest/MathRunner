#------------------------------------------------------------------------------#

from PySide6.QtGui     import QPalette, QPixmap, QUndoCommand, QUndoGroup, QUndoStack
from PySide6.QtWidgets import (QApplication,
                               QFileDialog,
                               QMessageBox,
                               QVBoxLayout,
                               QTabWidget)
from PySide6.QtCore import Qt

from . import parameters
from . import tools

from pathlib import Path

from .main_model    import MainModel
from .object_widget import ObjectWidget
from .plot_velocity import PlotVelocity
from .plot_track    import PlotTrack

import sys

from PySide6.QtGui import QUndoCommand, QPixmap
from PySide6.QtCore import Qt
from pathlib import Path

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

#------------------------------------------------------------------------------#
class MainController:

    path_resources = Path(__file__).parents[1]/'examples/resources'

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.win = window
        self.ui  = window.ui

        self.model = MainModel(self)
        
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
        
        #Criação do Undo Group
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
        ui.action_Save.triggered.connect(self.save)
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

        # ui.lineEdit_GameName
        # ui.lineEdit_Author
        # ui.pushButton_IconSelect
        # ui.plainTextEdit_GameDescription
        # ui.radioButton_HorizontalScrolling
        # ui.radioButton_VerticalScrolling
        # ui.checkBox_TrackKills
        # ui.doubleSpinBox_ScoreTimeBonus
        # ui.pushButton_AmbienceSoundSelect
        # ui.pushButton_AmbienceSoundRemove
        ui.pushButton_AmbienceSoundPlay.clicked.connect( self.ambience_play )
        # ui.doubleSpinBox_AmbienceSoundVolume

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
        ui.spinBox_PlayerWidth.valueChanged.connect(self.update_image_size)
        ui.spinBox_PlayerHeight.valueChanged.connect(self.update_image_size)
        ui.checkBox_PlayerKeepAspectRatio.stateChanged.connect(self.update_image_size)
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

        if not self.file_name:
            self.save_as()

        elif self.changed:
            self.model.save( self.file_name )
            self.changed = False

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

    def select_scoreboard_image(self):
        path_backgrounds = self.path_resources/'scoreboards'
        fname = self.get_open_fname('Escolha uma Imagem', path_backgrounds, 'png')
        if fname:
            self.background_image = Path(fname)

            pixmap = QPixmap(str(self.background_image))
            pixmap = pixmap.scaled(228, 128, Qt.KeepAspectRatio)
            
            self.ui.label_BackgroundImage.setPixmap(pixmap)
            self.changed = True

    def select_player_image(self):
        path_icon = self.path_resources / 'icons'
        fname = self.get_open_fname('Escolha uma Imagem', path_icon, 'png')
        
        if fname:
            label = self.ui.label_PlayerImage

            old_image = getattr(self, 'player_image', '')
            
            tools.path_image_to_label(label, fname)

            new_image = label.pixmap().toImage()
            
            self.add_image_undo(label, old_image, new_image, "Alterar imagem do fundo")
            self.player_image = new_image
            self.changed = True

    def update_image_size(self):    
        width = self.ui.spinBox_PlayerWidth.value()
        height = self.ui.spinBox_PlayerHeight.value()
        keep = self.ui.checkBox_PlayerKeepAspectRatio.isChecked()

        if hasattr(self, "player_image") and not self.player_image.isNull():
            pixmap = QPixmap.fromImage(self.player_image)

            if keep:
                pixmap = pixmap.scaledToWidth(width)
            else:
                pixmap = pixmap.scaled(width, height)

            self.ui.label_PlayerImage.setPixmap(pixmap)
    
    #--------------------------------------------------------------------------#
    def ambience_play(self):
        pass
        # tools.play_sound(self.win,
        #                  self.model.meta.game_ambience,
        #                  self.model.meta.game_ambience_volume)

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
        self.model.change_velocity_function(func)
        self.plot_velocity.update_velocity(
            self.model.get_velocity_function()
        )

    #--------------------------------------------------------------------------#
    def function_track_minimum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMinimum.text()
        self.model.change_track_minimum_function(func)
        self.plot_track.update_boundary(
            self.model.get_boundary_functions()
        )

    #--------------------------------------------------------------------------#
    def function_track_maximum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMaximum.text()
        self.model.change_track_maximum_function(func)
        self.plot_track.update_boundary(
            self.model.get_boundary_functions()
        )

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
        

#------------------------------------------------------------------------------#
