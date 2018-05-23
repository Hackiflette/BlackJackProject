from src.CardsAPI import Card

# To launch test in console :
# ... $ python -m pytest tests/

def test_create_object():

    card_1 = Card.Card(1)
    value = card_1.value
    assert value == 1

def test_create_object_str():

    card = Card.Card('TWO')
    assert card.value == 2

def test_create_object_value_entire():

    card = Card.Card('Three', 'diamond')
    assert card.value == 3
    assert card.color == 'DIAMONDS'