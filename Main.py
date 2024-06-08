import pygame
import sys

import ActionManager
from Artist import Artist
import Global


artist = Artist(Global)

# Draw initial hands
# for _ in range(5):
#     Global.player1.draw_card()
#     Global.player2.draw_card()


artist.draw_screen()

while True:
    ActionManager.handle_actions(Global)


    artist.draw_screen()


    pygame.display.flip()
