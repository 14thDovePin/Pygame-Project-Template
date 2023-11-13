import pygame

from configuration import ParseConfig


""" TODO
- Add an FPS display in game.
- Add an inner life cycle for pausing and unpausing.
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
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()

    """Import Class Methods"""

    from events import (
        _events,
        _window,
        _pressed_keys,
        _key_down,
    )

    from display import (
        _display,
        _fps_meter,
    )

    def start(self, run: bool):
        """Start the program's life cycle."""
        self.running = run
        while self.running:

            # Respond to events.
            self._events()

            # Manage and update display.
            self._display()

            # Limit FPS
            fps = self.config['fps']
            self.clock.tick(fps)

        pygame.quit()

    def set_caption(self, caption):
        """Set Window Caption"""
        pygame.display.set_caption(caption)


if __name__ == '__main__':
    game = MyGame()
    game.set_caption('Pygame Project Template')
    game.start(True)
