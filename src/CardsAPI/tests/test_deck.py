from src.CardsAPI import Deck,Card


def testInitDeck():

    deck = Deck.Deck()
    assert deck.top_card_index == 0
    assert len(deck.cards) == 312
    assert deck.red_card_index >= ((3 / 4) * 312) - 30 and deck.red_card_index <= ((3 / 4) * 312) + 30

    # Assert not shuffle
    deck = Deck.Deck(False)
    assert deck.top_card_index == 0
    assert len(deck.cards) == 312
    assert deck.red_card_index >= ((3 / 4) * 312) - 30 and deck.red_card_index <= ((3 / 4) * 312) + 30


def testDealDeck():

    deck = Deck.Deck()
    card = deck.getCard()
    assert type(card) == Card.Card
    assert deck.top_card_index == 1


def testRedCardDeck():

    deck = Deck.Deck()
    last_card = deck.cards[-1]
    deck.getCard()
    assert last_card == deck.cards[-1]

    for i in range(int(((3 / 4) * 312) + 35)):
        deck.getCard()

    assert deck.cards[-1] != last_card


def testShuffleDeck():

    deck = Deck.Deck()
    first_card = deck.cards[0]
    deck.shuffle()
    assert first_card != deck.cards[0]


def testInitShuffleDeck():

    deck1 = Deck.Deck(False)
    deck2 = Deck.Deck(False)
    assert deck1.cards[0] == deck2.cards[0]


def testToMuchDeal():

    deck = Deck.Deck()
    for i in range(500):
        card = deck.getCard()

    assert len(deck.cards) == 312
