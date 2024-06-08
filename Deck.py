from Card import Card
import random

def attack_action(player, opponent):
    death_blow = opponent.attacked(10)

def heal_action(player, opponent):
    player.heal(10)

def draw_action(player, opponent):
    player.draw_card()



class Deck:
    def get_draw_card():
        return Card("images/draw.png", "Draw Card", cost=1, action=draw_action)

    def __init__(self):
        self.cards = [
            Card("images/attack.png", "Attack Card", cost=1, action=attack_action),
            Card("images/heal.png", "Heal Card", cost=1, action=heal_action),
        ]
        random.shuffle(self.cards)
    
    def pop(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)