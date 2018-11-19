import pygame
from scripts.NPC import *

pygame.init()

class Player:
    def __init__(self, name):
        self.name = name
        self.facing = "south"
        self.health = 100
        sprite = pygame.image.load("graphics\\death_scythe_full.png")
        # self.mapping = {
        #     "south": [(0, 48 * i, 48, 48) for i in xrange(4)],
        #     "west": [(48, 48 * i, 48, 48) for i in xrange(4)],
        #     "north": [(96, 48 * i, 48, 48) for i in xrange(4)],
        #     "east": [(144, 48 * i, 48, 48) for i in xrange(4)]
        # }
        #self.facing = "up"

        size = sprite.get_size()
        self.width = size[0]
        self.height = size[1]

        # Get Player Direction
        self.faces = get_faces(sprite)

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)