import pygame
from pygame.locals import *

import src.common.constants as c
from src.common.func_pictures import load_image


def main(window, menu_config):
    """ The main function of the view of the game"""

    # Init window
    screen = window

    # Load background image
    bgd_tile = load_image("blackjack_table.png")
    bgd_tile = pygame.transform.scale(bgd_tile, (menu_config["width"], menu_config["height"]))
    background = pygame.Surface((menu_config["width"], menu_config["height"]))
    background.blit(bgd_tile, (0, 0))

    # Display on windows
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Init sprites
    all_sprites = pygame.sprite.RenderUpdates()
    clock = pygame.time.Clock()

    state = c.Game.play
    while state == c.Game.play:

        # Clear all the sprites
        all_sprites.clear(screen, bgd_tile)
        all_sprites.update()

        # Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                state = c.Game.menu
            elif (event.type == KEYDOWN and event.key == K_ESCAPE):
                state = c.Game.menu

        # Update the scene
        dirty = all_sprites.draw(screen)
        pygame.display.update(dirty)

        clock.tick(40)

    return state, dict()
