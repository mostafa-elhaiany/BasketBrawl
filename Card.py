import pygame 

class Card:
    def __init__(self,image_path, name, cost, action):
        self.name = name
        self.cost = cost
        self.action = action
        if(image_path is not None):
            self.image = pygame.image.load(image_path)
        else:
            self.image = None
        self.played = False  # New attribute to track if the card has been played

    def play(self, player, opponent):
        if not self.played:  # Ensure the card hasn't been played already
            self.action(player, opponent)
            self.played = True  # Mark the card as played
