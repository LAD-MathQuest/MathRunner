#------------------------------------------------------------------------------#
import io

from PySide6.QtCore       import Qt, QSize, QUrl, QByteArray, QBuffer, QIODevice
from PySide6.QtGui        import QPixmap, QColor
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from meta import MetaImage
from pathlib import Path
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtCore import QByteArray

#------------------------------------------------------------------------------#
def path_image_to_label(label, path) -> None:

    label.clear()

    pixmap = QPixmap()
    pixmap.load(path)

    size = label.size().boundedTo(pixmap.size())

    label.setPixmap(pixmap.scaled(size, aspectMode=Qt.KeepAspectRatio))
    label.setProperty('original_pixmap', pixmap)

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

def qcolor_to_tuple(qcolor):
    #Converte QColor para tupla (r,g,b,a) ou None
    if qcolor is None:
        return None
    return (qcolor.red(), qcolor.green(), qcolor.blue(), qcolor.alpha())

#------------------------------------------------------------------------------#
def font_file_to_bytes(font_path):
    #Lê arquivo de fonte e retorna bytes ou None
    if not font_path:
        return None
    with open(font_path, 'rb') as f:
        return f.read()
#------------------------------------------------------------------------------#
def bytes_to_qfont(font_bytes, font_size):
    if not font_bytes:
        return QFont("Arial", font_size)
    font_id = QFontDatabase.addApplicationFontFromData(QByteArray(font_bytes))
    if font_id != -1:
        family = QFontDatabase.applicationFontFamilies(font_id)[0]
        return QFont(family, font_size)
    return QFont("Arial", font_size)