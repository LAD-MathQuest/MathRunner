#------------------------------------------------------------------------------#

from io import BytesIO

import tempfile
import pygame

#--------------------------------------------------------------------------------#
class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_sound = None
        self.temp_files = []

    def load_sound(self, sound_source):
        self.stop()

        if isinstance(sound_source, BytesIO):
            temp_file = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
            temp_file.write(sound_source.getvalue())
            temp_file.close()
            self.temp_files.append(temp_file.name)
            pygame.mixer.music.load(temp_file.name)
        else:
            sound_path = str(sound_source) if hasattr(sound_source, 'fspath') else sound_source
            pygame.mixer.music.load(sound_path)

    def play(self, loop=False, volume=1.0):
        if pygame.mixer.music.get_busy():
            self.stop()

        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1 if loop else 0)

    def stop(self):
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(max(0.0, min(1.0, volume)))

    def cleanup(self):
        self.stop()
        for temp_file in self.temp_files:
            os.unlink(temp_file)
        self.temp_files = []

#------------------------------------------------------------------------------#
