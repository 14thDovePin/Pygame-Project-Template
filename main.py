import pygame


FPS = 60  # Frames per Second
SR = (1280, 720)  # Screen Resolution


""" TODO
Add FPS display in game.
Dissect the following into its own files.
    Main Loop `life_cycle.py`
    Event Handling `events.py`
    Display `display.py`
"""


def main(ML=True):
    pygame.init()

    # Setup Pygame
    screen = pygame.display.set_mode(SR)
    clock = pygame.time.Clock()

    # Pygame's Main Loop
    while ML:  

        # Check for Events
        for event in pygame.event.get():

            # Clicked the X or Exit button.
            if event.type == pygame.QUIT:
                ML = False

            # Keydown Events
            elif event.type == pygame.KEYDOWN:

                # `Alt`+`F4`
                if \
                    event.key == pygame.KMOD_ALT and \
                    event.key == pygame.K_F4:
                    ML = False

        clock.tick(FPS)  # Limit FPS

    pygame.quit()


if __name__ == '__main__':
    main()
