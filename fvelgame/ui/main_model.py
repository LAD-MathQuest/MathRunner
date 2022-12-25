#------------------------------------------------------------------------------#

import sys, os, tempfile

from PySide6.QtCore       import QUrl
from PySide6.QtGui        import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from pathlib import Path

import parameters as par
from world.meta_world import MetaWorld

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
def play_sound(parent, path, vol):

    player      = QMediaPlayer(parent)
    audioOutput = QAudioOutput(parent)

    player.setAudioOutput(audioOutput)
    player.setSource     (QUrl.fromLocalFile(str(path)))
    
    audioOutput.setVolume(vol)
    
    player.play()

#------------------------------------------------------------------------------#
class MainModel:
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
        pass

    #--------------------------------------------------------------------------#
    def run(self):

        temp = tempfile.NamedTemporaryFile( prefix='meta_', suffix='.game' )
        name = str(temp.name)

        self.meta.save(name)

        run_game = str(Path(__file__).parents[1]/'game'/'run_game.py')

        # TODO replace by QProcess
        # https://www.pythonguis.com/tutorials/qprocess-external-programs
        os.system( f'{sys.executable} {run_game} {name}')

    #--------------------------------------------------------------------------#
    def ambience_play(self):

        play_sound(self.win,
                   self.meta.game_ambience, 
                   self.meta.game_ambience_volume)

    #--------------------------------------------------------------------------#
    def eval_velocity(self, t_min, t_max ):

        tt = (t_min, t_max)
        vv = (self.meta.velocity.eval(tt[0]), self.meta.velocity.eval(tt[1]))

        return (tt, vv)

    #--------------------------------------------------------------------------#
    def eval_margins(self, t_min, t_max ):

        tt = (t_min, t_max)
        ll = (self.meta.margins.eval_min(tt[0]), self.meta.margins.eval_min(tt[1]))
        rr = (self.meta.margins.eval_max(tt[0]), self.meta.margins.eval_max(tt[1]))

        return (tt, ll, rr)

    #--------------------------------------------------------------------------#
    def meta_to_view(self):

      self.meta_to_view_game_tab      ()
      self.meta_to_view_appearence_tab()
      self.meta_to_view_object_tab    ()
      self.meta_to_view_velocity_tab  ()
      self.meta_to_view_margins_tab   ()

    #--------------------------------------------------------------------------#
    def meta_to_view_game_tab(self):

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
    def meta_to_view_appearence_tab(self):

        ui   = self.ui
        meta = self.meta

        #--- Background -------------------------------------------------------#
        
        draw_meta_image(ui.label_BackgroundImage, meta.background_image)

        ui.checkBox_BackgroundImageScrolls.setChecked(meta.background_scrolls)

        #--- Track ------------------------------------------------------------#

        draw_meta_image(ui.label_TrackImage, meta.track_image)

        if meta.track_image:
            ui.checkBox_DrawTrack         .setChecked(True)
            ui.pushButton_SelectTrackImage.setEnabled(True)

        else:
            ui.checkBox_DrawTrack         .setChecked(False)
            ui.pushButton_SelectTrackImage.setEnabled(False)

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
    def meta_to_view_object_tab(self):

        ui   = self.ui
        con  = self.con
        meta = self.meta

        #--- Player -----------------------------------------------------------#

        player = meta.player

        draw_meta_image(ui.label_PlayerImage, player.image)

        ui.spinBox_PlayerWidth. setValue(player.image.size[0])
        ui.spinBox_PlayerHeight.setValue(player.image.size[1])
        ui.spinBox_PlayerSpeed .setValue(meta.player_speed)
        
        ui.checkBox_PlayerKeepAspectRatio.setChecked(True)

        #--- Obstacles---------------------------------------------------------#

        ui.doubleSpinBox_ObsctaclesFrequency.setValue(meta.obstacles_frequency)

        con.clear_obstacle_widgets()

        for ob in meta.obstacles:
            label = con.new_obstacle_widget()
            draw_meta_image(label, ob.image)

        #--- Collectibles -----------------------------------------------------#
        
        ui.doubleSpinBox_CollectiblesFrequency.setValue(meta.collectibles_frequency)

        con.clear_collectible_widgets()

        for ob in meta.collectibles:
            label = con.new_collectible_widget()
            draw_meta_image(label, ob.image)

    #--------------------------------------------------------------------------#
    def meta_to_view_velocity_tab(self):

        ui    = self.ui
        meta  = self.meta

        ui.doubleSpinBox_VelocityA.setValue(meta.velocity.a)
        ui.doubleSpinBox_VelocityB.setValue(meta.velocity.b)

        tt, vv = self.eval_velocity(0, par.PLOT_MAX_TIME)

        self.con.plot_velocity_data.setData(tt, vv)

    #--------------------------------------------------------------------------#
    def meta_to_view_margins_tab(self):

        ui    = self.ui
        meta  = self.meta

        ui.doubleSpinBox_MarginLeft .setValue(meta.margins.const_min)
        ui.doubleSpinBox_MarginRight.setValue(meta.margins.const_max)

        tt, ll, rr = self.eval_margins(0, par.PLOT_MAX_TIME)

        self.con.plot_margin_min_data.setData(tt, ll)
        self.con.plot_margin_max_data.setData(tt, rr)

#------------------------------------------------------------------------------#
