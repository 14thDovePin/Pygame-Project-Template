from pygame import Color
from pygame.draw import rect as draw_rect

from fonts import CreateText


def _pds(self):
    """Code block of the debug screen's surface."""
    # FPS Meter
    self._fps_meter()

def _fps_meter(self):
    """FPS Meter"""
    # Construct text contents.
    content = self.clock.get_fps()
    content = 'FPS: ' + str(int(content))

    # Create text object.
    font = CreateText(content, debug=True)

    # Position text rectangle.
    sr = self.screen_rect
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
    draw_rect(self.debug_screen, rgb, dimensions, border_radius=2)
    self.debug_screen.blit(font.render, font.rect)
    self.screen.blit(self.debug_screen, (0, 0))
