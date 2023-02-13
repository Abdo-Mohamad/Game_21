from pygame import *
import pygame
import sys
import Button

init()
screen = pygame.display.set_mode([0, 0],pygame.FULLSCREEN)
clock = pygame.time.Clock()
Juego = True

BotonX = pygame.image.load("X.png").convert_alpha()
BotonY = pygame.image.load("X1.png").convert_alpha()


X_button = Button.Button(100, 200, BotonX, BotonY, 0.05)

while Juego == True:
    screen.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    if X_button.draw():
        Juego = False
    clock.tick(60)
    pygame.display.flip()