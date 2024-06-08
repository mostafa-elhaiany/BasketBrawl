import pygame
from Player import Player

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 650

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Card Game")

font = pygame.font.SysFont(None, 36)


player1 = Player("Player 1")
player2 = Player("Player 2")


card_width = 170
card_height = 140
card_offset = 160