import pygame
from config import load_font
class Button:
    def __init__(self, x=0, y=0, width=100, height=40, onclickfunction=None, text="", font=None, bg_color=(100,100,100), text_color=(255,255,255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.onclickfunction = onclickfunction
        self.text = text
        self.font = font or load_font()
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover = False

    def draw(self, screen):
        color = self.bg_color
        if self.hover:
            color = tuple(min(255, c + 20) for c in color)
        pygame.draw.rect(screen, color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if callable(self.onclickfunction):
                    try:
                        self.onclickfunction()
                    except Exception:
                        pass
                return True
        return False

    def is_clicked(self, event):
        return self.handle_event(event)
