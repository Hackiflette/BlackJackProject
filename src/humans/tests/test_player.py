from src.humans.player import  Player
from src.humans.dealer import Dealer
from src.cards import card
from src.common.constants import Decision


def testInitPlayer():
    player = Player("TestPlayer1", 1000)
    assert player.name == "TestPlayer1"
    assert player.wallet == 1000


def testPlayerBet():
    player = Player("TestPlayer1", 1000)
    player.addCard(card.Card(1), 0)
    player.bet(500, 0)
    assert player.wallet == 500

    player.bet(1000, 0)
    assert player.wallet == 0


def testSplit():
    ace_heart_card = card.Card("ace", "heart")
    ace_spade_card = card.Card("ace", "spades")

    assert ace_heart_card.value == 1
    assert ace_heart_card.color.lower() == "hearts"

    assert ace_spade_card.value == 1
    assert ace_spade_card.color.lower() == "spades"

    player = Player("TestPlayer1", 1000)
    player.addCard(ace_heart_card, 0)
    player.addCard(ace_spade_card, 0)

    player.bet(250, 0)

    split_possible = player.checkSplitIsPossible(0)
    assert split_possible

    player.split(0)
    assert len(player.hands) == 2
    assert player.wallet == 500

def testDealerDecision():
    dealer = Dealer()

    ace_heart_card = card.Card("ace", "heart")
    ten_heart_card = card.Card(10, "heart")

    dealer.addCard(ace_heart_card)
    dealer.addCard(ten_heart_card)

    # dealer hand is at 21 should stand, ace should be 11
    assert dealer.chooseAction() == Decision.stand

    dealer.clearHand()

    six_heart_card = card.Card(6, "heart")

    dealer.addCard(ace_heart_card)
    dealer.addCard(six_heart_card)

    # dealer hand is at 17 in mode 0 should stand, ace should be 1
    assert dealer.chooseAction() == Decision.stand
    # dealer hand is at 17 in mode 1 should hit, ace should be 1
    assert dealer.chooseAction(1) == Decision.hit

    dealer.clearHand()

    four_heart_card = card.Card(4, "heart")
    three_heart_card = card.Card(3, "heart")

    dealer.addCard(four_heart_card)
    dealer.addCard(three_heart_card)

    # dealer hand is at 7 should hit
    assert dealer.chooseAction() == Decision.hit
