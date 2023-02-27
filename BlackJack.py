import enum
import dataclasses
import random


@dataclasses.dataclass
class Card:
    name: str
    suit: str
    value: int
    is_special: bool = False

    @property
    def special_value(self):
        return 1


class Suits(enum.Enum):
    DIAMOND = "Diamond"
    HEART = "Heart"
    CROSS = "Cross"
    SPADES = "Spades"


class Deck:
    _VALUES = [
        ("2", 2, False),
        ("3", 3, False),
        ("4", 4, False),
        ("5", 5, False),
        ("6", 6, False),
        ("7", 7, False),
        ("8", 8, False),
        ("9", 9, False),
        ("10", 10, False),
        ("J", 10, False),
        ("Q", 10, False),
        ("K", 10, False),
        ("A", 11, True),
    ]

    def __init__(self):
        self.cards = []

        for name, value, is_special in self._VALUES:
            for suit in Suits:
                card = Card(name=name, value=value, suit=suit, is_special=is_special)
                self.cards.append(card)

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0

    def add(self, card: Card):
        self.cards.append(card)
        value = card.value

        if card.is_special:
            if self.score + card.value > 21:
                value = card.special_value

        if self.score + value > 21:
            raise ValueError("You exceeded max score 21. You lose")

        self.score += value


class BlackJack:
    def __init__(self):
        self.deck = self.reset()

    def step(self):
        return self.deck.cards.pop(0)

    def reset(self):
        self.deck = Deck()
        return self.deck


class ConsoleBlackjack:
    def __init__(self, players: int = 1):
        self.blackjack = BlackJack()
        self.players = [Player("Player " + str(i + 1)) for i in range(players)]

    def play(self):
        while True:
            for player in self.players:
                print(player.name + "'s turn.")
                while True:
                    try:
                        hit = input("Do you want to hit? (y/n) ").strip().lower()
                        if hit == 'y':
                            card = self.blackjack.step()
                            player.add(card)
                            print(f"You got {card.name} of {card.suit.value}")
                            print(f"Your current score is {player.score}")
                            if player.score == 21:
                                print("Blackjack! You won!")
                                return
                        elif hit == 'n':
                            print(f"{player.name} stands.")
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'")

                    except ValueError as e:
                        print(e)
                        print(f"{player.name} loses!")
                        return

            max_score = 0
            winners = []
            for player in self.players:
                if max_score < player.score <= 21:
                    max_score = player.score
                    winners = [player]
                elif player.score == max_score:
                    winners.append(player)

                if len(winners) == 1:
                    print(f"Player {winners[0]} wins with a score of {max_score}!")
                else:
                    print("It's a tie!")
                    for winner in winners:
                        print(f"Player {winner} ties with a score of {max_score}.")


if __name__ == '__main__':
    game = ConsoleBlackjack(players=2)
    game.play()

