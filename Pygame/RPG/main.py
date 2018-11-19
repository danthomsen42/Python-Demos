import pygame, sys, time, math, os
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
from scripts.meloonatic_gui import *


pygame.init()

cSec = 0
cFrame = 0
FPS = 0

map_data = []

#MAPLOCATION = input("Type Map Name: ")

terrain = Map_Engine.load_map("maps\\overworld.map")
#terrain = Map_Engine.load_map("maps\\" + MAPLOCATION + ".map")
clock = pygame.time.Clock()

Tiles.Size = 32

#fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)
fps_font = pygame.font.SysFont("Verdana", 20)

sky = pygame.image.load("Graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

fog = pygame.image.load("Graphics\\fog.png")
Fog = pygame.Surface(fog.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Fog.blit(fog, (0,0))
del fog


logo_img_temp = pygame.image.load("Graphics\\logo.png")
logo_img_temp = pygame.transform.scale(logo_img_temp, (800, 600))
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0,0))
del logo_img_temp

dialog_background = pygame.image.load("Graphics\\gui\\textbox2.png")
Dialog_Background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Dialog_Background.blit(dialog_background, (0,0))
Dialog_Background_Width, Dialog_Background_Height = Dialog_Background.get_size()
del dialog_background


clock = pygame.time.Clock()

def show_fps():
    fps_overlay = fps_font.render("FPS: " + (str(FPS)), True, Color.Goldenrod)
    window.blit(fps_overlay, (0,0))
    #print("no")

def create_window():
    global window, window_height, window_width, window_title, clock
    window_width, window_height = 800, 600
    window_title = "RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    clock = pygame.time.Clock()


def count_fps():
    global cSec, cFrame, FPS

    FPS = clock.get_fps()
    if FPS > 0:
        Globals.deltatime = 1 / FPS

    # if cSec == time.strftime("%S"):
    #     cFrame += 1
    # else:
    #     FPS = cFrame
    #     cFrame = 0
    #     cSec = time.strftime("%S")
    #     if FPS > 0:
    #         deltatime = 1 / FPS

create_window()

player = Player("Death")
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size

#Initialize Music
pygame.mixer.music.load("music_and_sounds\\Private_Reflection.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

#Initialize sounds
step = pygame.mixer.Sound("music_and_sounds\\softStep.wav")
step.set_volume(0.1)



man1 = Male1(name = "FatherTime", pos = (1792, 200), dialog = Dialog(text = [("Father Time: My imortal friend", "What can I do for you?"),
                                                                             ("Father Time: You usually show no interest", "in your...charges."),
                                                                             ("Death: .....", "It's me"),
                                                                             ("Father Time: You realize what you see will only", "resutlt in a paradox, don't you?"),
                                                                             ("Death: I'm not asking about who I am...", "...but who I was."),
                                                                             ("Father Time: *relieved sigh* That's much easier", "Just give me a moment, and... there!", "Here you are. Any particular time?"),
                                                                             ("Death: Go a little later, towards my...", "...end"),
                                                                             ("Father Time: Go over to your right", "What you seek is there")]))
#man2 = Male1(name = "David", pos = (300, 400), dialog = Dialog(text = [("Hello world", "Can You do this thing for me?"), ("It would mean a lot to me!", "Please help"), ("Thank you ever so much!", "GoodBye!")]))

intro1 = InnerThought(name = "deepthought1", pos = (1000, 675), dialog = Dialog(text = [("As the water ripples, so is a life.", ""),
                                                                                       ("It begins small, but its influence on others spreads", "but thins with age and then ends."),
                                                                                       ("Not so with me.", "Why am I here and if I just have been,", "how can I have this empathy?")]))

wife = InnerThought2(name = "deepthought1", pos = (2832, 250), dialog = Dialog(text =[("Death: I recognize this women...", "Why?")]))

doctor = Male2(name = "FatherTime", pos = (2992, 200), dialog = Dialog(text = [("This man looks familiar...", "How do I know these people")]))

ghost = Male3(name = "Ghost", pos = (550, 1600), dialog = Dialog(text = [("Death: Do you still wish to see the world?", "Take my Burden")]))

fire = Flame(name = "Fire1", pos = (400, 1700), dialog = Dialog(text = [("Hot","")]))
fire2 = Flame(name = "Fire1", pos = (410, 1730), dialog = Dialog(text = [("Hot","")]))
fire3 = Flame(name = "Fire1", pos = (430, 1700), dialog = Dialog(text = [("Hot","")]))
fire4 = Flame(name = "Fire1", pos = (400, 1600), dialog = Dialog(text = [("Hot","")]))
fire5 = Flame(name = "Fire1", pos = (460, 1620), dialog = Dialog(text = [("Hot","")]))
fire6 = Flame(name = "Fire1", pos = (390, 1590), dialog = Dialog(text = [("Hot","")]))
fire7 = Flame(name = "Fire1", pos = (2775, 1600), dialog = Dialog(text = [("Hot","")]))
fire8 = Flame(name = "Fire1", pos = (2750, 1620), dialog = Dialog(text = [("Hot","")]))
#fire9 = Flame(name = "Fire1", pos = (200, 300), dialog = Dialog(text = [("Hot"),""]))
#fire10 = Flame(name = "Fire1", pos = (200, 300), dialog = Dialog(text = [("Hot"),""]))

#wifeY = Wife(name = "wifeYoung", pos = (2700, 375), dialog = Dialog(text =[("Death: I recognize this women...", "Why?")]))




TestDialog = Dialog(text = [("How...", "How do I know..."), ("How do I know", "what it's like to die?"), ("How do I remember pain", "if I've done this forever?")])
Globals.active_dialog = TestDialog

#INITIALIZE GUI

#def mapEditor():
#    Globals.scene = "map_editor"

def Play():
    pygame.mixer.music.load("music_and_sounds\\Spacial_Harvest.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    Globals.scene = "game"

def Exit():
    global isRunning
    isRunning = False

btnPlay = Menu.Button(text = "Play", rect = (0, 0, 160, 60), tag =("menu", None))


btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Command = Play
btnExit = Menu.Button(text = "Exit", rect = (0, 0, 160, 60), tag =("menu", None))
#btnExit = Menu.Button(text = "Exit", rect = (0, 0, 160, 60),
                     # tag =("menu", None))

btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 10
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Death Remembered", color = Color.Red, font = Font.Large)

menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0


logo = Menu.Image(bitmap = logo_img)


isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not Globals.dialog_open:
                Globals.camera_move = 1
                player.facing = "north"
                step.play(-1)
            elif event.key == pygame.K_s and not Globals.dialog_open:
                Globals.camera_move = 2
                player.facing = "south"
                step.play(-1)
            elif event.key == pygame.K_a and not Globals.dialog_open:
                Globals.camera_move = 3
                player.facing = "east"
                step.play(-1)
            elif event.key == pygame.K_d and not Globals.dialog_open:
                Globals.camera_move = 4
                player.facing = "west"
                step.play(-1)

            if event.key == pygame.K_t:
                if Globals.dialog_open:
                    #Handle Next Page of Open Dialog
                    if Globals.active_dialog.Page < len(Globals.active_dialog.Text) - 1:
                        Globals.active_dialog.Page += 1
                    else:
                        Globals.dialog_open = False
                        Globals.active_dialog.Page = 0
                        Globals.active_dialog = None
                        # Unpuase any paused NPC'S
                        for npc in NPC.AllNPCs:
                            if not npc.Timer.Active:
                                npc.Timer.Start()
            else:
                #If Dialog isn't open
                for npc in NPC.AllNPCs:
                    #Is player in speech Bounds
                    #Player Cords are by Tile
                    #NPC Coords are by Pixel
                    #THis Causes Confusion
                    npc_x = npc.X / Tiles.Size
                    npc_y = npc.Y / Tiles.Size
                    if player_x >= npc_x - 2 and player_x <= npc_x + 2 and player_y >= npc_y - 2 and player_y <= npc_y + 2:
                        # Player is next to an NPC, However is Player facing them?
                        if player.facing == "north" and npc_y < player_y:
                            Globals.dialog_open = True
                            Globals.active_dialog = npc.Dialog
                            npc.Timer.Pause()
                            npc.walking = False

                        elif player.facing == "south" and npc_y > player_y:
                            Globals.dialog_open = True
                            Globals.active_dialog = npc.Dialog
                            npc.Timer.Pause()
                            npc.walking = False

                        elif player.facing == "east" and npc_x < player_x:
                            Globals.dialog_open = True
                            Globals.active_dialog = npc.Dialog
                            npc.Timer.Pause()
                            npc.walking = False

                        elif player.facing == "west" and npc_x > player_x:
                            Globals.dialog_open = True
                            Globals.active_dialog = npc.Dialog
                            npc.Timer.Pause()
                            npc.walking = False



        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:# LEFT CLICK
                # HANDLE BUTTON CLICK EVENTS
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() # DO BUTTON EVENT
                        btn.Rolling = False
                        break # EXIT LOOP

        # Using else: works just as well as this whole elif statement
        # elif event.type == pygame.KEYUP:
        else:
            step.stop()
            Globals.camera_move = 0
    #Render Scene
    if Globals.scene == "game":

            #print("uhh")
        #Logic
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 100 * Globals.deltatime
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 100 * Globals.deltatime
        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 100 * Globals.deltatime
        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 100 * Globals.deltatime

        player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size
        player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size




        #Render Graphics
        #window.fill(Color.Black)
        window.blit(Sky, (0,0))
        window.blit(terrain, (Globals.camera_x, Globals.camera_y))

        for npc in NPC.AllNPCs:
            npc.Render(window)

        player.render(window, (window_width / 2 - player_w / 2, window_height / 2 - player_h / 2))



        if Globals.dialog_open:
            window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height - 2))

            #DRAW DIALOG TEXT
            if Globals.active_dialog != None:
                lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

                for line in lines:
                    #DRAW TEXT TO SCREEN
                    window.blit(Font.Default.render(line, True, Color.Red), (130, (window_height - Dialog_Background_Height) + 5 + (lines.index(line)) * 25))

        window.blit(Fog, (0,0))

        #for t in Tiles.Blocked:
        #    pygame.draw.rect(window, Color.Red, (t[0] * Tiles.Size + Globals.camera_x, t[1] * Tiles.Size + Globals.camera_y, Tiles.Size, Tiles.Size), 2)
                                        # - Render Simple Terrain Grid
                                    #    for x in range(0, 640, Tiles.Size):
                                    #        for y in range(0, 480, Tiles.Size):
                                    #            for i in map_data:
                                    #                tile = (i[0] * Tiles.Size, i[1] * Tiles.Size)
                                    #                if (x, y) == tile:
                                    #                    window.blit(Tiles.Texture_Tags[i[2]], (x + Globals.camera_x, y + Globals.camera_y))

                                                #pygame.draw.rect(window, Color.White, (x, y, Tiles.Size + 1, Tiles.Size + 1), 1)
     #ProcessMenu                                           #window.blit(Tiles.Tiles, (x + Globals.camera_x, y + Globals.camera_y))
    elif Globals.scene == "menu":
        window.fill(Color.Fog)
        logo.Render(window)
        menuTitle.Render(window)

        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                #btnPlay.Render(window)
                #btnExit.Render(window)
                btn.Render(window)


    #elif Globals.scene == "map_editor":
    #    os.startfile()


    show_fps()
    #print("y")

    pygame.display.update()
    clock.tick()
    count_fps()


pygame.quit()
sys.exit()