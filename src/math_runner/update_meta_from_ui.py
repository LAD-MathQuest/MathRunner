#------------------------------------------------------------------------------#

from meta import MetaWorld, MetaObject, MetaImage
from PySide6.QtGui import QColor

from .tools import label_to_meta_image
from .tools import qcolor_to_tuple
from .tools import font_file_to_bytes  

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
        ui.checkBox_BoundaryMinimumKills.isChecked(),
        ui.checkBox_BoundaryMaximumKills.isChecked()
    ]

    meta.game_time_bonus = ui.doubleSpinBox_ScoreTimeBonus.value()

    # TODO: read sound and volume

#------------------------------------------------------------------------------#
def update_from_view_tab_appearance(meta: MetaWorld, ui, con) -> None:

    # Background

    label_to_meta_image(ui.label_BackgroundImage, meta.background_image)

    meta.background_scrolls = ui.checkBox_BackgroundImageScrolls.isChecked()

    # Track

    if ui.checkBox_DrawBoundary.isChecked():
        label_to_meta_image(ui.label_BoundaryImage, meta.boundary_image)
    else:
        meta.boundary_image = None

    # TODO: read track boundary lines
    # meta.min_color =
    # meta.max_color =
    # meta.min_width =
    # meta.max_width =

    # Scoreboard

    meta.scoreboard.image = MetaImage()
    label_to_meta_image(ui.label_ScoreboardImage, meta.scoreboard.image)

    meta.scoreboard.image.size = [
        ui.spinBox_ScoreboardImageWidth .value(),
        ui.spinBox_ScoreboardImageHeight.value()
    ]

    meta.scoreboard.text_position = [
        ui.spinBox_ScoreboardTextPositionX.value(),
        ui.spinBox_ScoreboardTextPositionY.value()
    ]

    meta.scoreboard.image_position = [
        ui.spinBox_ScoreboardImagePositionX.value(),
        ui.spinBox_ScoreboardImagePositionY.value()
    ]

    meta.scoreboard.text_font_size = int(getattr(con, "scoreboard_font_size", meta.scoreboard.text_font_size or 14))
    meta.scoreboard.text_spacing   = float(getattr(con, "scoreboard_text_spacing", 1.2))
    meta.scoreboard.text_fgcolor   = qcolor_to_tuple(getattr(con, "scoreboard_fg", QColor(255, 255, 255)))
    meta.scoreboard.text_bgcolor   = qcolor_to_tuple(getattr(con, "scoreboard_bg", QColor(0, 0, 0, 150)))


    # Salva os bytes da fonte personalizada, se houver
    font_path = getattr(con, "scoreboard_font_path", None)
    if font_path:
        meta.scoreboard.text_font = font_file_to_bytes(font_path)
    else:
        meta.scoreboard.text_font = None

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

    meta.obstacles.clear()

    for obj in con.obstacles:
        meta_obj = MetaObject()
        obj.object_to_meta(meta_obj)
        meta.obstacles.append(meta_obj)

    # Collectibles

    meta.collectibles_frequency = ui.doubleSpinBox_CollectiblesFrequency.value()

    meta.collectibles.clear()

    for obj in con.collectibles:
        meta_obj = MetaObject()
        obj.object_to_meta(meta_obj)
        meta.collectibles.append(meta_obj)

#------------------------------------------------------------------------------#
