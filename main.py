import pygame
import funx

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the window
pygame.display.set_caption("My Game")

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("cima")

            if event.key == pygame.K_a:
                print("esquerda")

            if event.key == pygame.K_s:
                print("baixo")

            if event.key == pygame.K_d:
                print("direita")

    # Update game logic here

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw game objects here


    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()