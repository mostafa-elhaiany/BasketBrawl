class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.deck = []
        self.discard_pile = []
        self.points = 0

    def draw_card(self):
        if self.deck:
            self.hand.append(self.deck.pop())

    def play_card(self, card_index, opponent):
        card = self.hand.pop(card_index)
        card.play(self, opponent)
        self.discard_pile.append(card)

    def add_points(self, points):
        self.points += points
