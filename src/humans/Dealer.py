from src.CardsAPI.Hand import Hand
from src.CardsAPI.Deck import Deck
from src.common.constants import Decision


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def chooseAction(self):
        """
        Function to choose action, Hit or Stand, depending on the dealer's
        hand value. Usually 2 rules can be chosen regarding the dealer's
        decision making:
        - dealer stands on all 17s (and hits below)
        - dealer hits on soft 17 and below (and stands on hard 17 and above)
        :return: decision
        """
        if self.hand.value < 17:  # Dealer stands on all 17s
            return Decision.hit
        else:
            return Decision.stand


