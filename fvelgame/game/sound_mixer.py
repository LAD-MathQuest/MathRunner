#------------------------------------------------------------------------------#

from pygame import mixer

#------------------------------------------------------------------------------#
class SoundMixer:
    '''pygame.mixer.music wrapper'''

    muted  = False
    volume = 1.0
    volume_step = 1/20

    has_music = None

    #--------------------------------------------------------------------------#
    def load_music(sound, vol=volume):

        SoundMixer.has_music = bool(sound)

        if SoundMixer.has_music:
            mixer.music.load(sound)
            mixer.music.set_volume(vol)

    #--------------------------------------------------------------------------#
    def play_music():
        
        if SoundMixer.has_music:
            mixer.music.play(-1)

    #--------------------------------------------------------------------------#
    def stop_music():

        if SoundMixer.has_music:
            mixer.music.stop()

    #--------------------------------------------------------------------------#
    def play_sound(sound, vol=volume):

        if not SoundMixer.muted:
            sound = mixer.Sound(sound)
            sound.set_volume(vol)
            sound.play()

    #--------------------------------------------------------------------------#
    def toggle_mute():

        SoundMixer.muted = not SoundMixer.muted

        if SoundMixer.has_music:
            if SoundMixer.muted:
                mixer.music.stop()
            else:
                mixer.music.play(-1)

    #--------------------------------------------------------------------------#
    def volume_up():
        SoundMixer.volume = min( 1.0, SoundMixer.volume + SoundMixer.volume_step )
        mixer.music.set_volume(SoundMixer.volume)

    #--------------------------------------------------------------------------#
    def volume_down():
        SoundMixer.volume = max( 0.0, SoundMixer.volume - SoundMixer.volume_step )
        mixer.music.set_volume(SoundMixer.volume)

#------------------------------------------------------------------------------#
