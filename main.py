# -*- coding: utf-8 -*-

# ============================================================================
# =
# = Imports
# =
# ============================================================================

import os
import json

import pygame
from pygame.locals import *

import src.common.constants as cst
from src.views import view_menu, view_game, view_option
from src.controller.game_controller import Game_controller

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
        self.initController()

        # mainloop
        self.mainloop()

    def loadConfig(self):
        """
        Load the configuration file
        """

        file_config = os.path.join(cst.DIR_CONFIG, "ui.cfg.json")
        with open(file_config, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def initPygame(self):
        """
        Initialize the main screen
        """

        pygame.init()
        pygame.display.set_caption("Black Jack by Hackiflette")
        self.window = pygame.display.set_mode(
            (self.config["window"]["width"],
             self.config["window"]["height"]))

    def initController(self):
        """
        Initialize the game_manager
        """

        self.ctrl = Game_controller(self.window, self.config["window"])

    def mainloop(self):
        """
        The mainloop the launch the game
        """

        state, param = view_menu.main(self.window, self.config["window"], self.config["menu_buttons"])

        while state != cst.Game.quit:

            if state == cst.Game.menu:
                state, param = view_menu.main(self.window, self.config["window"], self.config["menu_buttons"])
            elif state == cst.Game.play:
                self.ctrl.game_launch()
                state = self.gameLoop()
                # state, param = view_game.main(self.window, self.config["window"])
            elif state == cst.Game.option:
                state, param = view_option.main(self.window, self.config["window"])
            else:
                state = 0

        pygame.quit()

    def gameLoop(self):
        """
        The loop of the game which communicate with controller
        """
        state = cst.Game.play
        print("GameLoop")
        while state == cst.Game.play:

            for event in pygame.event.get():
                if event.type == QUIT:
                    state = cst.Game.menu
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    state = cst.Game.menu

        print("gameLoop")
        return state


if __name__ == '__main__':
    print("Exists?")
    for folder in [cst.DIR_SRC, cst.DIR_DATA, cst.DIR_CONFIG, cst.DIR_PICTURES]:
        print(folder, os.path.exists(folder))

    Main()
