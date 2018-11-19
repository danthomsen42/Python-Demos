#Pygame template
import pygame
import random
from settings import *

#Inititializers
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False


    #Update


    #Draw / render
    screen.fill(BLACK)

    #*after* drawing everything, f;ip the display
    pygame.display.flip()

pygame.quit()