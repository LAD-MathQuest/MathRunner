#------------------------------------------------------------------------------#

from PySide6.QtGui import QFont

from meta   import MetaWorld
from .tools import draw_meta_image

#--------------------------------------------------------------------------#
def update_ui_from_meta(meta: MetaWorld, ui, con) -> None:
    update_view_tab_game      (meta, ui, con)
    update_view_tab_appearance(meta, ui, con)
    update_view_tab_objects   (meta, ui, con)
    update_view_tab_velocity  (meta, ui, con)
    update_view_tab_boundary  (meta, ui, con)

#--------------------------------------------------------------------------#
def update_view_tab_game(meta: MetaWorld, ui, con) -> None:

    ui.lineEdit_GameName.setText(meta.soft_name)
    ui.lineEdit_Author  .setText(meta.soft_author)

    draw_meta_image(ui.label_GameIcon, meta.soft_icon)

    ui.plainTextEdit_GameDescription.setPlainText(meta.soft_description)

    if meta.game_vertical:
        ui.radioButton_VerticalScrolling.setChecked(True)
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
def update_view_tab_appearance(meta: MetaWorld, ui, con) -> None:

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
def update_view_tab_objects(meta: MetaWorld, ui, con) -> None:

    #--- Player -----------------------------------------------------------#

    player = meta.player

    draw_meta_image(ui.label_PlayerImage, player.image)

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
def update_view_tab_velocity(meta: MetaWorld, ui, con) -> None:

    ui.lineEdit_FunctionVelocity.setText(meta.velocity.get_function_orig())

#--------------------------------------------------------------------------#
def update_view_tab_boundary(meta: MetaWorld, ui, con) -> None:

    boundary = meta.boundary

    ui.lineEdit_FunctionTrackMinimum.setText(boundary.get_function_min_orig())
    ui.lineEdit_FunctionTrackMaximum.setText(boundary.get_function_max_orig())

#------------------------------------------------------------------------------#
