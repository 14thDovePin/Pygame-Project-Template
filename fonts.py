import pygame

from pygame.font import SysFont


# Default Font
DFLT = 'verdana'
# Debugging Font
DBG = 'consolas'


class CreateText:

    def __init__(
            self,
            content: str,
            size: int=0,
            bold: bool=False,
            italic: bool=False,
            font: str=DFLT,
            color: str='#070707',  # 3% White | 97% Black
            format: str='normal',
            debug: bool=False,
            antialias: bool=True
            ):
        """Create a text object.

        Args
        ----
        `format` modifies `size` attr:
            'title' -> 30,
            'h1' -> 24,
            'h2' -> 18,
            'h3' -> 14,
            'normal' -> 12
        """
        self.content = content
        self.size = size
        self.bold = bold
        self.italic = italic
        self.font = font
        self.color = color
        self.format = format
        self.debug = debug
        self.antialias = antialias

        self._condition_attr()

        self.rect: pygame.Rect
        self.render = pygame.font.Font.render

        # Construct text object.
        self.construct()

    def _condition_attr(self):
        """Condition attributes based on parameters."""
        # Condition `size` with `format`.
        if self.size == 0:
            format = self.format.lower()
            if format == 'title':
                self.size = 30
            elif format == 'h1':
                self.size = 24
            elif format == 'h2':
                self.size = 18
            elif format == 'h3':
                self.size = 14
            elif format == 'normal':
                self.size = 12

        # Condition `font` with `debug`.
        if self.debug:
            self.font = DBG
            self.color = '#f8f8f8'  # 97% White

    def construct(self):
        """Construct the text object."""
        # Render Text
        font_obj = SysFont(
            self.font,
            self.size,
            self.bold,
            self.italic
            )
        self.render = font_obj.render(
            self.content,
            self.antialias,
            self.color
            )

        # Construct Rectangle
        self.rect = self.render.get_rect()
