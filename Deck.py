from Card import Card
import random

def attack_action(player, opponent):
    if(opponent.mirror):
        opponent.mirror = False
        death_blow = player.attacked(1)
    else:
        death_blow = opponent.attacked(1)

def heal_action(player, opponent):
    player.heal(2)

def draw_action(player, opponent):
    player.draw_card()

def shield_action(player, opponent):
    player.animate_health_function((0,0,255))
    player.shielded = True

def poison_action(player, opponent):
    death_blow = opponent.poisoned(2)

def double_attack_action(player, opponent):
    if(opponent.mirror):
        opponent.mirror = False
        player.attacked(1)
    else:
        opponent.attacked(1)        
    death_blow = opponent.attacked(1)

def energy_boost_action(player, opponent):
    player.add_points(3)

def reflect_action(player, opponent):
    player.mirror = True

def sacrifice_action(player, opponent):
    player.attacked(3)
    player.add_points(5)

def steal_action(player, opponent):
    player.add_points(2)
    opponent.remove_points(2)

class Deck:
    def get_draw_card():
        return Card("images/draw.png", "Draw Card", cost=1, action=draw_action)

    def __init__(self):
        self.cards = [
            Card("images/attack.png", "Attack", cost=1, action=attack_action),
            Card("images/heal.png", "Heal", cost=2, action=heal_action),
            Card("images/shield.png","Shield", cost=3, action=shield_action),
            Card("images/poison.png", "Poison", cost=4, action=poison_action),
            Card("images/double attack.png", "Double Attack", cost=3, action=double_attack_action),
            Card("images/energy boost.png", "Energy Boost", cost=2, action=energy_boost_action),
            Card("images/reflect.png","Reflect Action", cost=4, action=reflect_action),
            Card("images/sacrifice.png","Sacrifice", cost=1, action=sacrifice_action),
            Card("images/steal.png","Steal", cost=4, action=steal_action),
        ]
        random.shuffle(self.cards)
    
    def pop(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)