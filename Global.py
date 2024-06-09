import pygame
from Player import Player

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 650
GAMEOVER = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("BasketBrawl")

font = pygame.font.SysFont(None, 36)


player1 = Player("Player 1")
player2 = Player("Player 2")


p1_card_x = 65
p2_card_x = 800
card_width = 200
card_height = 140
card_offset = 150


player1_texts = []
player2_texts = []