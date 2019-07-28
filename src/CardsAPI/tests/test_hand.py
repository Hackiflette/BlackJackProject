from src.CardsAPI import card, Hand

# To launch test in console :
# ... $ python -m pytest tests/
from src.CardsAPI.exceptions import CardsAPIError


def test_init_hand():

    hand = Hand.Hand()
    assert len(hand.card_list) == 0

    hand = Hand.Hand([card.Card(2)])
    assert hand.value == 2


def test_add_card():

    hand = Hand.Hand()
    card = card.Card(2)
    hand = hand + card
    card = card.Card(5)
    hand = hand + card
    assert len(hand.card_list) == 2
    assert hand.value == 7


def test_iadd_card():

    hand = Hand.Hand([card.Card(5)])
    hand_list = [hand]
    hand += card.Card(2)
    assert len(hand_list[0].card_list) == 2
    assert hand_list[0].value == 7


def test_comparison_hand():

    hand_1 = Hand.Hand([card.Card(5),
                        card.Card(7)])
    hand_2 = Hand.Hand([card.Card(3)])
    assert hand_1 > hand_2


def test_split_hand():

    hand = Hand.Hand([card.Card(3, 'heart'),
                      card.Card(3, 'spades')])
    [hand_1, hand_2] = hand.split()
    assert hand_1.value == 3 and hand_2.value == 3
    assert hand_1 == hand_2

    hand2 = Hand.Hand([card.Card(3), card.Card(4)])
    try:
        hand2.split()
    except CardsAPIError:
        assert True
    else:
        assert False

    # testing too many cards in hand
    hand += card.Card(3)
    try:
        hand.split()
    except CardsAPIError:
        assert True
    else:
        assert False
