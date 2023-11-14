import pygame

from configuration import ParseConfig


""" TODO
- Add an inner life cycle for pausing and unpausing.
  + When the game is paused, add a translucent (75%) gray background.
- Add an sample object that rotates around the cursor.
- Segregate the blit of `debug_screen` of `MyGame` into its own
  helper method.
"""


class MyGame:

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()

        # Setup and pull configuration.
        self.config = ParseConfig().data

        # Hide Cursor
        pygame.mouse.set_visible(False)

        # Setup Pygame
        resolution = \
            self.config['screen_width'], self.config['screen_height']

        # Surfaces
        self.screen = pygame.display.set_mode(resolution)
        self.screen_rect = self.screen.get_rect()
        self.debug_screen = \
            pygame.Surface(resolution, pygame.SRCALPHA)

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
        _dot_cursor,
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
