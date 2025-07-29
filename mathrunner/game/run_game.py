#------------------------------------------------------------------------------#

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1])) #incluir dinamicamente o diretório pai no sys.path
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import game_params as gp

import pygame
import pygame.freetype
import argparse
import threading

from world.meta_world import MetaWorld
from world.game_world import GameWorld
from game.engine import Engine

#------------------------------------------------------------------------------#
def main():
    '''Runs the game'''
    path_resources = Path(__file__).parents[1]/'resources'
    parser = argparse.ArgumentParser(description='MathRunner')
    parser.add_argument('world', help='Game World file name', nargs='?')
    args = parser.parse_args()

    default_game_path = None

    pygame.init()
    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    pygame.mouse.set_pos((0, 0))  

    if args.world:
        path = Path(args.world).resolve()

        if path.is_file():
            default_game_path = path
    meta = MetaWorld.load(args.world) if args.world else MetaWorld()

   
    #--- Carregar imagem de fundo ---
    if meta.background_image:
        print(Path(meta.background_image.path))
        img_path = Path(meta.background_image.path)
        background = pygame.image.load(img_path).convert()

        background = pygame.Surface((1920, 1080))
        background.fill((0, 0, 0))

    
    #--- Carregar som ambiente ---
    if meta.game_ambience:
        pygame.mixer.init()
        meta.game_ambience = str(path_resources/meta.game_ambience)
        sound_path = Path(meta.game_ambience)
        pygame.mixer.music.load(str(sound_path))
        volume = getattr(meta, 'game_ambience_volume', 1.0)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)

    # --- Reproduzir som ambiente ---
    if meta.game_ambience:
        if meta.game_ambience and not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)
        

    world = GameWorld(meta)
    engine = Engine(world)

    engine.run()
    sys.exit()

#------------------------------------------------------------------------------#
if __name__ == '__main__': main()

#------------------------------------------------------------------------------#
