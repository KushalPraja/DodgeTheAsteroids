import pygame
from button import Button
from config import load_font, SCREEN_LENGTH, SCREEN_HEIGHT

def draw_start_screen(screen):
    screen.fill((0, 0, 0))
    font = load_font(48)
    title_surface = font.render("Dodge the Asteroids!", True, (255, 255, 255))
    title_rect = title_surface.get_rect(center=(SCREEN_LENGTH//2, 150))
    screen.blit(title_surface, title_rect)

    button_font = load_font(20)
    start_button = Button(
        x=SCREEN_LENGTH//2 - 100,
        y=SCREEN_HEIGHT//2,
        width=200,
        height=80,
        onclickfunction=None,
        text="Start Game",
        font=button_font,
        bg_color=(0, 128, 0),
        text_color=(255, 255, 255)
    )

    start_button.draw(screen)
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if start_button.is_clicked(event):
                return