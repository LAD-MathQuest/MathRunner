#------------------------------------------------------------------------------#

from pygame import mixer

import pygame.locals as loc

#------------------------------------------------------------------------------#
class SoundMixer:
    '''pygame.mixer.music wrapper'''

    muted   = False # Mute all sounds
    playing = False # If playing music

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

            SoundMixer.playing = False

    #--------------------------------------------------------------------------#
    def play_music():

        if SoundMixer.has_music  and not SoundMixer.muted:

            mixer.music.play(-1)
            SoundMixer.playing = True

    #--------------------------------------------------------------------------#
    def stop_music():

        if SoundMixer.has_music:

            mixer.music.stop()
            SoundMixer.playing = False

    #--------------------------------------------------------------------------#
    def toggle_play_music():

        SoundMixer.playing = not SoundMixer.playing

        if SoundMixer.playing:
            SoundMixer.play_music()
        else:
            SoundMixer.stop_music()

    #--------------------------------------------------------------------------#
    def load_sound(sound_path):

        return mixer.Sound(sound_path)

    #--------------------------------------------------------------------------#
    def play_sound(sound, vol=volume):

        if not SoundMixer.muted:
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

        SoundMixer.volume = min(1.0, SoundMixer.volume + SoundMixer.volume_step)

        mixer.music.set_volume(SoundMixer.volume * SoundMixer.music_volume)

    #--------------------------------------------------------------------------#
    def volume_down():

        SoundMixer.volume = max(0.0, SoundMixer.volume - SoundMixer.volume_step)

        mixer.music.set_volume(SoundMixer.volume * SoundMixer.music_volume)

    #--------------------------------------------------------------------------#
    def parse_key(key):

        if key == loc.K_m:
            SoundMixer.toggle_mute()

        elif key == loc.K_n:
            SoundMixer.toggle_play_music()

        elif key == loc.K_EQUALS:
            SoundMixer.volume_up()

        elif key == loc.K_MINUS:
            SoundMixer.volume_down()

#------------------------------------------------------------------------------#
