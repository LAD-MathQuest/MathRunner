#------------------------------------------------------------------------------#

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1])) #incluir dinamicamente o diretório pai no sys.path
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import game_params as gp

import pygame
import pygame.freetype

from world.meta_world import MetaWorld
from world.game_world import GameWorld
from game.engine import Engine



#------------------------------------------------------------------------------#
def main():
    '''Runs the game'''

    import argparse
    import pygame
    import threading

    parser = argparse.ArgumentParser(description='MathRunner')
    parser.add_argument('world', help='Game World file name', nargs='?')
    args = parser.parse_args()

    pygame.init()
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    pygame.mouse.set_pos((0, 0))  

    RESOURCES = Path(__file__).resolve().parent.parent / "resources"  

    meta = MetaWorld.load(args.world) if args.world else MetaWorld()

    if meta.background_image:
        meta.background_image.path = RESOURCES / meta.background_image.path

    # --- Carregar imagem de fundo ---
    if meta.background_image:
        img_path = RESOURCES / meta.background_image.path
        background = pygame.image.load(str(img_path)).convert()
    else:
        background = pygame.Surface((1920, 1080))
        background.fill((0, 0, 0))

# --- Reproduzir som ambiente ---
    if meta.game_ambience:
        pygame.mixer.init()
        pygame.mixer.music.load(str(meta.game_ambience))
        volume = getattr(meta, 'game_ambience_volume', 1.0)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1) 


    world = GameWorld(meta)
    engine = Engine(world)

    engine.run()
    sys.exit()

#------------------------------------------------------------------------------#
if __name__ == '__main__': main()

#------------------------------------------------------------------------------#
