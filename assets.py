import os
import pygame.image

def get_asset(filename):
    path = os.path.join("assets", filename + ".png")
    sprite =  pygame.image.load(path)
    if not sprite:
        raise FileNotFoundError(f"Asset not found: {path}")
    return sprite

