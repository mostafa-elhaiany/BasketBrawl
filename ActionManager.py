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
        # keyboard controls
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Global.player1.add_points(1)
            if event.key == pygame.K_p:
                Global.player2.add_points(1)

            handle_keyboard_control(event.key, Global.player1, Global.player2)

            if event.key == pygame.K_v: # activate sudden death
                Global.player1.health=0
                Global.player2.health=0

def handle_keyboard_control(key, player1, player2):
    if key == pygame.K_a:
        play_card_on_click(player1, player2, 0)
    if key == pygame.K_s:
        play_card_on_click(player1, player2, 1)
    if key == pygame.K_d:
        play_card_on_click(player1, player2, 2)
    if key == pygame.K_f:
        play_card_on_click(player1, player2, 3)

    if key == pygame.K_l:
        play_card_on_click(player2, player1, 0)
    if key == pygame.K_k:
        play_card_on_click(player2, player1, 1)
    if key == pygame.K_j:
        play_card_on_click(player2, player1, 2)
    if key == pygame.K_h:
        play_card_on_click(player2, player1, 3)


def play_card_on_click(player, opponent, idx):
    player.play_card(idx, opponent)

def handle_click(player, opponent, pos, Global):
    y_offset = 20
    for i, _ in enumerate(player.hand):
        card_rect = pygame.Rect(Global.p1_card_x, y_offset, Global.card_width, Global.card_height)
        if card_rect.collidepoint(pos):
            player.play_card(i, opponent)
            return 
        y_offset += Global.card_offset
    y_offset = 20
    for i, _ in enumerate(opponent.hand):
        card_rect = pygame.Rect(Global.p2_card_x, y_offset, Global.card_width, Global.card_height)
        if card_rect.collidepoint(pos):
            opponent.play_card(i, player)
            return
        y_offset += Global.card_offset
