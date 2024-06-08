import pygame
import sys
import random

from Player import Player
from Card import Card

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Card Game")

font = pygame.font.SysFont(None, 36)

# Example card actions
def attack_action(player, opponent):
    opponent.add_points(-10)

def heal_action(player, opponent):
    player.add_points(10)

# Create example cards
card1 = Card("Attack Card", cost=1, action=attack_action)
card2 = Card("Heal Card", cost=1, action=heal_action)

# Player class

# Initialize players
player1 = Player("Player 1")
player2 = Player("Player 2")

# Add cards to player decks
player1.deck.extend([card1, card2] * 10)
player2.deck.extend([card1, card2] * 10)

# Shuffle decks
random.shuffle(player1.deck)
random.shuffle(player2.deck)

# Draw initial hands
for _ in range(5):
    player1.draw_card()
    player2.draw_card()

# Function to draw cards as rectangles
def draw_card(card, x, y):
    card_rect = pygame.Rect(x, y, 120, 180)
    pygame.draw.rect(screen, (255, 255, 255), card_rect)
    draw_text(card.name, font, (0, 0, 0), screen, x + 10, y + 10)
    if card.played:
        draw_text("Played", font, (255, 0, 0), screen, x + 10, y + 150)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    draw_text(f'{player1.name} Points: {player1.points}', font, (255, 255, 255), screen, 20, 20)
    draw_text(f'{player2.name} Points: {player2.points}', font, (255, 255, 255), screen, 20, 60)

    # Draw player 1 hand
    x_offset = 20
    for card in player1.hand:
        draw_card(card, x_offset, 100)
        x_offset += 140

    # Draw player 2 hand
    x_offset = 20
    for card in player2.hand:
        draw_card(card, x_offset, 300)
        x_offset += 140

    pygame.display.flip()
