import pygame

# Initialize the Pygame library
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((400, 300))

# Define the number of rows and columns in the grid
rows = 10
columns = 10

# Calculate the width and height of each cell
cell_width = screen.get_width() // columns
cell_height = screen.get_height() // rows

# Define the color of the grid cells
cell_color = (255, 255, 255)

# Initialize the clock to control the refresh rate of the screen
clock = pygame.time.Clock()

# Start the main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid
    for row in range(rows):
        for col in range(columns):
            cell = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, cell_color, cell, 1)

    # Update the screen
    pygame.display.update()

    # Control the refresh rate of the screen
    clock.tick(60)

# Quit Pygame
pygame.quit()
