# -*- coding: utf-8 -*-

# ============================================================================
# =
# = Imports
# =
# ============================================================================

import os

import pygame
from pygame.locals import *

from src.common.constants import *
from src.views import view_menu, view_game

# ============================================================================
# =
# = Application
# =
# ============================================================================


class Main:
    """
    The main application
    """

    def __init__(self):

        # Configuration
        self.loadConfig()

        # Init pygame
        self.initPygame()

        # mainloop
        self.mainloop()

    def loadConfig(self):
        """
        Load the configuration file
        """

        file_config = os.path.join(DIR_CONFIG, "ui.cfg.json")
        with open(file_config, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def initPygame(self):
        """
        Intialize the main screen
        """

        pygame.init()
        pygame.display.set_caption("Black Jack by Hackiflette")
        self.window = pygame.display.set_mode((self.config["window"]["width"],
                                               self.config["window"]["height"]))

    def mainloop(self):
        """
        The mainloop the launch the game
        """

        state, param = view_menu.main(self.window, self.config["window"])

        while state != Game.quit:

            if state == Game.menu:
                state, param = view_menu.main(self.window, self.config["window"])
            elif state == Game.play:
                state, param = view_game.main(self.window, self.config["window"])
            else:
                state = 0

        pygame.quit()


if __name__ == '__main__':
    print("Exists?")
    for folder in [DIR_SRC, DIR_DATA, DIR_CONFIG, DIR_PICTURES]:
        print(folder, os.path.exists(folder))

    Main()
