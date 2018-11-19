import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, x ,y):
        super(Player, self).__init__(x, y)
        self.charRight = grahpics.load("spriteCharRight")

