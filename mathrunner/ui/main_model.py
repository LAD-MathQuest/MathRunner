#------------------------------------------------------------------------------#

import sys, tempfile, os
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

        temp = tempfile.NamedTemporaryFile(mode   = 'wb',
                                           prefix = 'meta_',
                                           suffix = '.game',
                                           delete = False)

        self.meta.write(temp)
        temp.close()

        run_game = str(Path(__file__).parents[1]/'game'/'run_game.py')
        name = str(temp.name)

        self.p = QProcess()
        self.p.execute(sys.executable, [run_game, name])

        os.remove(name)

    #--------------------------------------------------------------------------#
    # Funções para atualizar a interface a partir de informações do modelo
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def update_view(self):
        self.update_view_tab_game      ()
        self.update_view_tab_appearence()
        self.update_view_tab_objects   ()
        self.update_view_tab_velocity  ()
        self.update_view_tab_boundary  ()

    #--------------------------------------------------------------------------#
    def update_view_tab_game(self):

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

        ui.checkBox_TrackMinimumKills.setChecked(meta.track_kills[0])
        ui.checkBox_TrackMaximumKills.setChecked(meta.track_kills[1])

        ui.doubleSpinBox_ScoreTimeBonus.setValue(meta.game_time_bonus)

        if meta.game_ambience:
            ui.pushButton_AmbienceSoundRemove.setEnabled(True)
            ui.pushButton_AmbienceSoundPlay  .setEnabled(True)
        else:
            ui.pushButton_AmbienceSoundRemove.setEnabled(False)
            ui.pushButton_AmbienceSoundPlay  .setEnabled(False)

    #--------------------------------------------------------------------------#
    def update_view_tab_appearence(self):

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
    def update_view_tab_objects(self):

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
    def update_view_tab_velocity(self):

        ui   = self.ui
        meta = self.meta

        ui.lineEdit_FunctionVelocity.setText(meta.velocity.get_function_orig())

    #--------------------------------------------------------------------------#
    def update_view_tab_boundary(self):

        ui = self.ui
        boundary = self.meta.boundary

        ui.lineEdit_FunctionTrackMinimum.setText(boundary.get_function_min_orig())
        ui.lineEdit_FunctionTrackMaximum.setText(boundary.get_function_max_orig())

    #--------------------------------------------------------------------------#
    # Atualiza as funções em resposta amudanças na interface
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def change_velocity_function(self, func):
        self.meta.velocity.set_function(func)

    #--------------------------------------------------------------------------#
    def change_track_minimum_function(self, func):
        self.meta.boundary.set_function_min(func)

    #--------------------------------------------------------------------------#
    def change_track_maximum_function(self, func):
        self.meta.boundary.set_function_max(func)


    #--------------------------------------------------------------------------#
    # Atualiza o metaword com os dados da interface
    #--------------------------------------------------------------------------#

    #--------------------------------------------------------------------------#
    def update_from_view(self):

        self.update_from_view_tab_game      ()
        self.update_from_view_tab_appearence()
        self.update_from_view_tab_objects   ()

    #--------------------------------------------------------------------------#
    def update_from_view_tab_game(self):

        ui   = self.ui
        meta = self.meta

        meta.soft_name   = ui.lineEdit_GameName.text()
        meta.soft_author = ui.lineEdit_Author  .text()

        meta.soft_description = ui.plainTextEdit_GameDescription.toPlainText()

        meta.game_vertical = ui.radioButton_VertialScrolling.isChecked()

        meta.track_kills = [
            ui.checkBox_TrackMinimumKills.isChecked(),
            ui.checkBox_TrackMaximumKills.isChecked()
        ]

        meta.game_time_bonus = ui.doubleSpinBox_ScoreTimeBonus.value()

        # TODO: Ler o arquivo de som e o volume

    #--------------------------------------------------------------------------#
    def update_from_view_tab_appearence(self):

        ui   = self.ui
        meta = self.meta

        #--- Background -------------------------------------------------------#

        # TODO: Ler a imagem de fundo
        # meta.background_image =

        meta.background_scrolls = ui.checkBox_BackgroundImageScrolls.isChecked()

        #--- Track ------------------------------------------------------------#

        if ui.checkBox_DrawTrack.isChecked():

            # TODO: Ler a imagem da pista
            # meta.track_image =
            pass

        else:
            meta.track_image = None

        #--- Scoreboard -------------------------------------------------------#

        # TODO: Ler a imagem do placar
        # meta.scoreboard.image =


        meta.scoreboard.text_position = [
            ui.spinBox_ScoreboardTextPositionX.value(),
            ui.spinBox_ScoreboardTextPositionY.value()
        ]

        meta.scoreboard.image_position = [
            ui.spinBox_ScoreboardImagePositionX.value(),
            ui.spinBox_ScoreboardImagePositionY.value()
        ]

        # TODO: Ler aspectratio
        # ui.checkBox_ScoreboardImageKeepAspectRatio.isChecked()

        # TODO: Ler cor e fonte

    #--------------------------------------------------------------------------#
    def update_from_view_tab_objects(self):

        ui   = self.ui
        con  = self.con
        meta = self.meta

        #--- Player -----------------------------------------------------------#

        # TODO: Ler imagem do jogador
        # meta.player =

        meta.player.image.size = [
            ui.spinBox_PlayerWidth. value(),
            ui.spinBox_PlayerHeight.value()
        ]

        meta.player_speed = ui.spinBox_PlayerSpeed.value()

        #--- Obstacles---------------------------------------------------------#

        # TODO: Ler obstaculos

        #--- Collectibles -----------------------------------------------------#

        # TODO: Ler colecionaveis

#------------------------------------------------------------------------------#
