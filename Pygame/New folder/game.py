import pygame
pygame.init()

winW = 1000
winH = 544
win = pygame.display.set_mode((winW, winH))
pygame.display.set_caption("Platform Start")

x = 50
y = 430
width = 40
height = 60
vel = 5
jumpDir = True
isJump = False
jumpCount = 20
left = False
right = False
walkCount = 0
shoot = False
#direction = False
clock = pygame.time.Clock()
shootEffect = pygame.mixer.Sound('sounds/shoot.wav')
bounceEffect = pygame.mixer.Sound('sounds/jump2.wav')
backgroundMusic = pygame.mixer.music.load('sounds/background1.mp3')
pygame.mixer.music.play(-1)
def p(filename):
        return pygame.image.load(filename)

def op(filename, left, right):
    if right:
        return pygame.image.load(filename)
    elif left:
        image = pygame.image.load(filename)
        return pygame.transform.flip(image, False, True)
        #image = pygame.transform.flip(filename, False, True)
        #return pygame.image.load(image)
        #pass
    #else:
     #   pass


platform = p('platform1.png')
walkright = [p("pics/mainPics/Run1.png"), p("pics/mainPics/Run2.png"), p("pics/mainPics/Run3.png"), p("pics/mainPics/Run4.png"), p("pics/mainPics/Run5.png"), p("pics/mainPics/Run6.png"), p("pics/mainPics/Run7.png"), p("pics/mainPics/Run8.png")]
walkleft = [p("pics/mainPics/RunL1.png"), p("pics/mainPics/RunL2.png"), p("pics/mainPics/RunL3.png"), p("pics/mainPics/RunL4.png"), p("pics/mainPics/RunL5.png"), p("pics/mainPics/RunL6.png"), p("pics/mainPics/RunL7.png"), p("pics/mainPics/RunL8.png")]
#shootright = [op("pics/mainPics/RunShoot1.png", left, right), op("pics/mainPics/RunShoot2.png", left, right), op("pics/mainPics/RunShoot3.png", left, right), op("pics/mainPics/RunShoot4.png", left, right), op("pics/mainPics/RunShoot5.png", left, right), op("pics/mainPics/RunShoot6.png", left, right), op("pics/mainPics/RunShoot7.png", left, right), op("pics/mainPics/RunShoot8.png", left, right) ]
shootleft = [p("pics/mainPics/RunShootL1.png"), p("pics/mainPics/RunShootL2.png"), p("pics/mainPics/RunShootL3.png"), p("pics/mainPics/RunShootL4.png"), p("pics/mainPics/RunShootL5.png"), p("pics/mainPics/RunShootL6.png"), p("pics/mainPics/RunShootL7.png"), p("pics/mainPics/RunShootL8.png")]
shootright = [p("pics/mainPics/RunShoot1.png"), p("pics/mainPics/RunShoot2.png"), p("pics/mainPics/RunShoot3.png"), p("pics/mainPics/RunShoot4.png"), p("pics/mainPics/RunShoot5.png"), p("pics/mainPics/RunShoot6.png"), p("pics/mainPics/RunShoot7.png"), p("pics/mainPics/RunShoot8.png")]
#shootleft = []
HW, HH = winW / 2, winH / 2
bg = p('pics/mainPics/platform.png')
obstacle_rect = bg.get_rect()
ox = HW - obstacle_rect.center[0]
oy = HH - obstacle_rect.center[1]


obstacle2 = pygame.image.load("platform_mask2.png").convert_alpha()
obstacle_mask = pygame.mask.from_surface(obstacle2)
#idle = [p('pics/mainPics/idle1.png'), p('pics/mainPics/idle2.png'), p('pics/mainPics/idle3.png'), p('pics/mainPics/idle4.png'), p('pics/mainPics/idle5.png'), p('pics/mainPics/idle6.png'), p('pics/mainPics/idle7.png'), p('pics/mainPics/idle8.png')]
idle = p('pics/mainPics/idle1.png')
idleL = p('pics/mainPics/idleL1.png')
idleShoot = p('pics/mainPics/Shoot4.png')
idleShootL = p('pics/mainPics/ShootL4.png')
jumpRight = []
jumpLeft = []
direction = 0
def redrawGameWindow():
    global walkCount
    global direction
    win.blit(bg, (0,0))

    win.blit(platform, (400,400))
    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    #win.fill((0,0,0))
    if walkCount + 1 >= 27:
        walkCount = 0


    if left:
        if shoot:
            win.blit(shootleft[walkCount//4], (x,y))
            walkCount += 1
            direction = 1
        else:
            win.blit(walkleft[walkCount//4], (x,y))
            walkCount += 1
            direction = 1

    elif right:
        if shoot:
            win.blit(shootright[walkCount // 4], (x, y))
            walkCount += 1
            direction = 0
        else:
            win.blit(walkright[walkCount//4], (x,y))
            walkCount += 1
            direction = 0
        #
        # walkCount += 1


    else:
        if direction == 0:
            if shoot:
                win.blit(idleShoot, (x,y))
            else:
                win.blit(idle, (x,y))
        else:
            if shoot:
                win.blit(idleShootL, (x,y))
            else:
                win.blit(idleL, (x,y))
    pygame.display.update()

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tempV = vel


    keys = pygame.key.get_pressed()


    #offset = (int(x - ox), int(y - oy))
#    result = obstacle_mask.overlap(blob_mask, offset)


    if keys[pygame.K_LEFT] and  x > vel:
        x -= vel
        left = True
        right = False
        if keys[pygame.K_x]:
            shoot = True
            shootEffect.play()
        else:
            shoot = False
    elif keys[pygame.K_RIGHT] and x < winW - width - vel:
        x += vel
        right = True
        left = False
        if keys[pygame.K_x]:
            shoot = True
            shootEffect.play()
        else:
            shoot = False
    else:
        right = False
        left = False
        walkCount = 0
        if keys[pygame.K_x]:
            shoot = True
            shootEffect.play()
        else:
            shoot = False

    if not (isJump):
        #if keys[pygame.K_UP] and y > vel:
         #   y -= vel
        #if keys[pygame.K_DOWN] and y < winH - height - vel:
         #   y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
            bounceEffect.play()

    else:
        if jumpCount >= -20:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * .05 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 20

    redrawGameWindow()

pygame.quit()