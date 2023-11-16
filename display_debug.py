from pygame import Color
from pygame.draw import rect as draw_rect

from fonts import CreateText


def _debug_surface(self):
    """Process debug surface."""
    # Debug Surface
    surface = self.debug_surface

    # FPS Meter
    self._fps_meter(surface)

def _fps_meter(self, surface):
    """FPS Meter"""
    # Construct text contents.
    content = self.clock.get_fps()
    content = 'FPS: ' + str(int(content))

    # Create text object.
    font = CreateText(content, debug=True)

    # Position text rectangle.
    sr = self.root_surface_rect
    x, y = sr.right, sr.bottom
    font.rect.right = x-5
    font.rect.bottom = y-5

    # Construct rounded rectangle.
    rgb = Color(64, 64, 64, 102)  # 40% Opacity
    dimensions = font.rect.copy()
    dimensions.width += 4
    dimensions.height += 4
    dimensions.center = font.rect.center

    # Draw on `debug_screen` and update `screen`.
    draw_rect(surface, rgb, dimensions, border_radius=2)
    surface.blit(font.render, font.rect)
