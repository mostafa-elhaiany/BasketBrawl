import pygame
import sys

import ActionManager
from Artist import Artist
import Global


artist = Artist(Global)

artist.draw_screen()


# Game Loop
while not Global.GAMEOVER:
    ActionManager.handle_actions(Global)

    if(Global.player1.health<=0 and Global.player2.health>0):
        Global.GAMEOVER = True
        artist.draw_mid_text("Player 2 wins!", color=(0,255,0))
    elif(Global.player2.health<=0 and Global.player1.health>0):
        Global.GAMEOVER = True
        artist.draw_mid_text("Player 1 wins!", color=(0,255,0))
    elif(Global.player2.health<=0 and Global.player1.health<=0):
        artist.draw_mid_text("Sudden Death", color=(255,0,0))
        Global.player1.health = 1
        Global.player2.health = 1

    artist.draw_screen()


    pygame.display.flip()

print("Game Over")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    artist.draw_screen()
    pygame.display.flip()
