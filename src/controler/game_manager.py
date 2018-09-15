
import src.common.constants as cst
from src.views.view_game import View_game

play = True
view_game = View_game()

class Game_manager:
    """
    A controler for all the game
    """

    def __init__(self):

        self.view_game = View_game()

    def refresh(self):

        self.view_game.refresh()