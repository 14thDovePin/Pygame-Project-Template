from pygame.image import load as load_image
from pygame.sprite import Sprite


# Spritesheet DIR
SS_DIR = '.\\assets\\lf2_dennis_atk.bmp'


class OrbitingShip(Sprite):

    def __init__(self, *args, **kwargs):
        "A rotating triangle with the cursor as its center."
        super().__init__(*args, **kwargs)

        # Load image or create shape.
        sprite_sheet = load_image(SS_DIR)

        # Create object rectangle.
        # Create position vector.
        # Create velocity vector.

    def _set_attributes(self):
        """Set the object's initial or spawn attributes."""
        # Set starting position.
        # Set starting velocity.

    def update_object(self):
        """Update object."""
        # Update position.
        # Update vector.

    def blit(self, surface):
        """Blit object on surface."""
        # Blit on surface.
