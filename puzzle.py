import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
GRID_SIZE = 3
TILE_SIZE = SCREEN_WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sliding Puzzle")

# Create the tiles
tiles = [i for i in range(GRID_SIZE ** 2)]

def shuffle_tiles():
    random.shuffle(tiles)

shuffle_tiles()

def draw_tiles():
    for i in range(len(tiles)):
        row = i // GRID_SIZE
        col = i % GRID_SIZE
        tile_number = tiles[i]
        pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        if tile_number > 0:
            font = pygame.font.Font(None, 36)
            text = font.render(str(tile_number), True, BLACK)
            text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
            screen.blit(text, text_rect)

def get_clicked_tile(x, y):
    col = x // TILE_SIZE
    row = y // TILE_SIZE
    return row * GRID_SIZE + col

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                clicked_tile = get_clicked_tile(*event.pos)
                if clicked_tile in range(GRID_SIZE ** 2):
                    blank_tile = tiles.index(0)
                    if clicked_tile // GRID_SIZE == blank_tile // GRID_SIZE or clicked_tile % GRID_SIZE == blank_tile % GRID_SIZE:
                        tiles[clicked_tile], tiles[blank_tile] = tiles[blank_tile], tiles[clicked_tile]

    # Check if the puzzle is solved


        # Reshuffle when solved
        if tiles == list(range(1, GRID_SIZE ** 2)) + [0]:
                shuffle_tiles()




    # Clear the screen
    screen.fill(BLACK)

    # Draw the tiles
    draw_tiles()

    pygame.display.update()