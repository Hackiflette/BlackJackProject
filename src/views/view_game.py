import pygame
from pygame.locals import *

import src.common.constants as cst
from src.common.func_pictures import load_image, convert_card_to_picture


class View_game:

    def __init__(self, window, menu_config):

        self.window = window
        self.menu_config = menu_config
        self.init_window()

    def init_window(self):
        # Init the window with background
        bgd_tile = load_image("blackjack_table.png")
        bgd_tile = pygame.transform.scale(bgd_tile, (self.menu_config["width"],
                                                     self.menu_config["height"]))
        self.background = pygame.Surface((self.menu_config["width"],
                                          self.menu_config["height"]))
        self.background.blit(bgd_tile, (0, 0))

        # Test the display of cards on the window
        from src.CardsAPI.Card import Card
        self.add_card(Card('King'), (350, 400))
        self.add_card(Card('Queen'), (365, 415))

        # Display on windows
        self.window.blit(self.background, (0, 0))
        pygame.display.flip()

        # Init sprites
        all_sprites = pygame.sprite.RenderUpdates()

        # Update the scene
        dirty = all_sprites.draw(self.window)
        pygame.display.update(dirty)

    def add_card(self, card, pos):
        """
        Add a card on the table view at a certain pos
        """
        card_tile = load_image(convert_card_to_picture(card))
        card_tile = pygame.transform.scale(card_tile, (cst.CONFIG_PICTURES['cards']['size']['width'],
                                                       cst.CONFIG_PICTURES['cards']['size']['height']))
        self.background.blit(card_tile, pos)

    def refresh(self):

        pass

def main(window, menu_config):
    """ The main function of the view of the game"""

    # Init window
    screen = window

    # Load self.background image
    bgd_tile = load_image("blackjack_table.png")
    bgd_tile = pygame.transform.scale(bgd_tile, (menu_config["width"], menu_config["height"]))
    self.background = pygame.Surface((menu_config["width"], menu_config["height"]))
    self.background.blit(bgd_tile, (0, 0))

    # Display on windows
    screen.blit(self.background, (0, 0))
    pygame.display.flip()

    # Init sprites
    all_sprites = pygame.sprite.RenderUpdates()
    clock = pygame.time.Clock()

    state = cst.Game.play
    while state == cst.Game.play:

        # Clear all the sprites
        all_sprites.clear(screen, bgd_tile)
        all_sprites.update()

        # Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                state = cst.Game.menu
            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = cst.Game.menu

        # Update the scene
        dirty = all_sprites.draw(screen)
        pygame.display.update(dirty)

        clock.tick(40)

    return state, dict()
