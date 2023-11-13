import pygame

from configuration import ParseConfig


""" TODO
- Add an FPS display in game.
"""


class MyGame:

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()

        # Setup and pull configuration.
        self.config = ParseConfig().data

        # Setup Pygame
        resolution = \
            self.config['screen_width'], self.config['screen_height']

        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()

    from events import (
        _events,
        _key_down,
        _window,
    )

    def start(self, run: bool):
        """Start the program's life cycle."""
        self.running = run
        while self.running:

            # Respond to events.
            self._events()

            # Limit FPS
            fps = self.config['fps']
            self.clock.tick(fps)

        pygame.quit()


if __name__ == '__main__':
    game = MyGame()
    game.start(True)
