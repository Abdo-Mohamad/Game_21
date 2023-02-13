import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((400, 300))

# Set window title
pygame.display.set_caption("Pygame Menu")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define font
font = pygame.font.Font(None, 30)

# Define menu options
menu_items = ["Start", "Quit", "Test"]

# Draw menu
def draw_menu(menu, font, screen, item_height):
    for index, item in enumerate(menu):
        label = font.render(item, 1, white)
        width = label.get_rect().width
        height = label.get_rect().height
        posx = (screen.get_width() / 2) - (width / 2)
        posy = (screen.get_height() / 2) - (height / 2) + (index * item_height)
        screen.blit(label, (posx, posy))

# Main game loop
running = True
selected_item = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("clicked")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_item = max(0, selected_item - 1)
                print("clicked")
            if event.key == pygame.K_DOWN:
                selected_item = min(len(menu_items) - 1, selected_item + 1)
                print("clicked")
            if event.key == pygame.K_RETURN:
                if menu_items[selected_item] == "Quit":
                    running = False

    screen.fill(black)
    item_height = font.size("A")[1] + 10
    draw_menu(menu_items, font, screen, item_height)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
