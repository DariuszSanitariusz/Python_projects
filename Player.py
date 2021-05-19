from Card import Card

class Player:

    def __init__(self,name,funds=0):
        self.name = name
        self.funds = funds
        self.hand = []
        self.hand_value = 0
        self.ace_in_hand = False
        self.player_bet = 0

    def add_chips(self, contestant):
        while True:
            try:
                money = int(input(f"{contestant}, how many chips would you like to buy? "))
            except ValueError:
                print("You didn't type a number")
                continue
            else:
                self.funds += money
                break
        print("Chips has been added.")

    def withdrawal_for_bet(self, amount):
        if self.funds >= amount:
            self.funds -= amount
            self.player_bet = amount
            print("Placing bet")
        else:
            print("Insufficient funds")   

    def taking_bet(self):
        print(f"{self.name}, place your bet")
        while self.player_bet == 0:
            while True:
                try:
                    amount = int(input("Type amount: "))
                except ValueError:
                    print("You didn't type a number")
                else:
                    self.withdrawal_for_bet(amount)
                    break

    def add_card(self, new_card):
        self.hand.append(new_card)

    def get_hand_value(self):
        result = 0
        for card in self.hand:
            result += card.value
            if card.rank == 'Ace':
                self.ace_in_hand = True
        if 21 <= result <= 31 and self.ace_in_hand:
            result -= 10
        elif result > 21:
            self.add_card(Card('BUST!', 'BUST!'))
        self.hand_value = result

    def remove_card(self):
        return self.hand.pop(-1)

    def empty_hands(self):
        for i in range(len(self.hand)):
            self.remove_card()
        self.hand_value = 0

    def __str__(self):
        return f"{self.name} funds: {self.funds}"
