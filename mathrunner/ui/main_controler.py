#------------------------------------------------------------------------------#

from PySide6.QtGui     import QPalette
from PySide6.QtWidgets import (QApplication,
                               QFileDialog,
                               QMessageBox,
                               QVBoxLayout)
import parameters as par

from ui.main_model    import MainModel
from ui.object_widget import ObjectWidget
from ui.plot_velocity import PlotVelocity
from ui.plot_track    import PlotTrack

import ui.tools as tools

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.win = window
        self.ui  = window.ui

        self.model = MainModel(self)

        color = self.win.palette().color(QPalette.Window)

        self.plot_velocity = PlotVelocity(self.ui.plotVelocity, color, self.model.meta.velocity)
        self.plot_track    = PlotTrack   (self.ui.plotBoundary, color, self.model.meta.boundary)

        self.init_objects()

        self.last_dir  = str(par.HOME)
        self.file_name = ''

        self.start_new()

        self.connect_signals_and_slots()

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
        ui.action_Save    .triggered.connect( self.save    )
        ui.action_Save_as .triggered.connect( self.save_as )
        ui.action_Exit    .triggered.connect( self.exit    )
        # ui.action_Undo    .triggered.connect( self.undo    )
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
        # ui.radioButton_VertialScrolling
        # ui.checkBox_TrackKills
        # ui.doubleSpinBox_ScoreTimeBonus
        # ui.pushButton_AmbienceSoundSelect
        # ui.pushButton_AmbienceSoundRemove
        ui.pushButton_AmbienceSoundPlay.clicked.connect( self.ambience_play )
        # ui.doubleSpinBox_AmbienceSoundVolume

        #--- Appearance Tab signals -------------------------------------------#

        # ui.pushButton_SelectBackground
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

        ui.pushButton_NewObstacle   .clicked.connect(self.new_obstacle_widget   )
        ui.pushButton_NewCollectible.clicked.connect(self.new_collectible_widget)

        ui.doubleSpinBox_ObstaclesFrequency.   valueChanged.connect(self.obstacles_frequency_changed   )
        ui.doubleSpinBox_CollectiblesFrequency.valueChanged.connect(self.collectibles_frequency_changed)

        #--- Velocity and Boundary Tabs signals -------------------------------#

        ui.lineEdit_FunctionVelocity    .editingFinished.connect(self.function_velocity_changed     )
        ui.lineEdit_FunctionTrackMinimum.editingFinished.connect(self.function_track_minimum_changed)
        ui.lineEdit_FunctionTrackMaximum.editingFinished.connect(self.function_track_maximum_changed)

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
        self.model.update_from_view()
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

    #--------------------------------------------------------------------------#
    def ambience_play(self):
        tools.play_sound(self.win,
                         self.model.meta.game_ambience,
                         self.model.meta.game_ambience_volume)

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
        self.plot_velocity.update_velocity(self.model.meta.velocity)

    #--------------------------------------------------------------------------#
    def function_track_minimum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMinimum.text()
        self.model.change_track_minimum_function(func)
        self.plot_track.update_boundary(self.model.meta.boundary)

    #--------------------------------------------------------------------------#
    def function_track_maximum_changed(self):

        func = self.ui.lineEdit_FunctionTrackMaximum.text()
        self.model.change_track_maximum_function(func)
        self.plot_track.update_boundary(self.model.meta.boundary)

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

        self.model.update_view()
        self.plot_velocity.update_velocity(self.model.meta.velocity)
        self.plot_track   .update_boundary(self.model.meta.boundary)

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

#------------------------------------------------------------------------------#
