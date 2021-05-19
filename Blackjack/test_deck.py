import unittest
import Deck


class TestDeck(unittest.TestCase):
    def test_dealing(self):
        deck = Deck.Deck()
        deck.deal_one()
        result = len(deck)
        self.assertEqual(result, 51)


if __name__ == '__main__':
    unittest.main()
