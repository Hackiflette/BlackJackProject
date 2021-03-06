from src.cards.card import Card

# To launch test in console :
# ... $ python -m pytest tests/


def test_create_num_card():

    card = Card(1)
    assert card.value == 1
    assert card.color == 'HEARTS'

    card = Card('TWO')
    assert card.value == 2

    card = Card('Three', 'diamond')
    assert card.value == 3
    assert card.color == 'DIAMONDS'


def test_create_face_card():

    card = Card(12)
    assert card.name == "QUEEN"
    assert card.value == 10

    card = Card("King")
    assert card.name == "KING"
    assert card.color == 'HEARTS'


def test_add_cards():

    card_1 = Card(5, "Hearts")
    card_2 = Card(7, "DIAMONDS")
    assert card_1 + card_2 == 12

    card_3 = Card("TWO", "spades")
    card_4 = Card(13)
    assert card_3 + card_4 == 12


def test_add_ace():

    card_1 = Card("KING", "hearts")
    card_2 = Card(9)
    card_3 = Card("ACE", "heaRts")
    assert card_1 + card_2 + card_3 == 20
    # assert card_3 + card_2 + card_1 == 20
