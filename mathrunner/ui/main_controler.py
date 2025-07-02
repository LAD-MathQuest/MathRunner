#------------------------------------------------------------------------------#

import numpy as np

from PySide6.QtGui     import QPalette
from PySide6.QtWidgets import (QApplication,
                               QFileDialog,
                               QMessageBox,
                               QVBoxLayout,
                               QLabel)
import pyqtgraph  as pg
import parameters as par

from ui.main_model    import MainModel
from ui.object_widget import ObjectWidget

from world.meta_world import MetaWorld, MetaImage, MetaObject, MetaScoreboard
from world.game_world import GameWorld, GameObjectParam

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


from pathlib import Path

import threading
import pygame

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.win = window
        self.ui  = window.ui

        self.model = MainModel(self)

        self.init_plots  ()
        self.init_objects()

        self.last_dir  = str(par.HOME)
        self.file_name = ''
        self.start_new()

        self.connect_signals_and_slots()

    #--------------------------------------------------------------------------#
    def init_plots(self):

        pv = self.ui.plotVelocity
        pm = self.ui.plotBoundary

        # Get the default window background
        color = self.win.palette().color(QPalette.Window)

        pv.setBackground(color)
        pv.setTitle('Velocity')
        pv.setLabel('left',   'Velocity (screens/second)')
        pv.setLabel('bottom', 'Time (seconds)'           )
        pv.showGrid(x=True, y=True)
        pv.setXRange(0, par.PLOT_MAX_T, padding=0)
        pv.setYRange(0, 1,              padding=0)

        pen = pg.mkPen(color=(0, 0, 255), width=2)
        self.plot_velocity_data = pv.plot((0, par.PLOT_MAX_T), (0.5, 0.5), pen=pen)

        pm.setBackground(color)
        pm.setTitle('Boundary' )
        pm.setLabel('left',   'Boundary (screen fraction)')
        pm.setLabel('bottom', 'Time (seconds)'            )
        pm.showGrid(x=True, y=True)
        pm.setXRange(0, par.PLOT_MAX_X, padding=0)
        pm.setYRange(0, 1,              padding=0)

        pen_min = pg.mkPen(color=(  0, 0, 255), width=2)
        pen_max = pg.mkPen(color=(255, 0, 255), width=2)
        pen_aux = pg.mkPen(None)
        brush   = pg.mkBrush(color=(100, 100, 160))

        p_min = pg.PlotDataItem(np.array((0,par.PLOT_MAX_X)), np.array((0.1, 0.1)), pen=pen_min)
        p_max = pg.PlotDataItem(np.array((0,par.PLOT_MAX_X)), np.array((0.9, 0.9)), pen=pen_max)
        p_aux = pg.PlotDataItem(np.array((0,par.PLOT_MAX_X)), np.array((0.9, 0.9)), pen=pen_aux)
        pfill = pg.FillBetweenItem(p_min, p_aux, brush=brush)

        pm.addItem(p_min)
        pm.addItem(p_max)
        pm.addItem(p_aux)
        pm.addItem(pfill)

        self.plot_boundary_min_data = p_min
        self.plot_boundary_max_data = p_max
        self.plot_boundary_aux_data = p_aux

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
        ##ui.action_Save    .triggered.connect( self.save    )
        ui.action_Save.triggered.connect(self.save)

        ui.action_Save_as .triggered.connect( self.save_as )
        ui.action_Exit    .triggered.connect( self.exit    )
        # ui.action_Undo    .triggered.connect( self.undo    )
        # ui.action_Redo    .triggered.connect( self.redo    )
        # ui.action_Reset   .triggered.connect( self.reset   )
        ui.action_Run.triggered.connect(self.run)
        ui.action_Build   .triggered.connect( self.build   )
        ui.action_About   .triggered.connect( self.about   )
        ui.action_Contents.triggered.connect( self.help    )

        #--- Game Tab signals -------------------------------------------------#

        # ui.lineEdit_GameName
        # ui.lineEdit_Author
        # ui.pushButton_IconSelect
        # ui.plainTextEdit_GameDescription
        # ui.radioButton_HorizontalScrolling
        # ui.radioButton_VertialScrolling
        # ui.checkBox_TrackKills
        # ui.doubleSpinBox_ScoreTimeBonus
        # ui.pushButton_AmbienceSoundSelect
        # ui.pushButton_AmbienceSoundRemove
        ui.pushButton_AmbienceSoundPlay.clicked.connect( self.ambience_play )
        # ui.doubleSpinBox_AmbienceSoundVolume
        #--- Game Tab signals -------------------------------------------------

        ui.pushButton_AmbienceSoundSelect.clicked.connect(self.select_ambience_sound)   
        ui.pushButton_AmbienceSoundRemove.clicked.connect(self.ambience_stop)

        ui.action_Save.setEnabled(True)
        ui.action_Save_as.setEnabled(True)




        #--- Appearance Tab signals -------------------------------------------#

        # ui.pushButton_SelectBackground
        ui.pushButton_SelectBackgroundImage.clicked.connect(self.select_background)
        # ui.checkBox_BackgroundScrolls

        # ui.checkBox_DrawTrack
        # ui.pushButton_SelectTrack

        # ui.pushButton_SelectScoreboardImage
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

        ui.pushButton_NewObstacle   .clicked.connect( self.new_obstacle_widget    )
        ui.pushButton_NewCollectible.clicked.connect( self.new_collectible_widget )

        ui.doubleSpinBox_ObstaclesFrequency   .valueChanged.connect( self.obstacles_frequency_changed    )
        ui.doubleSpinBox_CollectiblesFrequency.valueChanged.connect( self.collectibles_frequency_changed )

        #--- Velocity and Boundary Tabs signals -------------------------------#

        ui.lineEdit_FunctionVelocity    .editingFinished.connect( self.function_velocity_changed      )
        ui.lineEdit_FunctionTrackMinimum.editingFinished.connect( self.function_track_minimum_changed )
        ui.lineEdit_FunctionTrackMaximum.editingFinished.connect( self.function_track_maximum_changed )
       
        


    #--------------------------------------------------------------------------#
    # Action calls

    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def new(self):

        if not self.confirm_deletion():
            return

        self.file_name = ''
        self.start_new()

    #--------------------------------------------------------------------------#
    def open(self):

        if not self.confirm_deletion():
            return

        path  = par.RESOURCES / 'games'
        fname = self.get_open_fname('Chose a game description', path, 'game' )

        if fname:
            # TODO try:
            self.file_name = fname
            self.model.open(self.file_name)
            self.start_view_from_model()

    #--------------------------------------------------------------------------#

    def save(self):
        meta = MetaWorld()

        meta.soft_name = self.ui.lineEdit_GameName.text()
        meta.soft_author = self.ui.lineEdit_Author.text()
        meta.soft_description = self.ui.plainTextEdit_GameDescription.toPlainText()

        if hasattr(self, 'ambience_sound_file'):
            meta.game_ambience = self.ambience_sound_file
            meta.game_ambience_volume = 0.7

        if hasattr(self, 'background_image_file'):
            meta.background_image = MetaImage((1920, 1080), path=self.background_image_file)

        save_path = self.get_save_fname("Salvar jogo", "game", suggestion=str(par.RESOURCES / "games"))

        if save_path:
            meta.save(Path(save_path))
            QMessageBox.information(self.win, "Sucesso", f"Jogo salvo em:\n{save_path}")
            self.changed = False

        self.ui.action_Save.setEnabled(True)



    #--------------------------------------------------------------------------#
    def save_as(self):
        self.file_name = 'get_file_name'
        self.model.save( self.file_name )
        self.changed = False

    #--------------------------------------------------------------------------#
    def exit(self):
        if self.confirm_deletion():
            QApplication.quit()

    #--------------------------------------------------------------------------#
    def run(self):
        self.block_ui()
        self.model.run()

    #--------------------------------------------------------------------------#
    def build(self):
        # self.exe_file_name = 'get_file_name'
        # self.block_ui()
        # self.model.build( self.exe_file_name )
        pass

    #--------------------------------------------------------------------------#
    def about(self):
        QMessageBox.about(self.win, par.TITLE+' - About', par.ABOUT )

    #--------------------------------------------------------------------------#
    def help(self):
        QMessageBox.about(self.win, par.TITLE+' - Help', par.ABOUT )

    #--------------------------------------------------------------------------#
    # Slots
    #--------------------------------------------------------------------------#
    def select_ambience_sound(self):
        path = par.RESOURCES / 'sounds'
        fname = self.get_open_fname('Escolha um som ambiente', path, 'mp3')

        if fname:
            self.ambience_sound_file = fname  
        
        self.ui.pushButton_AmbienceSoundPlay.setEnabled(True)
        self.ui.pushButton_AmbienceSoundRemove.setEnabled(True)

    #--------------------------------------------------------------------------#
    def ambience_play(self):
        
        if hasattr(self, 'ambience_sound_file'):
            pygame.mixer.init()
            pygame.mixer.music.load(str(self.ambience_sound_file))

        # volume da interface
            volume = self.ui.doubleSpinBox_AmbienceSoundVolume.value()
            pygame.mixer.music.set_volume(volume)

            pygame.mixer.music.play(-1)  # -1: loop infinito


    def ambience_stop(self):
        if pygame.mixer.get_init():  # só tenta parar se estiver inicializado
            pygame.mixer.music.stop()
        
        self.ambience_sound_file = None
        self.ui.pushButton_AmbienceSoundPlay.setEnabled(False)
        self.ui.pushButton_AmbienceSoundRemove.setEnabled(False)


    def select_background(self):
        path = par.RESOURCES / 'backgrounds'
        fname = self.get_open_fname('Escolha uma imagem de fundo', path, 'png')

        if fname:
            self.background_image_file = Path(fname).relative_to(par.RESOURCES)

            pixmap = QPixmap(str(par.RESOURCES / self.background_image_file))
            pixmap = pixmap.scaled(228, 128, Qt.KeepAspectRatio)

        self.ui.label_BackgroundImage.setPixmap(pixmap)
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
        self.model.update_velocity_function(func)

    #--------------------------------------------------------------------------#
    def function_track_minimum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMinimum.text()
        self.model.update_track_minimum_function(func)

    #--------------------------------------------------------------------------#
    def function_track_maximum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMaximum.text()
        self.model.update_track_maximum_function(func)

    #--------------------------------------------------------------------------#
    # Internal tasks
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def start_new(self):

        self.model.new()
        self.start_view_from_model()

    #--------------------------------------------------------------------------#
    def start_view_from_model(self):

        self.ui.tabWidget_Game   .setCurrentIndex(0)
        self.ui.tabWidget_Objects.setCurrentIndex(0)

        self.model.start_view()
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

    #-------------------------------------------------------------------------#
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

#------------------------------------------------------------------------------#
