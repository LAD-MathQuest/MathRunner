#------------------------------------------------------------------------------#

from PySide6.QtCore       import Qt, QSize, QUrl
from PySide6.QtGui        import QPixmap, QColor
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

#------------------------------------------------------------------------------#
def draw_meta_image(label, meta):

    label.clear()

    # If there is no meta image leave the label empty
    if not meta: return

    if meta.path:
        pixmap = QPixmap(meta.path)
        size   = QSize(*(meta.size)) if meta.size else pixmap.size()
    else:
        size   = QSize(*(meta.size)) if meta.size else QSize(1920, 1080)
        pixmap = QPixmap(size)
        pixmap.fill(QColor(*(meta.color)))

    size = label.size().boundedTo(size)

    label.setPixmap(pixmap.scaled(size, aspectMode=Qt.KeepAspectRatio))

#------------------------------------------------------------------------------#
def play_sound(parent, path, vol):

    player      = QMediaPlayer(parent)
    audioOutput = QAudioOutput(parent)

    player.setAudioOutput(audioOutput)
    player.setSource     (QUrl.fromLocalFile(str(path)))

    audioOutput.setVolume(vol)

    player.play()

#------------------------------------------------------------------------------#
