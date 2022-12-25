#------------------------------------------------------------------------------#

import sys, os, tempfile

from PySide6.QtCore       import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from pathlib import Path
from world.meta_world import MetaWorld

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
    def __init__(self,window):

        self.meta = MetaWorld()
        self.win  = window

    #--------------------------------------------------------------------------#
    def new(self):
        self.meta = MetaWorld()

    #--------------------------------------------------------------------------#
    def open(self, file_name):
        self.meta = MetaWorld.load(file_name)

    #--------------------------------------------------------------------------#
    def save(self, file_name):
        pass

    #--------------------------------------------------------------------------#
    def run(self):
        temp_file = tempfile.NamedTemporaryFile( prefix='meta_', suffix='.game' )
        name = str(temp_file.name)

        self.meta.save(name)

        run_game = str(Path(__file__).parents[1]/'game'/'run_game.py')

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

#------------------------------------------------------------------------------#
