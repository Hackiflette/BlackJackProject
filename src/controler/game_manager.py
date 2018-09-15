
import src.common.constants as cst
from src.views.view_game import View_game


class Game_manager:
    """
    A controler for all the game
    """

    def __init__(self, window, menu_config):

        print("Enter in controler")
        self.window = window
        self.menu_config = menu_config
        # self.view_game = View_game(window, menu_config)

    def game_launch(self):
        self.view_game = View_game(self.window, self.menu_config)

    def refresh(self):

        self.view_game.refresh()