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
# Create a font for displaying text
font = pygame.font.Font(None, 36)
# Create the exit button


def exitButton(screen):
    exit_button = pygame.Rect(700, 550, 80, 50)
    # Set the font for the button text
    font = pygame.font.Font(None, 30)
    # Set the text for the button
    exit_text = font.render("Exit", True, (255, 255, 255))
    # Draw the button on the screen
    pygame.draw.rect(screen, (0, 0, 255), exit_button)
    screen.blit(exit_text, (725, 570))
    return exit_button

# Create the stand button


def standButton(screen):
    stand_button = pygame.Rect(1290, 785, 80, 50)
    # Set the font for the button text
    font = pygame.font.Font(None, 30)
    # Set the text for the button
    stand_text = font.render("Stand", True, (255, 255, 255))
    # Draw the button on the screen
    pygame.draw.rect(screen, (0, 0, 255), stand_button)
    screen.blit(stand_text, (1300, 800))
    return stand_button


def playAgain(screen):
    play_again = pygame.Rect(400, 650, 100, 50)
    # Set the font for the button text
    font = pygame.font.Font(None, 30)
    # Set the text for the button
    play_again_text = font.render("play Again", True, (255, 255, 255))
    # Draw the button on the screen
    pygame.draw.rect(screen, (0, 0, 255), play_again)
    screen.blit(play_again_text, (400, 650))
    return play_again
# def hit_button(screen):
#     hit_button = pygame.Rect(600, 500, 100, 50)
#     # Set the font for the button text
#     font = pygame.font.Font(None, 30)
#     # Set the text for the button
#     hit_text = font.render("Hit", True, (255, 255, 255))
#     # Draw the button on the screen
#     pygame.draw.rect(screen, (0, 0, 255), hit_button)
#     screen.blit(hit_text, (630, 520))

# Create the hit button


def hit_Buton(screen):
    hit_button = pygame.Rect(50, 550, 80, 50)
    # Set the font for the button text
    font = pygame.font.Font(None, 30)
    # Set the text for the button
    hit_text = font.render("Hit", True, (255, 255, 255))
    # Draw the button on the screen
    pygame.draw.rect(screen, (0, 0, 0), hit_button)
    screen.blit(hit_text, (75, 570))
    return hit_button


def bg_img(width, height, screen):
    bg_img = pygame.image.load('background.jpg')
    bg_img = pygame.transform.scale(bg_img, (width, height))
    screen.blit(bg_img, (0, 0))

# Load card images
# test = []


def new_func(card_values, card_suits, deck):
    for value in card_values:
        for suit in card_suits:
            card = value + suit
            print(card)
            deck.append(card)
            print(deck)

# for i in deck:
#     bg_imgs = pygame.image.load(f'img/AC.jpg')
#     # Clear the screen
#     screen.blit(bg_imgs, (400, 100))
#     pygame.display.flip()
#     pygame.time.delay(400)
#     t = card_values.get(i[0])
#     print(i[0], "j", t)


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
            back = pygame.image.load('back2.jpg')
            back = pygame.transform.scale(
                back, (image_size_w, image_size_h))
            screen.blit(back, (y+200, 50))

        else:
            print(y, "dhfsgjk")
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

# suma_player_hand = []

# def suma_card(card_values, player_hand, suma_player_hand):
#     for i in deckMezclada:
#         print(i[0], "The zero num")
#         num_values = i[0]
#         print(num_values)
#         get_card = card_values.get(num_values)
#         print(get_card)
#         pygame.time.wait(100)
#         if get_card != None:
#             suma_player_hand.append(get_card)
#         print(suma_player_hand)
#         # suma = sum(suma_player_hand)
#         # print(suma)
#         # print(deckMezclada)

# # myNumber = "11"
# # myArray = np.array(suma_player_hand)
# # pos = (np.abs(myArray-myNumber)).argmin()
# # r=myArray[pos]
# # print(r,"sdds")

# suma_card(card_values, player_hand, suma_player_hand)


def check_player_value(screen, font, card_images, dealer_hand, player_hand, draw_card, player_value):
    if player_value == 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        player_message = font.render(
            "Player wins with 21 (Blackjack)!", True, (20, 255, 255))
        screen.blit(player_message, (200, 300))
        pygame.display.flip()
        return True
        # pygame.time.wait(4000)
        # play_again = playAgain(screen)
        # if play_again.collidepoint(pygame.mouse.get_pos()):
        #     main()
        # pygame.time.wait(4000)
        # sys.exit()

    elif player_value > 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        player_bust_message = font.render(
            "Player busts!", True, (255, 55, 255))
        screen.blit(player_bust_message, (200, 300))
        pygame.display.flip()
        return True
        # play_again = playAgain(screen)
        # if play_again.collidepoint(pygame.mouse.get_pos()):
        #     main()
        # sys.exit()
    else:
        return False


def check_dealer_value(player_value, dealer_value):
    if dealer_value == 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        dealer_message = font.render(
            "Dealer wins with 21 (Blackjack)!", True, (25, 255, 255))
        screen.blit(dealer_message, (200, 300))
        pygame.display.flip()
        return True
        # play_again = playAgain(screen)
        # if play_again.collidepoint(pygame.mouse.get_pos()):
        #     main()
        # pygame.time.wait(4000)
        # sys.exit()

        # Check for bust
    elif dealer_value > 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        dealer_bust_message = font.render(
            "Dealer busts!", True, (255, 255, 55))
        screen.blit(dealer_bust_message, (200, 300))
        pygame.display.flip()
        return True
        # pygame.time.wait(4000)
        # play_again = playAgain(screen)
        # if play_again.collidepoint(pygame.mouse.get_pos()):
        #     main()
        # pygame.time.wait(4000)
        # sys.exit()

    elif dealer_value >= player_value < 21:
        draw_card(screen, card_images, dealer_hand, player_hand)
        dealer_bust_message = font.render(
            "Dealer Win!", True, (255, 255, 55))
        screen.blit(dealer_bust_message, (200, 300))
        pygame.display.flip()
        return True
        # pygame.time.wait(4000)
        # play_again = playAgain(screen)
        # if play_again.collidepoint(pygame.mouse.get_pos()):
        #     main()
        # pygame.time.wait(4000)
        # sys.exit()
    else:
        return False


# Draw player and dealer hands
while True:
    # Inicialización de variables
    card_values = ["A", "2", "3", "4", "5",
                   "6", "7", "8", "9", "1", "J", "Q", "K"]
    card_suits = ["D", "C", "H", "S"]
    card_images = {}

    for value in card_values:
        for suit in card_suits:
            file_path = f"cart_img/{value}{suit}.jpg"
            card_images[f"{value}{suit}"] = pygame.image.load(file_path)

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

    clock = pygame.time.Clock()
    deck = []
    dealer_hand = []
    dealer_value = 0
    dealer_next_game = False
    player_hand = []
    player_value = 0
    next_game = False
    new_func(card_values, card_suits, deck)
    deckMezclada = deck_mezclada(deck)
    haveCardDealer(dealer_hand, hand)
    haveCardPlayer(player_hand, hand)
    # Main game loop
    running = True
    bg_img(width, height, screen)
    while running:
        # suma_card(card_values, player_hand, suma_player_hand)
        # print THE card images

        # print(card_images)
        draw_card(screen, card_images, dealer_hand, player_hand)
        # Calculate player and dealer hand values
        player_value = sum([card_values[card[0]] for card in player_hand])
        # print(player_value)
        dealer_value = sum([card_values[card[0]] for card in dealer_hand])
        # print(dealer_value)
        # Calculate player and dealer hand values

        def take_card_dealer(player_value, dealer_value):
            player_value = sum([card_values[card[0]]
                               for card in player_hand])
            print(player_value)
            dealer_value = sum([card_values[card[0]]
                               for card in dealer_hand])
            print(dealer_value)
            print(deck, 'teteteejhdasf')
            while dealer_value < player_value:
                hand(dealer_hand)
                print(dealer_hand)
                player_value = sum([card_values[card[0]]
                                    for card in player_hand])
                print(player_value)
                dealer_value = sum([card_values[card[0]]
                                    for card in dealer_hand])
                print(dealer_value)
                pass
            otra_partida = check_dealer_value(player_value, dealer_value)
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
                # suma_player_hand = []
                # suma_card(card_values, player_hand, suma_player_hand)
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
                    # main()
            # pygame.time.wait(4000)
            # sys.exit()
        # numbers = [player_value]
        # closest_number = min(numbers, key=lambda x: abs(x - 21))
        # print(closest_number, "the number")

        # Check if the button is clicked

        # print(closest_number, "the closet number")

        #     if dealer_value == 21:
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         dealer_message = font.render(
        #             "Dealer wins with 21 (Blackjack)!", True, (55, 255, 255))
        #         screen.blit(dealer_message, (200, 300))
        #         pygame.display.flip()
        #         pygame.time.wait(4000)
        #         running = False

        #         # Check for bust
        #     elif dealer_value > 21:
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         dealer_bust_message = font.render(
        #             "Dealer busts!", True, (255, 255, 55))
        #         screen.blit(dealer_bust_message, (200, 300))
        #         pygame.display.flip()
        #         pygame.time.wait(4000)
        #         running = False
        #         # Check for 21 (Blackjack)
        #     elif dealer_value > player_value and dealer_value < 21:
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         dealer_message = font.render(
        #             "Dealer wins ", True, (55, 255, 255))
        #         screen.blit(dealer_message, (200, 300))
        #         pygame.display.flip()
        #         pygame.time.wait(4000)
        #         running = False

        #     else:
        #         print("dkjsf")
        # else:
        #     if dealer_value == 21:
        #         print("Player Stand2.")
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         dealer_message = font.render(
        #             "Dealer wins with 21 (Blackjack)!", True, (55, 255, 255))
        #         screen.blit(dealer_message, (200, 300))
        #         pygame.display.flip()
        #         pygame.time.wait(4000)
        #         running = False

        #         # Check for bust
        #     elif dealer_value > 21:
        #         print("Player Stand3.")
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         dealer_bust_message = font.render(
        #             "Dealer busts!", True, (255, 255, 55))
        #         screen.blit(dealer_bust_message, (200, 300))
        #         pygame.display.flip()
        #         pygame.time.wait(4000)
        #         running = False

        #         # Check for 21 (Blackjack)
        #     elif dealer_value > player_value and dealer_value < 21:
        #         print("Player Stand4.")
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         dealer_message = font.render(
        #             "Dealer wins ", True, (55, 255, 255))
        #         screen.blit(dealer_message, (200, 300))
        #         pygame.display.flip()
        #         pygame.time.wait(3000)
        #         running = False
        #     else:
        #         hand(dealer_hand)
        #         draw_card(screen, card_images, dealer_hand, player_hand)
        #         print("CASO X")
        # Check for 21 (Blackjack)

        # # Check for 21 (Blackjack)
        # if player_value == 21:
        #     print("Player wins with 21 (Blackjack)!")
        #     time.sleep(0.2)
        #     running = False
        # elif dealer_value == 21:
        #     print("Dealer wins with 21 (Blackjack)!")
        #     running = False

        #  # Check for bust
        # if player_value > 21:
        #     print("Player busts!")
        #     time.sleep(2)
        #     running = False
        # elif dealer_value > 21:
        #     print("Dealer busts!")
        #     time.sleep(2)
        #     running = False

        # Update the screen
        # pygame.display.flip()
        clock.tick(60)
        pygame.display.update()


# Clean up Pygame
pygame.quit()