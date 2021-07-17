from typing import Optional

from PIL import Image


def get_ascii(image_path: str, size: Optional[tuple] = None) -> str:
    """Converts the image at the given path to ascii art (str)

    Parameters
    ----------
    image_path: str
        path of the image user is trying to convert to ascii.
    size: Optional[tuple]
        size the user will like to convert the given image to.
    """
    image = Image.open(image_path)
    image = image.convert("L")

    if size:
        image = image.resize((size[0], size[1]))

    shades = list("@#$%?*+;:,.")
    ascii_art = []

    div = 255 // (len(shades)-1)

    for y in range(image.height):
        row = []
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            shade = shades[pixel//div]
            row.append(shade)
        ascii_art.append("".join(row))

    return "\n".join(ascii_art)
