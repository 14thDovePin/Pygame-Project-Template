import pygame


def _events(self):
    """Pygame Events"""
    # Loop through events.
    for event in pygame.event.get():

        # Window Events
        self._window(event)

        # Pressed Keys Events
        self._pressed_keys(event)

        # Keydown Events
        if event.type == pygame.KEYDOWN:
            self._key_down(event)

def _window(self, event):
    """Window Events"""
    # Window Exit Button = Exit Program
    if event.type == pygame.QUIT:
        self.running = False

def _pressed_keys(self, event):
    """Pressed Keys Events"""
    keys = pygame.key.get_pressed()

    # if keys[pygame.K_w]: print('up')
    # if keys[pygame.K_s]: print('down')
    # if keys[pygame.K_a]: print('left')
    # if keys[pygame.K_d]: print('right')

def _key_down(self, event):
    """Keydown Events"""
    # `Alt`+`F4` = Exit Program
    if \
        event.key == pygame.KMOD_ALT and \
        event.key == pygame.K_F4:
        self.running = False
