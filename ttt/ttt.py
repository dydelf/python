"""
Main file of the tic tac toe game.
"""

import sys

import pygame


def run_game():
    """ Initialize a game and create a screen. """
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic Tac Toe")
    # Set background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.draw.line(screen, (0, 0, 100), (20, 300), (100, 300), 10)

        # Redraw the screen during each pass of the loop
        screen.fill(bg_color)

        # Make the most recent screen visible
        pygame.display.flip()

run_game()
