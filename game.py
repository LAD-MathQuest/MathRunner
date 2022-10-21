#!/usr/bin/python
#------------------------------------------------------------------------------#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

import pygame

from world  import World
from engine import Engine

#------------------------------------------------------------------------------#

pygame.init()

pygame.mouse.set_visible( False )

info = pygame.display.Info()

world = World((info.current_w, info.current_h))

engine = Engine( world )

while True:

    engine.start()

    engine.new_enemy()

    engine.game_loop() 

#------------------------------------------------------------------------------#
