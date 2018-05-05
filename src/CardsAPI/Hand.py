from .Card import Card
from typing import List, Tuple


class Hand(object):
    def __init__(self, cardList: List[Card]=None, isDealerHand: bool=False,
                 isSplit: bool = False):
        if cardList is None:
            cardList = []
        self.cardList = cardList
        self.isSplit = isSplit
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
        sortedCardList = sorted(self.cardList, key=lambda x: x.value,
                                reverse=True)
        handSum = sum(sortedCardList)
        if handSum > 21:
            return True
        else:
            return False

    def split(self) -> Tuple['Hand', 'Hand']:
        """
        Performs a split action. Returns two instances of Hand.
        The methods checks for number of cards in the original Hand (which
        should be 2) and for equality of the two cards' values
        :return: The two resulting hands in a tuple
        :raise: AssertionError
        """
        assert len(self.cardList) == 2
        assert self.cardList[0].value == self.cardList[1].value
        return (self.__class__([self.cardList[0]], isSplit=True),
                self.__class__([self.cardList[1]], isSplit=True))

    """
    The following are comparison methods for comparing Hand objects. All 
    standard comparison operators are defined and take into account the fact 
    that a Hand can be a blackjack or not and that it can belong to the 
    dealer or not
    """
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
        """
        Adds a card to the Hand, using "hand = hand + card" or "hand += card"
        :param card: a Card object to append to the Hand's cardList
        :return: The Hand itself
        """
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
