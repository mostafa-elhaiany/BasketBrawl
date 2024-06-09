import pygame
import sys, time
import ActionManager
from Artist import Artist
import Global
from Poller import Poller

artist = Artist(Global)

artist.draw_screen()


poller = Poller("wby5QwdWjyA")
vote_interval = 3  # Check every 5 seconds
last_check = 0

was_polling = False

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
    if(not was_polling and Global.POLLING):
        was_polling = True
        artist.enable_poll()
    elif(was_polling and not Global.POLLING):
        artist.poll_active = False
        poller.apply_results(Global.player1, Global.player2)
        was_polling = False
    if(artist.poll_active):
        current_time = time.time()
        if current_time - last_check > vote_interval:
            poller.get_results()
            last_check = current_time
        artist.update_poll(poller)


    pygame.display.flip()

print("Game Over")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    artist.draw_screen()
    pygame.display.flip()
