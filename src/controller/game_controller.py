from src.views.view_game import ViewGame
from src.humans.Dealer import Dealer
from src.humans.Player import Player
from src.CardsAPI.Deck import Deck

import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_KP1,
    K_KP2,
    K_KP3,
    K_KP4,
    K_KP5,
    K_KP6
)


class GameController:
    """
    A controller for all the game
    """
    def __init__(self, window):

        print("Enter in controller")
        self.window = window
        self.deck = Deck()
        self.humans_list = [Player("Axelle",100)]
        self.view_game = None
        # self.view_game = View_game(window, view_config)

    def gameLaunch(self):
        self.view_game = ViewGame(self.window)

    def refresh(self):
        self.view_game.refresh()

    def addHuman(self, human) -> bool:
        """
        Adding one player into the list of humans to handle at each round

        :param human: Player to add
        :type arg1: Player
        """
        if isinstance(human, Player):
            if len(self.humans_list) > 1: 
                self.humans_list = self.humans_list[:-1] + [human] + self.humans_list[:-1]
            else:
                self.humans_list = [human] + self.humans_list
            return True
        else:
            # Given human isn't a player
            return False

    def removePlayer(self, player_uuid) -> bool:
        """
        Removing one player

        :param human: Player's id to remove
        :type arg1: Player
        """
        if len(self.humans_list) > 2:
            for i in range(len(self.humans_list[:-1])):
                if self.humans_list[i].uuid == player_uuid :
                    self.humans_list = self.humans_list[:i] + self.humans_list[i+1:]
                    return True
        else:
            # No player to remove, player list is empty
            return False
        # Id not found
        return False

    def resetAllHumans(self):
        """Resetting all humans : no more player and new dealer"""
        self.humans_list = [Player("Axelle",100)]

    def playOneRound(self):
        for human in self.humans_list:
            print(human.name + " is playing.")
            # Get list of possible actions
            # Manage interfaces
            # Let human choose
            state = True
            while state:
                event = pygame.event.wait()
                if event.type == QUIT:
                    return False

                elif event.type == KEYDOWN :
                    if event.key == K_ESCAPE:
                        return False

                    elif event.key == K_1 or event.key == K_KP1 :
                        print(1)
                        for i in range(len(human.hands)):
                            card = self.deck.getCard()
                            human.addCard(card, i)

                    elif event.key == K_2 or event.key == K_KP2 :
                        print(2)
                        betAmount = 5
                        handId = 0
                        if len(human.hands) >= 2:
                            print("You have " + len(human.hands) + "hands")
                            handId = input("Hand number for bet : ")
                        human.bet(int(betAmount), int(handId))

                    elif event.key == K_3 or event.key == K_KP3 :
                        print(3)
                        state = False

                    elif event.key == K_4 or event.key == K_KP4 :
                        print(4)
                        handId = 0
                        if len(human.hands)>=2:
                            print("You have " + len(human.hands) + "hands")
                            handId = input("Hand number for bet : ")
                        human.split(handId)

                    elif event.key == K_5 or event.key == K_KP5 :
                        print(5)
                        human.double(0)

                    elif event.key == K_6 or event.key == K_KP6 :
                        return False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.view_game.quit_btn.isClicked(pos):
                        return False