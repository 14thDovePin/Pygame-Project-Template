from pygame import Color, Rect, mouse
from pygame.draw import rect as draw_rect


def _root_surface(self):
    """Process root surface."""
    # Root Surface
    surface = self.root_surface

    # Orbiting Ship
    self.orbiting_ship.blit(surface)

    # Dot Cursor
    self._dot_cursor(surface)

def _dot_cursor(self, surface):
    """A green circle that mirrors the cursor's position."""
    rgb = Color(50, 168, 94)
    dimensions = Rect(10, 10, 10, 10)
    dimensions.center = mouse.get_pos()
    draw_rect(surface, rgb, dimensions, border_radius=5)
