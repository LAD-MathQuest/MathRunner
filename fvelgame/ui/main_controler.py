#------------------------------------------------------------------------------#

from PySide6.QtGui     import QPixmap, QPalette
from PySide6.QtWidgets import (QApplication, 
                               QFileDialog, 
                               QMessageBox)
import pyqtgraph  as pg
import parameters as par

from ui.main_model  import MainModel

PLOT_MAX_TIME = 5

#------------------------------------------------------------------------------#
def draw_meta_image(label, meta):

    label.setStyleSheet('')
    label.clear()

    if meta:
       if meta.path:
           pixmap = QPixmap(meta.path)
           label.setPixmap(pixmap)
       else:
           bg = 'rgb({},{},{})'.format(*(meta.color))
           label.setStyleSheet(f'QLabel{{background-color:{bg};}}')

#------------------------------------------------------------------------------#
class MainControler:

    #--------------------------------------------------------------------------#
    def __init__(self, window):

        self.model = MainModel(window)
        self.win   = window
        self.ui    = window.ui

        self.init_plots()

        self.last_dir  = str(par.HOME)
        self.file_name = ''
        self.start_new()

        self.connect_signals_and_slots()

    #--------------------------------------------------------------------------#
    def init_plots(self):

        pv = self.ui.plotVelocity
        pm = self.ui.plotMargins

        # Get the default window background,
        color = self.win.palette().color(QPalette.Window)  

        pv.setBackground(color)
        pv.setTitle('Velocity')
        pv.setLabel('left',   'Velocity (screens/second)')
        pv.setLabel('bottom', 'Time (seconds)'           )
        pv.showGrid(x=True, y=True)
        pv.setXRange(0, PLOT_MAX_TIME, padding=0)
        pv.setYRange(0, 1,             padding=0)

        pen = pg.mkPen(color=(0, 0, 255), width=2)
        self.plot_velocity_data = pv.plot((0, PLOT_MAX_TIME), (0.5, 0.5), pen=pen)

        pm.setBackground(color)
        pm.setTitle('Margins' )
        pm.setLabel('left',   'Margins (screen fraction)')
        pm.setLabel('bottom', 'Time (seconds)'           )
        pm.showGrid(x=True, y=True)
        pm.setXRange(0, PLOT_MAX_TIME, padding=0)
        pm.setYRange(0, 1,             padding=0)

        pen = pg.mkPen(color=(0, 0, 255), width=2)
        self.plot_margin_min_data = pm.plot((0, PLOT_MAX_TIME), (0.3, 0.3), pen=pen)

        pen = pg.mkPen(color=(255, 0, 255), width=2)
        self.plot_margin_max_data = pm.plot((0, PLOT_MAX_TIME), (0.7, 0.7), pen=pen)

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

    #--------------------------------------------------------------------------#
    # Action calls
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def new(self):

        if self.confirm_deletion():
            self.file_name = ''
            self.start_new()

    #--------------------------------------------------------------------------#
    def open(self):

        if self.confirm_deletion():

            path  = par.RESOURCES / 'games' 
            fname = self.get_open_fname('Chose a game description', path, 'game' )

            if fname:
                # TODO try:
                self.file_name = fname
                self.model.open(self.file_name)
                self.changed = False
                self.update()

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

    #--------------------------------------------------------------------------#
    def ambience_play(self):
        self.model.ambience_play()

    #--------------------------------------------------------------------------#
    # Internal tools
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def start_new(self):
        self.model.new()
        self.changed = False
        self.update()

    #--------------------------------------------------------------------------#
    def confirm_deletion(self):

        if self.changed:
            return False

        return True

    #--------------------------------------------------------------------------#
    def block_ui(self):
        pass

    #--------------------------------------------------------------------------#
    def update(self):

      self.update_game_tab      ()
      self.update_appearence_tab()
      self.update_object_tab    ()
      self.update_velocity_tab  ()
      self.update_margins_tab   ()

    #--------------------------------------------------------------------------#
    def update_game_tab(self):

        ui   = self.ui
        meta = self.model.meta

        ui.lineEdit_GameName.setText(meta.soft_name)
        ui.lineEdit_Author  .setText(meta.soft_author)

        ui.label_GameIcon.clear()
        ui.plainTextEdit_GameDescription.setPlainText(meta.soft_description)

        if meta.game_vertical:
            ui.radioButton_VertialScrolling.setChecked(True)
        else:
            ui.radioButton_HorizontalScrolling.setChecked(True)

        ui.checkBox_TrackKills.setChecked(meta.track_boundaries_kill)
        ui.doubleSpinBox_ScoreTimeBonus.setValue(meta.game_time_bonus)

        if meta.game_ambience:
            ui.pushButton_AmbienceSoundRemove.setEnabled(True)
            ui.pushButton_AmbienceSoundPlay  .setEnabled(True)
        else:
            ui.pushButton_AmbienceSoundRemove.setEnabled(False)
            ui.pushButton_AmbienceSoundPlay  .setEnabled(False)

    #--------------------------------------------------------------------------#
    def update_appearence_tab(self):

        ui   = self.ui
        meta = self.model.meta

        #--- Background -------------------------------------------------------#
        
        draw_meta_image(ui.label_BackgroundImage, meta.background_image)

        ui.checkBox_BackgroundScrolls.setChecked(meta.background_scrolls)

        #--- Track ------------------------------------------------------------#

        draw_meta_image(ui.label_TrackImage, meta.track_image)

        if meta.track_image:
            ui.checkBox_DrawTrack    .setChecked(True)
            ui.pushButton_SelectTrack.setEnabled(True)

        else:
            ui.checkBox_DrawTrack    .setChecked(False)
            ui.pushButton_SelectTrack.setEnabled(False)

        #--- Scoreboard -------------------------------------------------------#

        score = meta.scoreboard

        draw_meta_image(ui.label_ScoreboardImage, score.image)

        rect = score.text_rect
        ui.spinBox_ScoreboardTextPositionX.setValue(rect[0])
        ui.spinBox_ScoreboardTextPositionY.setValue(rect[1])
        ui.spinBox_ScoreboardTextHeight   .setValue(rect[2])
        ui.spinBox_ScoreboardTextWidth    .setValue(rect[3])

        pos  = score.image_position
        size = score.image.size    
        ui.spinBox_ScoreboardImagePositionX.setValue(pos [0])
        ui.spinBox_ScoreboardImagePositionY.setValue(pos [1])
        ui.spinBox_ScoreboardImageHeight   .setValue(size[0])
        ui.spinBox_ScoreboardImageWidth    .setValue(size[1])
        
        ui.checkBox_ScoreboardImageKeepAspectRatio.setChecked(True)

        bg = 'background-color: rgb({},{},{});'.format(*(score.text_bgcolor))
        fg = 'color:            rgb({},{},{});'.format(*(score.text_fgcolor))
        ui.label_ScoreboardExample.setStyleSheet(f'QLabel{{ {bg} {fg} }}')

    #--------------------------------------------------------------------------#
    def update_object_tab(self):

        ui   = self.ui
        meta = self.model.meta

        #--- Player -----------------------------------------------------------#

        player = meta.player

        draw_meta_image(ui.label_PlayerImage, player.image)

        ui.spinBox_PlayerWidth. setValue(player.image.size[0])
        ui.spinBox_PlayerHeight.setValue(player.image.size[1])
        ui.spinBox_PlayerSpeed .setValue(meta.player_speed)
        
        ui.checkBox_PlayerKeepAspectRatio.setChecked(True)

    #--------------------------------------------------------------------------#
    def update_velocity_tab(self):

        ui    = self.ui
        model = self.model
        meta  = model.meta

        ui.doubleSpinBox_VelocityA.setValue(meta.velocity.a)
        ui.doubleSpinBox_VelocityB.setValue(meta.velocity.b)

        tt, vv = model.eval_velocity(0, PLOT_MAX_TIME)

        self.plot_velocity_data.setData(tt, vv)

    #--------------------------------------------------------------------------#
    def update_margins_tab(self):

        ui    = self.ui
        model = self.model
        meta  = model.meta

        ui.doubleSpinBox_MarginLeft .setValue(meta.margins.const_min)
        ui.doubleSpinBox_MarginRight.setValue(meta.margins.const_max)

        tt, ll, rr = model.eval_margins(0, PLOT_MAX_TIME)

        self.plot_margin_min_data.setData(tt, ll)
        self.plot_margin_max_data.setData(tt, rr)

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
