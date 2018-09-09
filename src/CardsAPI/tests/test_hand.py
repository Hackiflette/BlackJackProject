from src.CardsAPI import Card, Hand

# To launch test in console :
# ... $ python -m pytest tests/


def test_init_hand():

    hand = Hand.Hand()
    assert len(hand.card_list) == 0

    hand = Hand.Hand([Card.Card(2)])
    assert hand.value == 2


def test_add_card():

    hand = Hand.Hand()
    card = Card.Card(2)
    hand += card
    card = Card.Card(5)
    hand += card
    assert len(hand.card_list) == 2
    assert hand.value == 7


def test_comparison_hand():

    hand_1 = Hand.Hand([Card.Card(5),
                        Card.Card(7)])
    hand_2 = Hand.Hand([Card.Card(3)])
    assert hand_1 > hand_2


def test_split_hand():

    hand = Hand.Hand([Card.Card(3, 'heart'),
                      Card.Card(3, 'spades')])
    [hand_1, hand_2] = hand.split()
    assert hand_1.value == 3 and hand_2.value == 3
    assert hand_1 == hand_2

    hand2 = Hand.Hand([Card.Card(3), Card.Card(4)])
    try:
        h1, h2 = hand2.split()
        split = True
    except AssertionError:
        split = False
    assert not split

    hand += Card.Card(3)
    try:
        [h1, h2] = hand.split()
        split = True
    except AssertionError:
        split = False
    assert not split
