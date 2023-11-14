from pygame import Color, Rect, mouse
from pygame.display import flip
from pygame.draw import rect

from fonts import CreateText


def _display(self):
    """Window Display Management"""
    # Renew previous frame with template background color
    self.screen.fill('#a15cbd')

    self._dot_cursor()

    # Display FPS Meter
    self._fps_meter()

    # Update display.
    flip()

def _dot_cursor(self):
    """A green colored circle that follows the cursor."""
    rgb = Color(50, 168, 94)
    dimensions = Rect(10, 10, 10, 10)
    dimensions.center = mouse.get_pos()
    rect(self.screen, rgb, dimensions, border_radius=5)

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

    # Draw background rectangle.
    rgb = Color(64, 64, 64, 102)  # 40% Opacity
    dimensions = font.rect.copy()
    dimensions.width += 4
    dimensions.height += 4
    dimensions.center = font.rect.center
    rect(self.debug_screen, rgb, dimensions, border_radius=2)

    # Render background and text object on screen.
    self.screen.blit(self.debug_screen, (0, 0))
    self.screen.blit(font.render, font.rect)
