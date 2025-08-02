#------------------------------------------------------------------------------#

# from meta import MetaWorld, save_meta, load_meta

#--------------------------------------------------------------------------#
def update_meta_from_ui(meta, ui, con):
    pass
    # update_from_view_tab_game      (meta, ui, con)
    # update_from_view_tab_appearance(meta, ui, con)
    # update_from_view_tab_objects   (meta, ui, con)

#--------------------------------------------------------------------------#
def update_from_view_tab_game(meta, ui, con):

    meta.soft_name   = ui.lineEdit_GameName.text()
    meta.soft_author = ui.lineEdit_Author  .text()

    meta.soft_description = ui.plainTextEdit_GameDescription.toPlainText()

    meta.game_vertical = ui.radioButton_VerticalScrolling.isChecked()

    meta.track_kills = [
        ui.checkBox_TrackMinimumKills.isChecked(),
        ui.checkBox_TrackMaximumKills.isChecked()
    ]

    meta.game_time_bonus = ui.doubleSpinBox_ScoreTimeBonus.value()

    # TODO: Ler o arquivo de som e o volume

#--------------------------------------------------------------------------#
def update_from_view_tab_appearance(meta, ui, con):

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
def update_from_view_tab_objects(meta, ui, con):

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
