import pygame


def _events(self):
    """Pygame Events"""
    # Loop through events.
    for event in pygame.event.get():

        # Window Events
        self._window(event)

        # Keydown Events
        if event.type == pygame.KEYDOWN:
            self._key_down(event)

def _window(self, event):
    """Window Events"""
    if event.type == pygame.QUIT:
        self.running = False

def _key_down(self, event):
    """Keydown Events"""
    # `Alt`+`F4` = Exit Program
    if \
        event.key == pygame.KMOD_ALT and \
        event.key == pygame.K_F4:
        self.running = False
