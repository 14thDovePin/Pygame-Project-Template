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

        # Load image/s or create shape.
        sprite_sheet = load_image(SS_DIR)
        self.sprites = subdivide_sprite(sprite_sheet, 81,82)

        # Create object rectangle.
        self.rect = sprite_sheet.get_rect()

        # Animation index.
        self.animation_speed = 10  # Frames per frame.
        self.creation_index = [0, 8, 1, 9]
        self.motion_index = [2, 10, 3, 11]
        self.destroy_index = [4, 5, 6, 7]

        self._set_attributes()

    def _set_attributes(self):
        """Set the object's initial or spawn attributes."""
        # Create and set position & velocity vector.
        init_value = 0, 0
        self.pos = Vector2(init_value)
        self.vect = Vector2(init_value)

        # Set rectangle.
        self.rect.bottomright = self.rect.topleft

        # Set index and image.
        self.current_index = 0
        self.image = self.sprites[0]

    def update(self, current_frame):
        """Update object."""
        # Update position & rectangle.
        pos = mouse.get_pos()
        self.pos = Vector2(pos)
        self.rect.topleft = pos

        # Update animation index.
        if current_frame % self.animation_speed == 0:
            self._next_frame(self.motion_index)

    def _next_frame(self, animation_index):
        """Update sprite with the next frame."""
        # Update current index.
        if self.current_index < len(animation_index)-1:
            self.current_index += 1
        else:
            self.current_index = 0

        # Update sprite.
        idx = animation_index[self.current_index]
        img = self.sprites[idx]
        self.image = img

    def blit(self, surface):
        """Blit object on surface."""
        # Blit on surface.
        surface.blit(self.image, self.rect)
