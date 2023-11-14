from pygame.display import flip

from fonts import CreateText


def _display(self):
    """Window Display Management"""
    # Renew previous frame with template background color
    self.screen.fill('#a15cbd')

    # Display FPS Meter
    self._fps_meter()

    # Update display.
    flip()

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

    # Render text object on screen.
    self.screen.blit(font.render, font.rect)
