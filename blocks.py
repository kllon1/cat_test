import pygame
from os import path

PLATF_WIDTH = 32
PLATF_HEIGHT = 32
PLATFORM_COLOR = (0, 0, 255)

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PLATF_WIDTH, PLATF_HEIGHT))
        self.image.fill(PLATFORM_COLOR)
        #self.image = image.load("%s/blocks/platform.png" % ICON_DIR)
        self.rect = pygame.Rect(x, y, PLATF_WIDTH, PLATF_HEIGHT)


