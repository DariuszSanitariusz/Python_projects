import unittest
import Player
import Card


def get_input(text):
    return input(text)


player = Player.Player('test')
card = Card.Card('Clubs', 'Three')
output = []
Player.print = lambda m: output.append(m)


class TestPlayer(unittest.TestCase):

    def test_add_chips(self):
        test_input = 10

        def mock_input(s):
            return test_input

        Player.input = mock_input
        player.add_chips('contestant')
        result = player.funds
        self.assertEqual(result, 10)

    def test_withdrawal_for_bet(self):
        amount = 1
        player.withdrawal_for_bet(amount)
        result = player.funds
        self.assertEqual(result, 9)

    def test_withdrawal_for_bet_overdraft(self):
        amount = 10
        player.withdrawal_for_bet(amount)
        result = output[2]
        self.assertEqual(result, "Insufficient funds")

    def test_add_card(self):
        player.add_card(card)
        result = len(player.hand)
        self.assertEqual(result, 1)

    def test_get_hand_value(self):
        player.get_hand_value()
        value = card.value
        result = player.hand_value
        self.assertEqual(result, value)


if __name__ == '__main__':
    unittest.main()
