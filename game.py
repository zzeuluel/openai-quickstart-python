#!/usr/bin/env python3
"""Runnable game script converted from notebook content."""
import os
import sys

# Try to load settings; fall back to defaults if not available
try:
    from settings import *  # type: ignore
except ModuleNotFoundError:
    sys.path.insert(0, r'c:\Users\faith_txgqlij')
    sys.path.insert(0, os.getcwd())
    try:
        from settings import *  # type: ignore
    except ModuleNotFoundError:
        WINDOW_WIDTH = 640
        WINDOW_HEIGHT = 480
        GAME_WIDTH = 300
        GAME_HEIGHT = 600
        COLUMNS = 10
        ROWS = 20
        CELL_SIZE = 30
        LIGHT_COLOR = (50, 50, 50)
        PADDING = 10

import pygame


class Game:
    def __init__(self):
        # Surface that holds the game area
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        # Ensure a display surface exists when we blit later; main() will call pygame.init()
        if pygame.display.get_surface() is None:
            pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.display_surface = pygame.display.get_surface()
        # lines
        self.lines_surface = self.surface.copy()

    def draw_grid(self):
        for col in range(COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.surface, LIGHT_COLOR, (x, 0), (x, self.surface.get_height()), 1)
        for row in range(ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.surface, LIGHT_COLOR, (0, y), (self.surface.get_width(), y), 1)
        # If lines_surface is intended for something else, this keeps it consistent
        self.surface.blit(self.lines_surface, (0, 0))

    def run(self):
        # drawing
        bg_color = globals().get('GRAY', (30, 30, 30))
        self.surface.fill(bg_color)
        self.draw_grid()
        # Blit the game surface onto the display surface with padding
        self.display_surface.blit(self.surface, (PADDING, PADDING))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Game Window")
    clock = pygame.time.Clock()
    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.run()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
