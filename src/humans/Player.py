from src.CardsAPI import Hand
import uuid
from typing import List, Tuple

class Player:

    def __init__(self, name, wallet, uid=None):
        self.uuid: uuid.UUID = self.create_uuid(uid)
        self.hands: List[Tuple[Hand, int]] = list()
        self.wallet: int = wallet

    @staticmethod
    def create_uuid(uid):
        if uid is None:
            return uuid.uuid4()
        else:
            return uid

    def bet(self, amount):
        assert amount <= self.wallet
