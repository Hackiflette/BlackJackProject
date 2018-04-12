import itertools
import random

from .Card import Card, cardToValueDict, colors


class Deck:
    def __init__(self, SHUFFLE: bool=True):
        self.cards = list(
            itertools.product(cardToValueDict.keys(), colors)) * 6

        if SHUFFLE:
            self.shuffle()

        # index of the card on the top of the deck
        self.topCardIndex = 0

        # index of the red card, when the dealer finds this card, he shuffles
        # the deck. Usually placed around 3/4 of the deck
        self.redCardIndex = random.randint(
            (3/4) * len(self.cards) - 30, (3 / 4) * len(self.cards) + 30)
        # TODO: find a cleaner way than -30 +30, like gaussian distribution

    def shuffle(self):
        # shuffle deck
        random.shuffle(self.cards)
        # reset counter
        self.topCardIndex = 0

    def deal(self) -> Card:
        self.topCardIndex += 1
        if self.topCardIndex == self.redCardIndex:
            self.shuffle()
            # TODO: we should do it only at the end of a turn

        return Card(*self.cards[self.topCardIndex])
