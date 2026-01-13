import pygame
from config import load_font
def draw_cooldown_bar(screen, x, y, width, cooldown_text, height, cooldown, max_cooldown):
    if max_cooldown == 0:
        cooldown_ratio = 1
    else:
        cooldown_ratio = max(0, min(1, 1 - cooldown / max_cooldown))
    
    filled_width = int(width * cooldown_ratio)

    # Draw the cooldown bar background and filled portion
    pygame.draw.rect(screen, "#ffffff", (x, y, width, height))

    # Draw the filled portion
    pygame.draw.rect(screen, "#00ff00", (x, y, filled_width, height))

    # Draw the border and text
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height), 2)
    font = load_font(20)
    text_surface = font.render(cooldown_text, True, (255, 255,255))

    text_rect = text_surface.get_rect(center=(x + width // 2, y - 10))
    screen.blit(text_surface, text_rect)
    


