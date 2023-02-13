

import pygame
import sys
from button import Button

pygame.init()

# Set screen size and caption
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
# Create a font for displaying text
font = pygame.font.Font(None, 36)
# Create the exit button
pygame.display.set_caption("Menu")


def bg_img(width, height, screen):
    bg_img = pygame.image.load('background.jpg')
    bg_img = pygame.transform.scale(bg_img, (width, height))
    screen.blit(bg_img, (0, 0))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(None, size)


def exitButton(screen):
    while True:
        screen.fill((0, 0, 1))
        bg_img(width, height, screen)
        exit_button = pygame.Rect(700, 550, 80, 50)
        # Set the font for the button text
        font = pygame.font.Font(None, 30)
        # Set the text for the button
        exit_text = font.render("Exit", True, (255, 255, 255))
        # Draw the button on the screen
        pygame.draw.rect(screen, (0, 0, 255), exit_button)
        screen.blit(exit_text, (725, 570))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mouse.get_pressed()[0]:
            if exit_button.collidepoint(pygame.mouse.get_pos()):
                print('clickd')
                main_menu()
        pygame.display.update()





def main_menu():
    bg_img(width, height, screen)
    run = True
    while run:
        print('soy el menu')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mouse.get_pressed()[0]:
            if exitButton(screen).collidepoint(pygame.mouse.get_pos()):
                print('clickd')
                screen.fill((0, 0, 1))
                run = False
        pygame.display.update()


main_menu()
