
from PIL import Image

import os

carpeta = "/Users/FELIPE/Downloads/comprimir/"

if __name__ == "__main__":
    for filename in os.listdir(carpeta):
        name, extension = os.path.splitext(carpeta + filename)

        if extension in [".jpg", ".JPG", ".jpeg", ".png"]:
            picture = Image.open(carpeta + filename)
            picture.save(carpeta + "compressed" + filename, optimize=True, quality=60)