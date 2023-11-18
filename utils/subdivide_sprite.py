from pygame import Rect


def subdivide_sprite(sprite_sheet, width, height, border=1):
    """Return a list of divided sprites.

    Attributes
    ----------
    sprite_sheet : pygame.Surface
        Sprite Sheet
    width : int (px)
        Sprite Sheet Width
    height : int (px)
        Sprite Sheet Height
    border : int (px)
        Border Between Sprites

    Notes
    -----
    Divides sprite sheet from left-right and top-bottom.
    """
    sprites = []
    ss_rect = sprite_sheet.get_rect()

    # Set cell values.
    print(width, border)
    print(height, border)
    cwidth = width+border
    cheight = height+border

    # Check spritesheet divisibility.
    x_div = ss_rect.width % cwidth
    y_div = ss_rect.height % cheight

    if x_div != 0 or y_div != 0:
        error_message = 'SpriteSheetDivisionError\n\t'
        error_message += 'Sprite sheet division result irrational.'
        raise ValueError(error_message)

    # Loop & store sprites.
    for y in range(0, ss_rect.height, cheight):
        for x in range(0, ss_rect.width, cwidth):
            sprite_rect = Rect(x, y, width, height)
            sprite = sprite_sheet.subsurface(sprite_rect)
            sprites.append(sprite)

    return sprites
