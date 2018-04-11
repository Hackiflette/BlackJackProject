from .Card import Card

class Hand(object):
    def __init__(self, cardList = None, isDealerHand = False):
        if cardList is None:
            cardList = []
        self.cardList = cardList
        self.isSplit = False
        self.isDealerHand = isDealerHand



    @property
    def value(self):
        # without this sort, aces are always counted as 11
        self.cardList.sort(key=lambda x: x.value, reverse=True)
        return sum(self.cardList)

    @property
    def isBlackjack(self):
        handSum = sum(self.cardList)
        if handSum == 21 and len(self.cardList) == 2 and not self.isSplit:
            return True
        else:
            return False

    @property
    def isBurnt(self):
        # without this sort, aces are always counted as 11
        self.cardList.sort(key=lambda x: x.value, reverse=True)
        handSum = sum(self.cardList)
        if handSum > 21:
            return True
        else:
            return False

    """
    @property
    def handValue(self):
        # without this sort, aces are always counted as 11
        self.cardList.sort(key=lambda x: x.value, reverse=True)
        handSum = sum(self.cardList)
        if handSum == 21 and len(self.cardList) == 2 and not self.isSplit:
            return HandValue(value=21, blackjack=True)
        elif handSum > 21:
            return HandValue(value=handSum, burnt=True)
        else:
            return HandValue(value=handSum)
    """

    def __gt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        if self.isBlackjack and not other.isBlackjack:
            return True
        elif other.isBurnt and not self.isBurnt:
            return True
        elif self.isBurnt and other.isBurnt and self.isDealerHand:
            return True
        elif self.value > other.value and not self.isBurnt:
            return True
        else:
            return False

    def __lt__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__gt__(other) and not self.__eq__(other)

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        if self.isBlackjack and other.isBlackjack:
            return True
        elif self.isBurnt and other.isBurnt and not self.isDealerHand \
                and not other.isDealerHand:
            return True
        elif self.value == other.value and not \
                self.isBlackjack and not other.isBlackjack:
            return True
        else:
            return False

    def __ge__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__lt__(other)

    def __le__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__gt__(other)

    def __ne__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__eq__(other)

    def __add__(self, card):
        if not isinstance(card, Card):
            return NotImplemented
        self.cardList.append(card)
        return self

    def __repr__(self):
        return "Hand(cardList={}, isDealerHand={})".format(self.cardList,
                                                           self.isDealerHand)
    def __str__(self):
        if self.isDealerHand:
            owner = "Dealer"
        else:
            owner = "Player"
        return "{} Hand : {}".format(owner, self.cardList)

    def __iadd__(self, card):
        if not isinstance(card, Card):
            return NotImplemented
        self.cardList.append(card)
        return self
"""

class HandValue:
    def __init__(self,
                 value: int,
                 burnt: bool = False,
                 blackjack: bool = False):
        self.value = value
        self.burnt = burnt
        self.blackjack = blackjack
"""