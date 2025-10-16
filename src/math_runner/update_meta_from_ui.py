#------------------------------------------------------------------------------#

from meta import MetaWorld

from .tools import label_to_meta_image

#------------------------------------------------------------------------------#
def update_meta_from_ui(meta: MetaWorld, ui, con) -> None:
    update_from_view_tab_game      (meta, ui, con)
    update_from_view_tab_appearance(meta, ui, con)
    update_from_view_tab_objects   (meta, ui, con)

#------------------------------------------------------------------------------#
def update_from_view_tab_game(meta: MetaWorld, ui, con) -> None:

    meta.soft_name   = ui.lineEdit_GameName.text()
    meta.soft_author = ui.lineEdit_Author  .text()

    meta.soft_description = ui.plainTextEdit_GameDescription.toPlainText()

    label_to_meta_image(ui.label_GameIcon, meta.soft_icon)

    meta.game_vertical = ui.radioButton_VerticalScrolling.isChecked()

    meta.track_kills = [
        ui.checkBox_TrackMinimumKills.isChecked(),
        ui.checkBox_TrackMaximumKills.isChecked()
    ]

    meta.game_time_bonus = ui.doubleSpinBox_ScoreTimeBonus.value()

    # TODO: read sound and volume

#------------------------------------------------------------------------------#
def update_from_view_tab_appearance(meta: MetaWorld, ui, con) -> None:

    # Background

    label_to_meta_image(ui.label_BackgroundImage, meta.background_image)

    meta.background_scrolls = ui.checkBox_BackgroundImageScrolls.isChecked()

    # Track

    if ui.checkBox_DrawTrack.isChecked():
        label_to_meta_image(ui.label_TrackImage, meta.track_image)
    else:
        meta.track_image = None

    # TODO: read track boundary lines
    # meta.min_color =
    # meta.max_color =
    # meta.min_width =
    # meta.max_width =

    # Scoreboard

    # TODO: read scoreboard information

    meta.scoreboard.text_position = [
        ui.spinBox_ScoreboardTextPositionX.value(),
        ui.spinBox_ScoreboardTextPositionY.value()
    ]

    meta.scoreboard.image_position = [
        ui.spinBox_ScoreboardImagePositionX.value(),
        ui.spinBox_ScoreboardImagePositionY.value()
    ]

#------------------------------------------------------------------------------#
def update_from_view_tab_objects(meta: MetaWorld, ui, con) -> None:

    # Player

    label_to_meta_image(ui.label_PlayerImage, meta.player.image)

    meta.player.image.size = [
        ui.spinBox_PlayerWidth. value(),
        ui.spinBox_PlayerHeight.value()
    ]

    meta.player_speed = ui.spinBox_PlayerSpeed.value()

    # Obstacles

    meta.obstacles_frequency = ui.doubleSpinBox_ObstaclesFrequency.value()

    # TODO: get number od obstacles and read obstacles

    # Collectibles

    meta.collectibles_frequency = ui.doubleSpinBox_CollectiblesFrequency.value()

    # TODO: get number od collectibles and read collectibles

#------------------------------------------------------------------------------#
