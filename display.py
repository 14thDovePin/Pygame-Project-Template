from pygame.display import flip


def _display(self):
    """Root surface of the program."""
    # Renew frame with color.
    self.screen.fill('#a15cbd')

    # Process & blit layer 1.
    self._layer_i()

    # Process & blit debug screen.
    self._pds()

    # Update display.
    flip()
