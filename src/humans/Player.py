from src.CardsAPI import Hand
import uuid
from typing import List, Tuple
from src.common.constants import PlayerHand

class Player:

    def __init__(self, name, wallet, uid=None):
        self.uuid: uuid.UUID = self.create_uuid(uid)
        # hands are list of Hand, money bet and if the hand is lock
        self.hands: List[Tuple[Hand, int, False]] = list()
        self.wallet: int = wallet

    @staticmethod
    def create_uuid(uid):
        if uid is None:
            return uuid.uuid4()
        else:
            return uid

    def bet(self, amount, index_of_the_hand) -> bool:
        """
        Check wallet value and substract the amount or take all the wallet
        :return: boolean value :
                 - True : amount betted can be bet
                 - False : amount is too high bet only what left in the wallet
        """

        if amount <= wallet :
            # subtract amount from wallet and add it the the pot
            self.wallet -= amount
            # increasing the amount of money bet for this hand
            self.hands[index_of_the_hand][PlayerHand.HandBet] += amount
            return True
        else:
            # amount is higher than wallet put wallet at zero and put it into
            # the money bet on hand
            self.hands[index_of_the_hand][PlayerHand.HandBet] += self.wallet
            self.wallet = 0

        return False

    def checkSplitIsPossible(self, index_of_hand_to_split) -> bool:
        """
        Check if a split is possible according to the money bet on the hand and
        the value of the wallet.
        :return: boolean
           - True : split can be done
           - False: split can't be done
        """
        if self.checkDoubleBetIsPossible(index_of_hand_to_split) \
           and self.hands[index_of_hand_to_split][PlayerHand.Hand].checkSplitIsPossible()
           return True

        return False

    def checkDoubleBetIsPossible(self, index_of_the_bet_to_double) -> bool:
        """
        Check if player can bet again what he has already bet on his hands
        :return: True if double is possible False if not
        """
        if self.hands[index_of_the_bet_to_double][PlayerHand.HandBet] <= self.wallet:
            return True

        return False

    def double(self, index_of_the_hand_to_double):
        """
        Double the money spend by the player
        """
        if self.checkDoubleBetIsPossible(index_of_the_hand_to_double):
            # ---- Double the bet ----
            # 3 - lock the hand
            self.hands[index_of_the_hand_to_double][PlayerHand.IsLock] = True

            # 1 - removing the bet in the wallet
            self.wallet -= self.hands[index_of_the_hand_to_double][PlayerHand.HandBet]

            # 2 - adding the new bet value
            self.hands[index_of_the_hand_to_double][PlayerHand.HandBet] += self.hands[index_of_the_hand_to_double][PlayerHand.HandBet]
        else :
            print("<class Player>[double] double bet on Player", self.uuid, "is impossible")


    def split(self, index_of_hand_to_split):
        """
        Check if the hand can be split if so it split it
        """

        if self.checkSplitIsPossible(index_of_hand_to_split)
            # if check is ok cards are good and wallet have enough money
            splitted_hand = self.hands[index_of_hand_to_split][PlayerHand.Hand].split()
            bet_of_the_hand = self.hands[index_of_hand_to_split][PlayerHand.HandBet]

            # remove bet of the second hand just created
            self.wallet -= bet_of_the_hand

            if len(splitted_hand) > 2 :
                # ---- Creating the new hands ---
                # 1 - reinitialize hands of the player
                self.hands = []

                # 2 - adding first hand with the associated bet
                self.hands.append(Tuple[splitted_hand[0], bet_of_the_hand])

                # 3 - adding second hand with it associated bet
                self.hands.append(Tuple[splitted_hand[1], bet_of_the_hand])
            else:
                print("<class Player>[split] split return less than 2 cards for hand of Player ", self.uuid)



