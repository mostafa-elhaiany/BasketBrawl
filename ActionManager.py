import sys
import pygame

def handle_actions(Global):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                handle_click(Global.player1, Global.player2, event.pos, Global)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Global.player1.points +=1
            if event.key == pygame.K_p:
                Global.player2.points +=1


def handle_click(player, opponent, pos, Global):
    # print(pos)
    y_offset = 20
    for i, _ in enumerate(player.hand):
        card_rect = pygame.Rect(100, y_offset, Global.card_width, Global.card_height)
        if card_rect.collidepoint(pos):
            player.play_card(i, opponent)
            return 
        y_offset += Global.card_offset
    y_offset = 20
    for i, _ in enumerate(opponent.hand):
        card_rect = pygame.Rect(850, y_offset, Global.card_width, Global.card_height)
        if card_rect.collidepoint(pos):
            opponent.play_card(i, player)
            return
        y_offset += Global.card_offset
