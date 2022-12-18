#------------------------------------------------------------------------------#

from pygame import mixer

#------------------------------------------------------------------------------#
class SoundMixer:
    '''pygame.mixer.music wrapper'''

    volume = 1

    #--------------------------------------------------------------------------#
    def __init__( self, sound ):

        self.has_sound = bool(sound)

        if self.has_sound:
            mixer.music.load(sound)
            mixer.music.set_volume(SoundMixer.volume)

    #--------------------------------------------------------------------------#
    def play(self):

        if self.has_sound:
            mixer.music.play(-1)

    #--------------------------------------------------------------------------#
    def stop(self):

        if self.has_sound:
            mixer.music.stop()

    #--------------------------------------------------------------------------#
    def toggle_mute(self):

        SoundMixer.volume = 1 - SoundMixer.volume
        mixer.music.set_volume(SoundMixer.volume)

    #--------------------------------------------------------------------------#
    def play_sound(sound):

        if SoundMixer.volume:
            mixer.Sound(sound).play()

#------------------------------------------------------------------------------#
