#------------------------------------------------------------------------------#

import sys, tempfile
import numpy as np

from PySide6.QtCore       import QProcess, QUrl
from PySide6.QtGui        import QPixmap, QFont
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from pathlib import Path

import parameters as par
import ui.tools   as tools

from world.meta_world import MetaWorld

#------------------------------------------------------------------------------#
class MainModel:

    #--------------------------------------------------------------------------#
    def __init__(self, controler):

        self.meta = MetaWorld()

        self.con = controler
        self.win = controler.win
        self.ui  = controler.win.ui

    #--------------------------------------------------------------------------#
    def new(self):
        self.meta = MetaWorld()

    #--------------------------------------------------------------------------#
    def open(self, filename):
        self.meta = MetaWorld.load(filename)

    #--------------------------------------------------------------------------#
    def save(self, filename):
        self.meta.save(filename)

    #--------------------------------------------------------------------------#
    def run(self):

        temp = tempfile.NamedTemporaryFile( prefix='meta_', suffix='.game' )
        name = str(temp.name)

        self.meta.save(name)

        run_game = str(Path(__file__).parents[1]/'game'/'run_game.py')

        self.p = QProcess()
        self.p.execute(sys.executable, [run_game, name])

    #--------------------------------------------------------------------------#
    def ambience_play(self):

        tools.play_sound(self.win,
                         self.meta.game_ambience,
                         self.meta.game_ambience_volume)

    #--------------------------------------------------------------------------#
    def start_view(self):

      self.start_view_tab_game      ()
      self.start_view_tab_appearence()
      self.start_view_tab_objects   ()
      self.start_view_tab_velocity  ()
      self.start_view_tab_margins   ()

    #--------------------------------------------------------------------------#
    def start_view_tab_game(self):

        ui   = self.ui
        meta = self.meta

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
    def start_view_tab_appearence(self):

        ui   = self.ui
        meta = self.meta

        #--- Background -------------------------------------------------------#

        tools.draw_meta_image(ui.label_BackgroundImage, meta.background_image)

        ui.checkBox_BackgroundImageScrolls.setChecked(meta.background_scrolls)

        #--- Track ------------------------------------------------------------#

        tools.draw_meta_image(ui.label_TrackImage, meta.track_image)

        if meta.track_image:
            ui.checkBox_DrawTrack         .setChecked(True)
            ui.pushButton_SelectTrackImage.setEnabled(True)

        else:
            ui.checkBox_DrawTrack         .setChecked(False)
            ui.pushButton_SelectTrackImage.setEnabled(False)

        #--- Scoreboard -------------------------------------------------------#

        score = meta.scoreboard

        tools.draw_meta_image(ui.label_ScoreboardImage, score.image)

        pos = score.text_position
        ui.spinBox_ScoreboardTextPositionX.setValue(pos[0])
        ui.spinBox_ScoreboardTextPositionY.setValue(pos[1])

        if score.image:
            pos  = score.image_position
            size = score.image.size
            ui.spinBox_ScoreboardImagePositionX.setValue(pos [0])
            ui.spinBox_ScoreboardImagePositionY.setValue(pos [1])
            ui.spinBox_ScoreboardImageHeight   .setValue(size[0])
            ui.spinBox_ScoreboardImageWidth    .setValue(size[1])

        ui.checkBox_ScoreboardImageKeepAspectRatio.setChecked(True)

        css = 'color: rgb({},{},{});'.format(*(score.text_fgcolor))

        if score.text_bgcolor:
            css += ' background-color: rgb({},{},{});'.format(*(score.text_bgcolor))

        ui.label_ScoreboardExample.setStyleSheet(f'QLabel{{ {css} }}')
        ui.label_ScoreboardExample.setFont(QFont('Times', score.text_font_size))

    #--------------------------------------------------------------------------#
    def start_view_tab_objects(self):

        ui   = self.ui
        con  = self.con
        meta = self.meta

        #--- Player -----------------------------------------------------------#

        player = meta.player

        tools.draw_meta_image(ui.label_PlayerImage, player.image)

        ui.spinBox_PlayerWidth. setValue(player.image.size[0])
        ui.spinBox_PlayerHeight.setValue(player.image.size[1])
        ui.spinBox_PlayerSpeed .setValue(meta.player_speed)

        ui.checkBox_PlayerKeepAspectRatio.setChecked(True)

        #--- Obstacles---------------------------------------------------------#

        ui.doubleSpinBox_ObstaclesFrequency.setValue(meta.obstacles_frequency)

        con.clear_obstacle_widgets()

        for meta_op in meta.obstacles:
            con.new_obstacle_widget().meta_to_object(meta_op)

        #--- Collectibles -----------------------------------------------------#

        ui.doubleSpinBox_CollectiblesFrequency.setValue(meta.collectibles_frequency)

        con.clear_collectible_widgets()

        for meta_op in meta.collectibles:
            con.new_collectible_widget().meta_to_object(meta_op)

    #--------------------------------------------------------------------------#
    def start_view_tab_velocity(self):

        ui   = self.ui
        meta = self.meta

        ui.lineEdit_FunctionVelocity.setText( meta.velocity.get_function() )

        tt = np.arange(0, par.PLOT_MAX_T, 0.1)
        vv = meta.velocity.eval(tt)

        self.con.plot_velocity_data.setData(tt, vv)

    #--------------------------------------------------------------------------#
    def start_view_tab_margins(self):

        ui   = self.ui
        meta = self.meta

        ui.lineEdit_FunctionTrackMinimum.setText( meta.margins.get_function_min() )
        ui.lineEdit_FunctionTrackMaximum.setText( meta.margins.get_function_max() )

        xx     = np.arange(0, par.PLOT_MAX_X, 0.1)
        mm, MM = meta.margins.eval(xx)

        self.con.plot_margin_min_data.setData(xx, mm)
        self.con.plot_margin_max_data.setData(xx, MM)

        self.update_track_aux_function()

    #--------------------------------------------------------------------------#
    def update_velocity_function(self, func):

        self.meta.velocity.set_function          (func)
        self.ui.lineEdit_FunctionVelocity.setText(func)

        tt = np.arange(0, par.PLOT_MAX_T, 0.1)
        vv = self.meta.velocity.eval(tt)

        self.con.plot_velocity_data.setData(tt, vv)
        self.update_track_aux_function()

    #--------------------------------------------------------------------------#
    def update_track_minimum_function(self, func):

        self.meta.margins.set_function_min           (func)
        self.ui.lineEdit_FunctionTrackMinimum.setText(func)

        xx = np.arange(0, par.PLOT_MAX_X, 0.1)
        mm = self.meta.margins.eval_min(xx)

        self.con.plot_margin_min_data.setData(xx, mm)
        self.update_track_aux_function()

    #--------------------------------------------------------------------------#
    def update_track_maximum_function(self, func):

        self.meta.margins.set_function_max           (func)
        self.ui.lineEdit_FunctionTrackMaximum.setText(func)

        xx = np.arange(0, par.PLOT_MAX_X, 0.1)
        MM = self.meta.margins.eval_max(xx)

        self.con.plot_margin_max_data.setData(xx, MM)
        self.update_track_aux_function()

    #--------------------------------------------------------------------------#
    def update_track_aux_function(self):

        xx = self.con.plot_margin_min_data.xData

        y_aux = np.maximum(self.con.plot_margin_min_data.yData,
                           self.con.plot_margin_max_data.yData)

        self.con.plot_margin_aux_data.setData(xx, y_aux)

#------------------------------------------------------------------------------#
