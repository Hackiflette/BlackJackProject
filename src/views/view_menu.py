# import os.path

import pygame
from pygame.locals import *

from src.common.func_pictures import load_image
from src.common.constants import *


def main(window: pygame.Surface, menu_config: dict):
    """ The main function of the view of menu"""

    # Init window
    screen = window

    # Load background image
    bgd_tile = load_image("menu/bgd_menu.png")
    background = pygame.Surface((menu_config["width"], menu_config["height"]))
    background.blit(bgd_tile, (0, 0))

    # Prepare text
    title_font = pygame.font.Font(None, 44)
    title_text = title_font.render("Black Jack Project", 2, (255, 255, 255))

    core_font = pygame.font.Font(None, 30)
    begin_text = core_font.render('Start (Enter)', 2, (255, 255, 255))
    option_text = core_font.render('Options (o)', 2, (255, 255, 255))
    quit_text = core_font.render('Quit (Esc)', 2, (255, 255, 255))

    # Display on windows
    screen.blit(background, (0, 0))
    screen.blit(title_text, (80, 30))
    screen.blit(begin_text, (300, 200))
    screen.blit(option_text, (300, 300))
    screen.blit(quit_text, (300, 400))


    pygame.display.flip()

    # Init sprites
    all_sprites = pygame.sprite.RenderUpdates()
    clock = pygame.time.Clock()

    state = Game.menu
    while state == Game.menu:

        # Clear all the sprites
        all_sprites.clear(screen, bgd_tile)
        all_sprites.update()

        # Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                state = Game.quit
            elif event.type == KEYDOWN and event.key == K_RETURN:
                state = Game.play
            elif event.type == KEYDOWN and event.key == K_o:
                state = Game.option
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                state = Game.quit

        # Update the scene
        dirty = all_sprites.draw(screen)
        pygame.display.update(dirty)

        clock.tick(40)

    return state, dict()
