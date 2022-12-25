#------------------------------------------------------------------------------#

from PySide6.QtCore       import QUrl
from PySide6.QtGui        import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

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
