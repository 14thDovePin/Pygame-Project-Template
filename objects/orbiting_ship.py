from pygame.image import load as load_image
from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame import mouse  # TODO: Remove | TestingOnly

from utils.subdivide_sprite import subdivide_sprite


# Spritesheet DIR
SS_DIR = '.\\assets\\lf2_dennis_atk.bmp'


class OrbitingShip(Sprite):

    def __init__(self, *args, **kwargs):
        "A rotating triangle with the cursor as its center."
        super().__init__(*args, **kwargs)
        # Load image or create shape.
        sprite_sheet = load_image(SS_DIR)
        self.image = sprite_sheet
        self.sprites = subdivide_sprite(sprite_sheet, 81,82)

        # Create object rectangle.
        self.rect = sprite_sheet.get_rect()

        self._set_attributes()

    def _set_attributes(self):
        """Set the object's initial or spawn attributes."""
        # Create and set position & velocity vector.
        init_value = 0, 0
        self.pos = Vector2(init_value)
        self.vect = Vector2(init_value)

        # Set rectangle.
        self.rect.bottomright = self.rect.topleft

    def update(self):
        """Update object."""
        # Update position & rectangle.
        pos = mouse.get_pos()
        self.pos = Vector2(pos)
        self.rect.topleft = pos

    def blit(self, surface):
        """Blit object on surface."""
        # Blit on surface.
        surface.blit(self.sprites[9], self.rect)
