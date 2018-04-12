from .Card import Card
from typing import List


class Hand(object):
    def __init__(self, cardList: List[Card]=None, isDealerHand: bool=False):
        if cardList is None:
            cardList = []
        self.cardList = cardList
        self.isSplit = False
        self.isDealerHand = isDealerHand

    @property
    def value(self) -> int:
        # without this sort, aces are always counted as 11
        sortedCardList = sorted(self.cardList, key=lambda x: x.value,
                                reverse=True)
        return sum(sortedCardList)

    @property
    def isBlackjack(self) -> bool:
        handSum = sum(self.cardList)
        if handSum == 21 and len(self.cardList) == 2 and not self.isSplit:
            return True
        else:
            return False

    @property
    def isBurnt(self) -> bool:
        # without this sort, aces are always counted as 11
        self.cardList.sort(key=lambda x: x.value, reverse=True)
        handSum = sum(self.cardList)
        if handSum > 21:
            return True
        else:
            return False

    def __gt__(self, other: 'Hand') -> bool:
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

    def __lt__(self, other: 'Hand') -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__gt__(other) and not self.__eq__(other)

    def __eq__(self, other: 'Hand') -> bool:
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

    def __ge__(self, other: 'Hand') -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__lt__(other)

    def __le__(self, other: 'Hand') -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__gt__(other)

    def __ne__(self, other: 'Hand') -> bool:
        if not isinstance(other, Hand):
            return NotImplemented
        return not self.__eq__(other)

    def __add__(self, card: Card) -> 'Hand':
        if not isinstance(card, Card):
            return NotImplemented
        self.cardList.append(card)
        return self

    def __repr__(self) -> str:
        return "Hand(cardList={}, isDealerHand={})".format(self.cardList,
                                                           self.isDealerHand)

    def __str__(self) -> str:
        if self.isDealerHand:
            owner = "Dealer"
        else:
            owner = "Player"
        return "{} Hand : {}".format(owner, self.cardList)
