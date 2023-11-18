""" README

This file serves as a guide reference for constructing game objects using Python within this repository. Please note that anything contained in this file, as well as the file itself, is not intended for use in the actual game.
"""


class ObjectTemplate:

    def __init__(self):
        """A class template for game objects."""
        # Load image or create shape.
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
        # Update rectangle.

    def blit(self, surface):
        """Blit object on surface."""
        # Blit on surface.

    def reset(self):
        """Reset object's attributes & propeties."""
        self._set_attributes()
        # Call other methods or functions.
