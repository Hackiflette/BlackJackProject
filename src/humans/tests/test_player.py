from src.humans import Player
from src.CardsAPI import Card

def testInitPlayer():
    player = Player.Player("TestPlayer1", 1000)
    assert player.name == "TestPlayer1"
    assert player.wallet == 1000


def testPlayerBet():
    player = Player.Player("TestPlayer1", 1000)
    player.addCard(Card.Card(1),0)
    player.bet(500, 0)
    assert player.wallet == 500

    player.bet(1000, 0)
    assert player.wallet == 0

def testSplit():
    ace_heart_card = Card.Card("ace", "heart")
    ace_spade_card = Card.Card("ace", "spades")

    assert ace_heart_card.value == 1
    assert ace_heart_card.color.lower() == "hearts"

    assert ace_spade_card.value == 1
    assert ace_spade_card.color.lower() == "spades"

    player = Player.Player("TestPlayer1", 1000)
    player.addCard(ace_heart_card, 0)
    player.addCard(ace_spade_card, 0)

    player.bet(250, 0)

    split_possible = player.checkSplitIsPossible(0)
    assert split_possible == True

    player.split(0)
    assert len(player.hands) == 2
    assert player.wallet == 500
