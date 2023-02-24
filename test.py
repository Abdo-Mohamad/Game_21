import pygame
import imageio.v3 as iio

# Initialize pygame
pygame.init()

# Set up the window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
# Initializing RGB Color
def bg_img(width, height, screen):
    bg_img = pygame.image.load('cards/background.jpg')
    bg_img = pygame.transform.scale(bg_img, (width, height))
    screen.blit(bg_img, (0, 0))
 

# Load the GIF frames as a list of numpy arrays
gif_frames = iio.imread('5.gif')


def gif(screen, gif_frames):
    for frame in gif_frames:
        # Convert the numpy array to a Pygame surface
        surface = pygame.surfarray.make_surface(frame)

    # Set the color key to black
        surface.set_colorkey((0, 0, 0))

    # Scale the surface to fit the window
        surface = pygame.transform.scale(surface, (200, 200))

    # Display the surface on the screen
        screen.blit(surface, (0, 0))

    # Update the screen
        pygame.display.flip()
    # Wait for a short time before displaying the next frame
        pygame.time.wait(100)

gif(screen, gif_frames)
# Loop through the frames and display them on the screen



# Wait for the user to close the window
while True:
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Changing surface color
