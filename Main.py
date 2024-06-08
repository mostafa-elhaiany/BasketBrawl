import pygame
import sys

import ActionManager, Artist
import Global



# Draw initial hands
for _ in range(4):
    Global.player1.draw_card()
    Global.player2.draw_card()


while True:
    ActionManager.handle_actions(Global)


    Artist.draw_screen(Global)


    pygame.display.flip()
