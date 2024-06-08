from Deck import Deck
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.deck = Deck()
        self.points = 0
        self.health = 100
        self.shield = 0

    def add_draws(self):
        self.hand = [Deck.get_draw_card() for _ in range(4)]

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop())
            if(len(self.deck)==0):
                self.deck = Deck()


    def play_card(self, card_index, opponent):
        cost = self.hand[card_index].cost
        if(self.points>=cost):
            self.points -= cost
            card = self.hand.pop(card_index)            
            card.play(self, opponent)

    def add_points(self, points):
        self.points += points

    def attacked(self, hit_points):
        self.health -=hit_points
        if(self.health<=0):
            print("Game over")
            return True
        return False
    
    def heal(self, heal_points):
        self.health +=heal_points
        if(self.health>100):
            self.health = 100
        return False