from pygame import Color, Rect, mouse
from pygame.draw import rect as draw_rect


def _layer_i(self):
    """Code block of surface layer 1."""
    # Dot Cursor
    self._dot_cursor()

def _dot_cursor(self):
    """A green circle that mirrors the cursor's position."""
    rgb = Color(50, 168, 94)
    dimensions = Rect(10, 10, 10, 10)
    dimensions.center = mouse.get_pos()
    draw_rect(self.screen, rgb, dimensions, border_radius=5)
