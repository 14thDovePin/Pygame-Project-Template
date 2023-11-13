from pygame.display import flip

import pygame


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
    # Construct Text Content
    fps = self.clock.get_fps()
    fps = 'FPS: ' + str(int(fps))

    # Construct Rendered Text
    fps_meter_font = pygame.font.SysFont('verdana', 12)
    fps_meter = fps_meter_font.render(fps, True, '#FFFFFF')

    # Position Rect
    sr = self.screen_rect
    x, y = sr.right, sr.bottom
    fps_meter_rect = fps_meter.get_rect()
    fps_meter_rect.right = x-5
    fps_meter_rect.bottom = y-5

    # Blit Text
    self.screen.blit(fps_meter, fps_meter_rect)
