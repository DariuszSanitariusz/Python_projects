from Card import Card
from Deck import Deck
from Player import Player

suits_symbol = {'X':'', 'BUST!':'', 'Hearts':'\u2665', 'Diamonds':'\u2666', 'Spades':'\u2660', 'Clubs':'\u2663'}


class Gameplay:

    def __init__(self):

        self.number_of_players = 0
        self.list_of_players = []
        self.compare_list = []
        self.shuffle_deck = True
        self.dealer = Player('DEALER')
        self.player_turn = True
        self.hidden_card = 0
        self.game_on = True

    def get_number_of_players(self):
        typing = True
        while typing:
            try:
                number = int(input("How many players? "))
            except ValueError:
                print("Please enter a number")
            else:
                typing = False
        self.number_of_players = number

    def adding_players(self):
        for i in range(self.number_of_players):
            human = input(f"Please enter your name, player {i+1}: ")
            player = Player(human)
            player.add_chips(human)
            self.list_of_players.append(player)

    def preparing_deck(self):
        deck = Deck()
        if len(deck) < 26 or self.shuffle_deck:
            deck.shuffle()
            self.shuffle_deck = False
        return deck

    def everyone_bets(self):
        for contestant in self.list_of_players:
            contestant.taking_bet()

    def starting_hands(self, deck):
        for i in range(2):
            self.dealer.add_card(deck.deal_one())
            for player in self.list_of_players:
                player.add_card(deck.deal_one())

    def dealer_hidden_card(self):
        if self.player_turn:
            self.hidden_card = self.dealer.remove_card()
            self.dealer.add_card(Card('X', 'X'))
        else:
            self.dealer.remove_card()
            self.dealer.add_card(self.hidden_card)

    def display_table(self):
        print('\n'*50)
        print(f"{self.dealer.name}: ")
        for card in self.dealer.hand:
            print(card.rank + suits_symbol[card.suit] + ' ', end='')
        print('\n'*3)
        for contestant in self.list_of_players:
            print(f"{contestant.name}: ")
            for card in contestant.hand:
                print(card.rank + suits_symbol[card.suit] + ' ', end='')
            print('\n')

    def player_hit_or_stop(self, deck, contestant):
        choice = 0
        while choice not in ['hit', 'stop']:
            choice = input(f"{contestant.name}, do you want to HIT or STOP? ").lower()
            if choice not in ['hit', 'stop']:
                print("Sorry, I don't understand, please type HIT or STOP")
        if choice == 'hit':
            contestant.add_card(deck.deal_one())
        else:
            self.compare_list.append(contestant)
            self.player_turn = False

    def dealer_turn(self, deck):
        while self.dealer.hand_value <= 17:
            self.dealer.add_card(deck.deal_one())
            self.dealer.get_hand_value()
        if self.dealer.hand_value > 21:
            self.dealer.hand_value = 0
            print("Players have won!")
        self.player_turn = True

    def compare_players_score(self):
        for contestant in self.compare_list:
            if self.dealer.hand_value > contestant.hand_value:
                print(f"{contestant.name}, no luck")
                print('\n')
            elif self.dealer.hand_value == contestant.hand_value:
                print(f"{contestant.name}, draw")
                contestant.funds += contestant.player_bet
                print('\n')
            else:
                print(f"{contestant.name} has won!")
                contestant.funds += contestant.player_bet*2
                print('\n')
                
    def endgame(self):
        self.compare_list = []
        for contestant in self.list_of_players:
            contestant.player_bet = 0
            contestant.empty_hands()
            print(f"{contestant.name}'s balance: {contestant.funds}")
            if contestant.funds == 0:
                choice = 0
                while choice not in ['y', 'n']:
                    choice = input(f"{contestant.name}, you went bankrupt. Do you want to buy more chips? Y or N").lower()
                    if choice not in ['y', 'n']:
                        print("I don't understand")
                if choice == 'y':
                    amount = input("Please type amount: ")
                    contestant.add_chips(amount)
                else:
                    self.list_of_players.pop(contestant)
                    self.number_of_players -= 1

    def replay(self):
        replay = 0
        while replay not in ['y', 'n']:
            replay = input("Do you want to play again? Y or N").lower()
            if replay not in ['y', 'n']:
                print("I don't understand")
        if replay == 'y':
            self.game_on = True
        else:
            self.game_on = False

    def leaving_table(self):
        choice = 0
        while choice not in ['y', 'n']:
            choice = input("Does anyone want to leave the table? Y or N").lower()
            if choice not in ['y', 'n']:
                print("I don't understand")
        if choice == 'y':
            while True:
                try:
                    number = int(input("How many players? "))
                except ValueError:
                    print("Please repeat")
                if number < self.number_of_players:
                    break
                else:
                    print("There aren't that many players")

            for i in range(number):
                enter_name = True
                while enter_name:
                    player = input("Please type your name?")
                    for contestant in self.list_of_players:
                        if contestant.name == player:
                            self.list_of_players.remove(player)
                            self.number_of_players -= 1
                            enter_name = False
                        else:
                            print("Please repeat")
                            break
        else:
            print("Excellent!")
