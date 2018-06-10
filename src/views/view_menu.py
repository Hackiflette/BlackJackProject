import os.path

import pygame
from pygame.locals import QUIT

DIR_SRC = os.path.dirname(__file__)
DIR_PICTURES = os.path.join(os.path.dirname(DIR_SRC), "pictures")
DIR_MENU_PICTURES = os.path.join(DIR_PICTURES, "menu")


def loadImage(file):
    """	Loads an image, prepares it for play """

    file = os.path.join(DIR_MENU_PICTURES, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        error = "Could not load image \"%s\" %s" % (file, pygame.get_error())
        raise SystemExit(error)
    return surface.convert()


def main(window, menu_config):
    """ The main function of the view of menu"""

    # Init window
    screen = window

    # Load background image
    bgd_tile = loadImage("bgd_menu.png")
    background = pygame.Surface((menu_config["width"], menu_config["height"]))
    background.blit(bgd_tile, (0, 0))

    # Prepare text
    title_font = pygame.font.Font(None, 36)
    text = title_font.render("Black Jack Project", 2, (255, 255, 255))

    # Display on windows
    screen.blit(background, (0, 0))
    screen.blit(text, (80, 30))
    pygame.display.flip()

    # Init sprites
    all_sprites = pygame.sprite.RenderUpdates()
    clock = pygame.time.Clock()

    play = True
    while play:

        # Clear all the sprites
        all_sprites.clear(screen, bgd_tile)
        all_sprites.update()

        # Check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                play = False

        # Update the scene
        dirty = all_sprites.draw(screen)
        pygame.display.update(dirty)

        clock.tick(40)

    pygame.quit()
    return '', dict()


if __name__ == '__main__':
    main()