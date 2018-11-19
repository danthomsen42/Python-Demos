import pygame, random
from scripts.Time import Timer
from scripts.globals import Globals
from scripts.textures import Tiles

pygame.init()

def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[0] / 2), int(size[1] / 2))

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0,0), (0,0, tile_size[0], tile_size[1]))
    faces["south"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    faces["north"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    faces["east"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE | pygame.SRCALPHA)
    west.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))
    faces["west"] = west

    return faces

def MoveNPC(npc):
    npc.facing = random.choice(("south", "north", "east", "west"))
    #npc.facing = "south"
    npc.walking = random.choice((False, False))

class Dialog:
    def __init__(self, text):
        self.Page = 0
        self.Text = text # [("Hello world", "Can You do this thing for me?"), ("It would mean a lot to me!", "Please help"), ("Thank you ever so much!", "GoodBye!")] - Tuples in a List

class NPC:

    AllNPCs = []

    def __init__(self, name, pos, dialog, sprite):
        self.Name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.walking = False
        self.Timer = Timer(1)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Timer.Start()

        self.LastLocation = [0, 0]

        #GET NPC FACES
        self.facing = "south"
        self.faces = get_faces(sprite)

        #PUBLISH
        NPC.AllNPCs.append(self)

    def Render(self, surface):
        self.Timer.Update()
        if self.walking:
            move_speed = 100 * Globals.deltatime
            if self.facing == "south":
                self.Y += move_speed
            elif self.facing == "north":
                self.Y -= move_speed
            elif self.facing == "east":
                self.X -= move_speed
            elif self.facing =="west":
                self.X += move_speed

        #Block tile NPC is currently standing on
        location = [round(self.X/Tiles.Size), round (self.Y / Tiles.Size)]
        if self.LastLocation in Tiles.Blocked:
            Tiles.Blocked.remove(self.LastLocation)

        if not location in Tiles.Blocked:
            Tiles.Blocked.append(location)
            self.LastLocation = location

        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))

class FLAMENPC:

    AllNPCs = []

    def __init__(self, name, pos, dialog, sprite):
    # def __init__(self, name, pos, sprite):
        self.Name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.walking = False
        self.Timer = Timer(0.1)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Timer.Start()

        self.LastLocation = [0, 0]

        #GET NPC FACES
        self.facing = "south"
        self.faces = get_faces(sprite)

        #PUBLISH
        NPC.AllNPCs.append(self)

    def Render(self, surface):
        self.Timer.Update()
        if self.walking:
            move_speed = 200 * Globals.deltatime
            if self.facing == "south":
                self.Y += move_speed
            elif self.facing == "north":
                self.Y -= move_speed
            elif self.facing == "east":
                self.X -= move_speed
            elif self.facing =="west":
                self.X += move_speed

        #Block tile NPC is currently standing on
        location = [round(self.X/Tiles.Size), round (self.Y / Tiles.Size)]
        if self.LastLocation in Tiles.Blocked:
            Tiles.Blocked.remove(self.LastLocation)

        if not location in Tiles.Blocked:
            Tiles.Blocked.append(location)
            self.LastLocation = location

        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))



class INANIMATE:

    AllNPCs = []

    def __init__(self, name, pos, dialog, sprite):
        self.Name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        #self.walking = False
        #self.Timer = Timer(0.1)
        #self.Timer.OnNext = lambda: MoveNPC(self)
        #self.Timer.Start()

        #self.LastLocation = [0, 0]

        #GET NPC FACES
        self.facing = "south"
        #self.faces = get_faces(sprite)

        #PUBLISH
        #NPC.AllNPCs.append(self)

    def Render(self, surface):
        #self.Timer.Update()
        # if self.walking:
        #     move_speed = 200 * Globals.deltatime
        #     if self.facing == "south":
        #         self.Y += move_speed
        #     elif self.facing == "north":
        #         self.Y -= move_speed
        #     elif self.facing == "east":
        #         self.X -= move_speed
        #     elif self.facing =="west":
        #         self.X += move_speed
        #
        # #Block tile NPC is currently standing on
        # location = [round(self.X/Tiles.Size), round (self.Y / Tiles.Size)]
        # if self.LastLocation in Tiles.Blocked:
        #     Tiles.Blocked.remove(self.LastLocation)
        #
        # if not location in Tiles.Blocked:
        #     Tiles.Blocked.append(location)
        #     self.LastLocation = location

        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))






class Male1(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\NPC\\fathertime2.png"))

class InnerThought(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\water.png"))

class InnerThought2(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\sand.png"))

class Male2(NPC):
   def __init__(self, name, pos, dialog = None):
       super().__init__(name, pos, dialog, pygame.image.load("Graphics\\NPC\\doctor2.png"))

class Male3(NPC):
   def __init__(self, name, pos, dialog = None):
       super().__init__(name, pos, dialog, pygame.image.load("Graphics\\NPC\\ghost.png"))

class Wife(NPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\NPC\\bed_ridden.png"))

class Flame(FLAMENPC):
    def __init__(self, name, pos, dialog = None):
        super().__init__(name, pos, dialog, pygame.image.load("Graphics\\fire2.png"))
    #def __init__(self, name, pos):
     #   super().__init__(name, pos, pygame.image.load("Graphics\\fire2.png"))