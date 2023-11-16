from pygame import Surface, display

import pygame

from configuration import ParseConfig


""" TODO
- Add an inner life cycle for pausing and unpausing.
  + When the game is paused, add a translucent (75%) gray background.
- Add an sample object that rotates around the cursor.
"""


class MyGame:

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()

        # Setup and pull configurations.
        self.config = ParseConfig().data

        # Setup window resolution & display surfaces.
        width = self.config['screen_width']
        height = self.config['screen_height']
        resolution = width, height

        self.root_surface = display.set_mode(resolution)
        self.top_surface = Surface(resolution, pygame.SRCALPHA)
        self.debug_surface = Surface(resolution, pygame.SRCALPHA)

        # Create respective rectangles.
        self.root_surface_rect = self.root_surface.get_rect()
        self.top_surface_rect = self.root_surface_rect.copy()
        self.debug_screen_rect = self.root_surface_rect.copy()

        # Manage cycles.
        self.fps = self.config['fps']
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
    )

    from display_root import(
        _root_surface,
        _dot_cursor,
    )

    from display_top import(
        _top_surface,
    )

    from display_debug import(
        _debug_surface,
        _fps_meter,
    )

    def start(self, run: bool):
        """Start the program's life cycle."""
        self.running = run
        while self.running:

            # Manage events.
            self._events()

            # Manage display.
            self._display()

            # Control cycles per second.
            self.clock.tick(self.fps)

        pygame.quit()

    def set_caption(self, caption):
        """Set Window Caption"""
        display.set_caption(caption)


if __name__ == '__main__':
    game = MyGame()
    game.set_caption('Pygame Project Template')
    game.start(True)
