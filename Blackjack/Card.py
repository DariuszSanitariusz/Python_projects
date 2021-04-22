class Card:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    suits_symbol = {'X': '', 'BUST!': '', 'Hearts': '\u2665', 'Diamonds': '\u2666', 'Spades': '\u2660',
                    'Clubs': '\u2663'}
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'X': 0, 'BUST!': 0, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit
