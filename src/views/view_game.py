from collections import defaultdict

import pygame

from src.button import Button
from src.common.func_pictures import load_image
from src.common.game_view_config import game_view_config
from src.views.image_loaders.tokensloader import TokensLoader


class ViewGame:
    def __init__(self, window):
        self._area_counts = defaultdict(int)

        # Buttons
        self.buttons = dict()

        # Init Window
        self.window = window
        self.background = None  # init in init_window
        self.init_window()

    def init_window(self):
        # Init the window with background
        background_tile = load_image("green_carpet.jpeg")
        background_tile = pygame.transform.scale(
            background_tile, (game_view_config.window.width, game_view_config.window.height)
        )
        self.background = pygame.Surface(
            (game_view_config.window.width, game_view_config.window.height)
        )
        self.background.blit(background_tile, (0, 0))

        # Display on windows
        self.window.blit(self.background, (0, 0))

        self.init_game_btns()

        # Display everything
        pygame.display.flip()

        # Init sprites
        # all_sprites = pygame.sprite.Group()
        #
        # # Update the scene
        # dirty = all_sprites.draw(self.window)
        # pygame.display.update(dirty)

    def init_game_btns(self):
        # Display game buttons area
        cfg_btns = game_view_config.game_buttons
        pygame.draw.rect(
            self.window,
            cfg_btns.color,
            (cfg_btns.x, cfg_btns.y, cfg_btns.width, cfg_btns.height),
        )

        disp = (
            ("card", "Carte", (40, 610)),
            ("bet", "Bet", (240, 610)),
            ("end_turn", "End Turn", (440, 610)),
            ("split", "Split", (640, 610)),
            ("double", "Double", (840, 610)),
            ("quit", "Quit", (1040, 610))
        )
        for i, (iid, text, pos) in enumerate(disp, 1):
            text = f"({i}) {text}"
            b = Button(
                self.window, text=text, pos=pos, size=(120, 74), bg_normal=(30, 190, 130)
            )
            b.draw()
            self.buttons[iid] = b

    def refresh(self, card_area_organizer):
        """
        :param card_area_organizer: organizer that keep place and value of all card
        :return:
        """
        print("Updating View...")
        # Init sprites
        sprite_group = pygame.sprite.Group()

        self.window.blit(self.background, (0, 0))
        self.init_game_btns()

        for el in card_area_organizer.dealer_area:
            self.window.blit(el.surface, el.position.as_tuple)
        for area in card_area_organizer.player_areas:
            for el in area:
                self.window.blit(el.surface, el.position.as_tuple)

        # TODO: Tokens should be resized and transparent
        token = TokensLoader.get_image(10)
        token = pygame.transform.scale(
            token, (game_view_config.tokens.width, game_view_config.tokens.height)
        )
        self.window.blit(token, (500, 300))

        # Update the scene
        scene = sprite_group.draw(self.window)
        pygame.display.flip()

        print("Updating View...Done!")
