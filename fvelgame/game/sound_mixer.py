#------------------------------------------------------------------------------#

from pygame import mixer

#------------------------------------------------------------------------------#
class SoundMixer:
    '''pygame.mixer.music wrapper'''

    muted = False  # Mute all sounds
    music = True   # Play music if it was provided

    volume      = 1.0
    volume_step = 1/20

    has_music    = None
    music_volume = 1.0

    #--------------------------------------------------------------------------#
    def load_music(sound, vol=volume):

        SoundMixer.has_music    = bool(sound)
        SoundMixer.music_volume = vol

        if SoundMixer.has_music:
            mixer.music.load(sound)
            mixer.music.set_volume(SoundMixer.volume * SoundMixer.music_volume)

    #--------------------------------------------------------------------------#
    def play_music():
        if SoundMixer.has_music and SoundMixer.music and not SoundMixer.muted:
            mixer.music.play(-1)

    #--------------------------------------------------------------------------#
    def stop_music():
        if SoundMixer.has_music:
            mixer.music.stop()

    #--------------------------------------------------------------------------#
    def toggle_play_music():

        SoundMixer.music = not SoundMixer.music

        if SoundMixer.music:
            SoundMixer.play_music()
        else:
            SoundMixer.stop_music()

    #--------------------------------------------------------------------------#
    def play_sound(sound, vol=volume):

        if not SoundMixer.muted:
            sound = mixer.Sound(sound)
            sound.set_volume(SoundMixer.volume * vol)
            sound.play()

    #--------------------------------------------------------------------------#
    def toggle_mute():

        SoundMixer.muted = not SoundMixer.muted

        if SoundMixer.muted:
            SoundMixer.stop_music()
        else:
            SoundMixer.play_music()

    #--------------------------------------------------------------------------#
    def volume_up():
        SoundMixer.volume = min( 1.0, SoundMixer.volume + SoundMixer.volume_step )
        mixer.music.set_volume(SoundMixer.volume * SoundMixer.music_volume)

    #--------------------------------------------------------------------------#
    def volume_down():
        SoundMixer.volume = max( 0.0, SoundMixer.volume - SoundMixer.volume_step )
        mixer.music.set_volume(SoundMixer.volume * SoundMixer.music_volume)

#------------------------------------------------------------------------------#
