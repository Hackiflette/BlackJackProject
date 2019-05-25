import itertools
import random

from .Card import Card, card_to_value_dict, colors


class Deck:
    def __init__(self, SHUFFLE: bool = True):
        self.cards = list(
            itertools.product(card_to_value_dict.keys(), colors)) * 6

        if SHUFFLE:
            self.shuffle()

        # index of the card on the top of the deck
        self.top_card_index = 0

        # index of the red card, when the dealer finds this card, he shuffles
        # the deck. Usually placed around 3/4 of the deck
        self.red_card_index = random.randint(
            (3/4) * len(self.cards) - 30, (3 / 4) * len(self.cards) + 30)

    def shuffle(self):
        # shuffle deck
        random.shuffle(self.cards)
        # reset counter
        self.top_card_index = 0

    def deal(self) -> Card:
        self.top_card_index += 1
        if self.top_card_index == self.red_card_index:
            self.shuffle()
            # FIXME: we should do it only at the end of a turn

        return Card(*self.cards[self.top_card_index])
