from pygame.display import flip


def _display(self):
    """Display Manager"""
    # Color-fill root surface.
    self.root_surface.fill('#a15cbd')

    # Process root surface.
    self._root_surface()

    # Process top surface.
    self._top_surface()

    # Process debug surface.
    self._debug_surface()

    # Update surfaces & display.
    tl = (0, 0)  # Top-left
    self.root_surface.blit(self.top_surface, tl)
    self.root_surface.blit(self.debug_surface, tl)

    flip()
