import unittest
from BlackJack import Card, Suits, ConsoleBlackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.game = ConsoleBlackjack(players=2)
        self.players = self.game.players

    def test_deck_size(self):
        self.assertEqual(len(self.game.blackjack.deck), 52)

    def test_deck_shuffle(self):
        original_deck = self.game.blackjack.deck.cards.copy()
        self.game.blackjack.reset()
        shuffled_deck = self.game.blackjack.deck.cards
        self.assertNotEqual(original_deck, shuffled_deck)

    def test_player_add_card(self):
        player = self.players[0]
        card = Card(name="K", value=10, suit=Suits.HEART, is_special=False)
        player.add(card)
        self.assertIn(card, player.cards)
        self.assertEqual(player.score, 10)

    def test_player_add_special_card(self):
        player = self.players[0]
        card = Card(name="A", value=11, suit=Suits.HEART, is_special=True)
        player.add(card)
        self.assertIn(card, player.cards)
        self.assertEqual(player.score, 11)

    def test_play(self):
        self.game.play()
        self.assertGreaterEqual(self.players[0].score, 0)
        self.assertGreaterEqual(self.players[1].score, 0)


if __name__ == '__main__':
    unittest.main()
