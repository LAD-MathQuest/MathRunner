#------------------------------------------------------------------------------#
import io

from PySide6.QtCore       import Qt, QSize, QUrl, QByteArray, QBuffer, QIODevice
from PySide6.QtGui        import QPixmap, QColor
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from meta import MetaImage

#------------------------------------------------------------------------------#
def meta_image_to_label(label, meta: MetaImage) -> None:

    label.clear()

    if not meta:
        label.setProperty('original_pixmap', None)
        return

    if meta.data:
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(meta.data.getvalue()))
        size = QSize(*(meta.size)) if meta.size else pixmap.size()

    else:
        size = QSize(*(meta.size)) if meta.size else QSize(1920, 1080)
        pixmap = QPixmap(size)
        pixmap.fill(QColor(*(meta.color)))

    size = label.size().boundedTo(size)

    label.setPixmap(pixmap.scaled(size, aspectMode=Qt.KeepAspectRatio))
    label.setProperty('original_pixmap', pixmap)

#------------------------------------------------------------------------------#
def label_to_meta_image(label, meta: MetaImage) -> None:

    pixmap = label.property('original_pixmap')

    if not pixmap:
        meta = None
        return

    buffer = QBuffer()
    buffer.open(QIODevice.ReadWrite)

    image = pixmap.toImage()
    image.save(buffer, 'PNG')

    meta.data = io.BytesIO(buffer.data().data())

    buffer.close()

    size = pixmap.size()
    meta.size = (size.width(), size.height())

#------------------------------------------------------------------------------#
def play_sound(parent, path, vol):

    player      = QMediaPlayer(parent)
    audioOutput = QAudioOutput(parent)

    player.setAudioOutput(audioOutput)
    player.setSource     (QUrl.fromLocalFile(str(path)))

    audioOutput.setVolume(vol)

    player.play()

#------------------------------------------------------------------------------#
