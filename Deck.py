from Card import Card
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Deck:

    def __init__(self):

        self.game_deck = []
        self.size = 0

        for rank in ranks:
            for suit in suits:
                for_deck = Card(suit, rank)
                self.game_deck.append(for_deck)
                self.size += 1

    def shuffle(self):
        random.shuffle(self.game_deck)

    def deal_one(self):
        self.size -= 1
        return self.game_deck.pop()

    def __len__(self):
        return self.size
