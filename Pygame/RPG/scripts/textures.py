import pygame

pygame.init()



class Tiles:
    Size = 32
    Blocked = []
    Blocked_Types = ["5", "6", "7", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "25", "27", "28", "29"]

    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False


    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface


    Tiles = Load_Texture("Graphics\\hospitalTile.png", Size)
    Stone = Load_Texture("Graphics\\stone.png", Size)
    Grass = Load_Texture("Graphics\\grass.png", Size)
    Water = Load_Texture("Graphics\\water.png", Size)

    Machine = Load_Texture("Graphics\\hospitalTileMachine.png", Size*4)
    WifeY = Load_Texture("Graphics\\young_bed.png", Size*4)
    WifeO = Load_Texture("Graphics\\old_bed.png", Size*4)
    DoorOpen = Load_Texture("Graphics\\door_open.png", Size)
    DoorClosed = Load_Texture("Graphics\\door_closed.png", Size)

    WallLeft = Load_Texture("Graphics\\leftwall.png", Size)
    WallUpper = Load_Texture("Graphics\\upperwall.png", Size)
    WallRight = Load_Texture("Graphics\\rightwall.png", Size)
    WallLower = Load_Texture("Graphics\\lowerwall.png", Size)
    UpperLeftCorner = Load_Texture("Graphics\\left_upperCorner.png", Size)
    UpperRightCorner = Load_Texture("Graphics\\right_upperCorner.png", Size)
    LowerRightCorner = Load_Texture("Graphics\\right_lowerCorner.png", Size)
    LowerLeftCorner = Load_Texture("Graphics\\left_lowerCorner.png", Size)

    TowerWall = Load_Texture("Graphics\\Towerwall.png", Size)
    TowerWallLeft = Load_Texture("Graphics\\TowerwallLeft.png", Size)
    TowerWallRight = Load_Texture("Graphics\\TowerwallRight.png", Size)
    WoodFloor = Load_Texture("Graphics\\woodfloor.png", Size)

    Balloons = Load_Texture("Graphics\\balloons.png", Size)
    Yellow = Load_Texture("Graphics\\yellow.png", Size)
    White = Load_Texture("Graphics\\white.png", Size)
    Tombstone = Load_Texture("Graphics\\tombstone.png", Size)
    Sand = Load_Texture("Graphics\\sand.png", Size)
    Plane = Load_Texture("Graphics\\plane.png", Size * 8)
    Car1 = Load_Texture("Graphics\\car3.png", Size * 6)
    Car2 = Load_Texture("Graphics\\car4.png", Size * 6)

    Texture_Tags = {"1" : Grass,
                    "2" : Stone,
                    "3" : Water,
                    "4" : Tiles,
                    "5" : Machine,
                    "6" : WifeY,
                    "7" : WifeO,
                    "8" : DoorOpen,
                    "9" : DoorClosed,
                    "10" : WallLeft,
                    "11" : WallUpper,
                    "12" : WallRight,
                    "13" : WallLower,
                    "14" : UpperLeftCorner,
                    "15" : UpperRightCorner,
                    "16" : LowerRightCorner,
                    "17" : LowerLeftCorner,
                    "18" : TowerWall,
                    "19" : TowerWallLeft,
                    "20" : TowerWallRight,
                    "21" : WoodFloor,
                    "22" : Balloons,
                    "23" : Yellow,
                    "24" : White,
                    "25" : Tombstone,
                    "26" : Sand,
                    "27" : Plane,
                    "28" : Car1,
                    "29" : Car2}