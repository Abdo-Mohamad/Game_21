import pygame
from pygame.locals import *
import sys
import random
import time
import numpy as np
# Initialize Pygame


pygame.init()

# Set screen size and caption
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height), FULLSCREEN)
pygame.display.set_caption("21 (Blackjack)")
# Set font and size
font = pygame.font.SysFont('arial', 30)
# Create the exit butt
 # Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
hover_color = (255, 0, 0)
button_color = (65, 93, 54)

def exitButton(screen):
    exit_button = pygame.Rect(1390, 0, 70, 60)
    # Set the font for the button text
    # Set the text for the button
    exit_text = font.render("X", True, (255, 255, 255))
    # Draw the button on the screen
    mouse_pos = pygame.mouse.get_pos()
    if exit_button.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = button_color
    pygame.draw.rect(screen, color, exit_button)
    screen.blit(exit_text, (1407, 18))
    return exit_button

# Create the stand button

def standButton(screen):
    stand_button = pygame.Rect(760, 700, 100, 75)
    # Set the font for the button text
    # Set the text for the button
    stand_text = font.render("Stand", True, (255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    if stand_button.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = button_color
    # Draw the button on the screen
    pygame.draw.rect(screen, color, stand_button)
    screen.blit(stand_text, (780, 730))
    return stand_button


def playAgain(screen):
    play_again = pygame.Rect(680, 600, 140, 70)
    # Set the font for the button text
    # Set the text for the button
    play_again_text = font.render("play Again", True, (255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    if play_again.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = button_color
    # Draw the button on the screen
    pygame.draw.rect(screen, color, play_again)
    screen.blit(play_again_text, (700, 624))
    return play_again


def backs(screen):
    back_m = pygame.Rect(0, 0, 100, 50)
    # Set the font for the button text
    # Set the text for the button
    back_m_text = font.render("Back", True, (255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    if back_m.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = button_color
    # Draw the button on the screen
    pygame.draw.rect(screen, color, back_m)
    screen.blit(back_m_text, (12, 16))
    return back_m


def hit_Buton(screen):
    hit_button = pygame.Rect(640, 700, 100, 75)
    # Set the font for the button text
    # Set the text for the button
    hit_text = font.render("Hit", True, (255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    if hit_button.collidepoint(mouse_pos):
        color = hover_color
    else:
        color = button_color
    # Draw the button on the screen
    pygame.draw.rect(screen, color, hit_button)
    screen.blit(hit_text, (675, 730))
    return hit_button


def bg_img(width, height, screen):
    bg_img = pygame.image.load('cards/background.jpg')
    bg_img = pygame.transform.scale(bg_img, (width, height))
    screen.blit(bg_img, (0, 0))


def new_func(card_values, card_suits, deck):
    for value in card_values:
        for suit in card_suits:
            card = value + suit

            deck.append(card)


def deck_mezclada(deck):
    deckMezclada = deck
    random.shuffle(deckMezclada)
    # print(deckMezclada)
    return deckMezclada


def hand(h1):
    h1.append(deckMezclada.pop())

# for i in range(numCards):
#     hand(dealer_hand,2)


def haveCardDealer(dealer_hand, hand):
    while len(dealer_hand) < 1:
        hand(dealer_hand)


def haveCardPlayer(player_hand, hand):
    while len(player_hand) < 2:
        # print(numCards, "test")
        hand(player_hand)


def draw_card(screen, card_images, dealer_hand, player_hand):
    image_size_w = 150
    image_size_h = 225
    for i, cardy in enumerate(dealer_hand):
        y = i * 200
        # print(i)
        if i < 1:

            imagey = pygame.transform.scale(
                card_images[cardy], (image_size_w, image_size_h))
            screen.blit(imagey, (y, 50))
            back = pygame.image.load('cards/card_back.jpg')
            back = pygame.transform.scale(
                back, (image_size_w, image_size_h))
            screen.blit(back, (y+200, 50))

        else:
            imagey = pygame.transform.scale(
                card_images[cardy], (image_size_w, image_size_h))
            screen.blit(imagey, (y, 50))

    for i, cardx in enumerate(player_hand):
        x = i * 100
        if i < 2:
            if x == 0:
                x = 20
            imagex = pygame.transform.scale(
                card_images[cardx], (image_size_w, image_size_h))
            screen.blit(imagex, (x, 400))
            if x == 1:
                screen.blit(imagex, (x, 200))
        else:
            imagex = pygame.transform.scale(
                card_images[cardx], (image_size_w, image_size_h))
            screen.blit(imagex, (x, 400))


def check_player_value(screen, font, card_images, dealer_hand, player_hand, draw_card, player_value):
    if player_value == 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        bg_img(width, height, screen)
        backs(screen)
        exitButton(screen)
        playAgain(screen)
        draw_card(screen, card_images, dealer_hand, player_hand)
        player_message = font.render(
            "Player wins with 21 (Blackjack)!", True, (20, 255, 255))
        screen.blit(player_message, (200, 300))
        pygame.display.flip()
        return True

    elif player_value > 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        bg_img(width, height, screen)
        backs(screen)
        exitButton(screen)
        playAgain(screen)
        draw_card(screen, card_images, dealer_hand, player_hand)
        player_bust_message = font.render(
            "Player busts!", True, (255, 55, 255))
        screen.blit(player_bust_message, (200, 300))
        pygame.display.flip()
        return True
    else:
        return False


def check_dealer_value(player_value, dealer_value):
    if dealer_value == 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        bg_img(width, height, screen)
        backs(screen)
        exitButton(screen)
        playAgain(screen)
        draw_card(screen, card_images, dealer_hand, player_hand)
        dealer_message = font.render(
            "Dealer wins with 21 (Blackjack)!", True, (25, 255, 255))
        screen.blit(dealer_message, (200, 300))
        pygame.display.flip()
        return True

        # Check for bust
    elif dealer_value > 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        bg_img(width, height, screen)
        backs(screen)
        exitButton(screen)
        playAgain(screen)
        draw_card(screen, card_images, dealer_hand, player_hand)
        dealer_bust_message = font.render(
            "Dealer busts!", True, (255, 255, 55))
        screen.blit(dealer_bust_message, (200, 300))
        pygame.display.flip()
        return True

    elif dealer_value >= player_value < 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        bg_img(width, height, screen)
        backs(screen)
        exitButton(screen)
        playAgain(screen)
        draw_card(screen, card_images, dealer_hand, player_hand)
        dealer_bust_message = font.render(
            "Dealer Win!", True, (255, 255, 55))
        screen.blit(dealer_bust_message, (200, 300))
        pygame.display.flip()
        return True
    else:
        return False


# Create menu items
menu_items = ['Start', 'Rules', 'Quit']

# Create a list to store the menu items' rectangles
item_rects = []

# Draw player and dealer hands
for index, item in enumerate(menu_items):
    item_rect = pygame.Rect(650, 300 + index * 100, 200, 50)
    item_rects.append(item_rect)
    # Fill the screen with white


def menu_optinos(screen, font, BLACK, menu_items, item_rects):

    # Draw the menu items
    for index, item in enumerate(menu_items):
        text = font.render(item, True, WHITE)
        screen.blit(text, (700, 315 + index * 100))
        font2 = pygame.font.SysFont('didot.ttc', 72)
        img2 = font2.render('Black Jack 21', True, BLACK)
        screen.blit(img2, (600, 115))


clock = pygame.time.Clock()
# Create a varibel for displaying text
regles = ("————Reglas————",
     "El objetivo del juego es conseguir o aproximarse al número 21","sumando el número de las cartas que te aparecen",


     "Si la suma de los números de tus cartas superan 21 pierdes.",
     "Si el valor de la suma de las cartas es igual a 21 automáticamente ganas.",
     "Empiezas con 2 cartas, donde la suma máxima de las 2 cartas iniciales es 20.",
     "El crupier solo participa en el juego si el jugador se ha quedado con un valor",
     "inferior o igual a 20.",




     "·····Valor de la cartas·····",
     "Las cartas con un valor numérico se quedan igual, es decir el 2 vale 2 y el 10",
     "vale 10, así con todos los números.",
     "El valor de las figuras es el siguiente:",
     "J, Q, K = 10",
     "A = 1")
def text(screen):
   for i, x in enumerate(regles):
       print(x)
       r = 100
       c = 400
       y = i * 50 + r
       if i == 0:
           y = r
           c = 600
       elif i == 8:
           c = 600
       img = font.render(x, True, (0, 0, 0))
       screen.blit(img, (c, y))
while True:
    bg_img(width, height, screen)

    # Create a rectangle for each menu item
    menu_optinos(screen, font, BLACK, menu_items, item_rects)

    # Main game loop

    # Inicialización de variables

    # Handle events
    ts = True
    while ts:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            # Check for mouse click
        if pygame.mouse.get_pressed()[0]:
            # Get the mouse position
            mouse_pos = pygame.mouse.get_pos()

            # Check if the mouse is over a menu item
            for index, item_rect in enumerate(item_rects):
                if item_rect.collidepoint(mouse_pos):
                    print(index)
                    if index == 0:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                sys.exit()
                        m_run = True
                        while m_run:
                            # Perform action based on the menu item
                            card_values = ["A", "2", "3", "4", "5",
                                           "6", "7", "8", "9", "1", "J", "Q", "K"]
                            card_suits = ["D", "C", "H", "S"]
                            card_images = {}

                            for value in card_values:
                                for suit in card_suits:
                                    file_path = f"cards/{value}{suit}.jpg"
                                    card_images[f"{value}{suit}"] = pygame.image.load(
                                        file_path)

                            # Set card value dictionary
                            card_values = {
                                "A": 1,
                                "2": 2,
                                "3": 3,
                                "4": 4,
                                "5": 5,
                                "6": 6,
                                "7": 7,
                                "8": 8,
                                "9": 9,
                                "1": 10,
                                "J": 10,
                                "Q": 10,
                                "K": 10
                            }

                            deck = []
                            dealer_hand = []
                            dealer_next_game = False
                            player_hand = []
                            next_game = False
                            new_func(card_values, card_suits, deck)
                            deckMezclada = deck_mezclada(deck)
                            haveCardDealer(dealer_hand, hand)
                            haveCardPlayer(player_hand, hand)

                            print('Start clicked')
                            bg_img(width, height, screen)
                            running = True
                            while running:

                                # print(card_images)
                                draw_card(screen, card_images,
                                          dealer_hand, player_hand)
                                # Calculate player and dealer hand values
                                player_value = sum([card_values[card[0]]
                                                    for card in player_hand])
                                # print(player_value)
                                dealer_value = sum([card_values[card[0]]
                                                    for card in dealer_hand])
                                # print(dealer_value)
                                # Calculate player and dealer hand values

                                def take_card_dealer(player_value, dealer_value):
                                    player_value = sum([card_values[card[0]]
                                                        for card in player_hand])

                                    dealer_value = sum([card_values[card[0]]
                                                        for card in dealer_hand])

                                    while dealer_value < player_value:
                                        hand(dealer_hand)

                                        player_value = sum([card_values[card[0]]
                                                            for card in player_hand])

                                        dealer_value = sum([card_values[card[0]]
                                                            for card in dealer_hand])

                                        pass
                                    otra_partida = check_dealer_value(
                                        player_value, dealer_value)
                                    return otra_partida
                                exit_button = exitButton(screen)
                                if next_game == False and dealer_next_game == False:
                                    hit_button = hit_Buton(screen)
                                    stand_button = standButton(screen)

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        sys.exit()

                                # Check if the button is clicked
                                if pygame.mouse.get_pressed()[0]:
                                    if exit_button.collidepoint(pygame.mouse.get_pos()):
                                        sys.exit()

                                        # Check if the button is clicked
                                    elif hit_button.collidepoint(pygame.mouse.get_pos()) and next_game == False and dealer_next_game == False:
                                        # Add code to give player another card

                                        if player_value < 21:
                                            hand(player_hand)
                                            pygame.time.delay(200)
                                        else:
                                            pass
                                        print("Player hits.")
                                    elif stand_button.collidepoint(pygame.mouse.get_pos()) and next_game == False and dealer_next_game == False:
                                        print("Player Stand0.")
                                        dealer_next_game = take_card_dealer(
                                            player_value, dealer_value)

                                next_game = check_player_value(screen, font, card_images, dealer_hand,
                                                               player_hand, draw_card, player_value)
                                if next_game or dealer_next_game:
                                    play_again = playAgain(screen)
                                    if pygame.mouse.get_pressed()[0]:
                                        if play_again.collidepoint(pygame.mouse.get_pos()):
                                            running = False
                                back_m = backs(screen)
                                if pygame.mouse.get_pressed()[0]:
                                    if back_m.collidepoint(pygame.mouse.get_pos()):
                                        running = False
                                        m_run = False
                                        bg_img(width, height, screen)
                                        menu_optinos(
                                            screen, font, BLACK, menu_items, item_rects)

                                clock.tick(60)
                                pygame.display.update()
                    elif index == 1:
                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    sys.exit()
                            bg_img(width, height, screen)
                            back_m = backs(screen)
                            text(screen)
                            if pygame.mouse.get_pressed()[0]:
                                if back_m.collidepoint(pygame.mouse.get_pos()):
                                    running = False
                                    bg_img(width, height, screen)
                                    menu_optinos(
                                        screen, font, BLACK, menu_items, item_rects)

                            clock.tick(60)
                            pygame.display.update()

                    elif index == 2:
                        print('Options clicked2')
                        running = False
                        sys.exit()

            # Update the display
        pygame.display.update()
        # Main game loop


# Clean up Pygame
