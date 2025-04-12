import pygame as pg
import os

PLATFORM_WD = 32
PLATFORM_HT = 32
PLATFORM_CL = '#FF6262'
ICON_DIR = os.path.dirname(__file__)

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Surface.__init__(self)

        self.image = pg.Surface(
            (PLATFORM_WD,
             PLATFORM_HT)
        )
        self.image.fill(pg.Color(PLATFORM_CL))
        self.image = pg.image.load('blocks/platform.png' % ICON_DIR)
        self.rect = pg.Rect(x, y, PLATFORM_WD, PLATFORM_HT)