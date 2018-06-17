# -*- coding: utf-8 -*-

import pygame
from src.common.constants import *


def load_image(file):
    """
    Loads an image, prepares it for play
    """

    file = os.path.join(DIR_PICTURES, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        error = "Could not load image \"%s\" %s" % (file, pygame.get_error())
        raise SystemExit(error)
    return surface.convert()
