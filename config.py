import pygame

SCREEN_LENGTH = 800
SCREEN_HEIGHT = 600
FPS = 60

FONT_PATH = "fonts/Comfortaa-Medium.ttf"


def load_font():
    try:
        font = pygame.font.Font(FONT_PATH, 24)
        return font
    except Exception as e:
        print(f"Error loading font: {e}")
        return pygame.font.Font(None, 24)