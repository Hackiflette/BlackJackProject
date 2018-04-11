import random

from .Card import Card, cardToValueDict, colors


class Deck:
    def __init__(self, SHUFFLE = True):
        self.cardList = [Card(name, color) for color in colors
                    for name in cardToValueDict.keys()
                    for _ in range(6)] # 6 x (52-card decks)
        if SHUFFLE:
            self.shuffle()

        # instantiates generator
        self.generator = self._generator()

    def _generator(self):
        yield from self.cardList

    def shuffle(self):
        random.shuffle(self.cardList)

    def deal(self):
        return self.generator.__next__()
