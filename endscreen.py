import pygame
from button import Button
from config import load_font

def draw_end_screen(screen, score):
    clock = pygame.time.Clock()
    font = load_font()
    small = load_font()

    while True:
        screen.fill((0,0,0))
        title = font.render("Game Over", True, (255,255,255))
        title_rect = title.get_rect(center=(400, 120))
        screen.blit(title, title_rect)

        score_surf = small.render(f"Score: {score}", True, (255,255,255))
        score_rect = score_surf.get_rect(center=(400, 200))
        screen.blit(score_surf, score_rect)

        restart_btn = Button(250, 300, 140, 60, text="Restart", font=small, bg_color=(0,128,0), text_color=(255,255,255))
        quit_btn = Button(410, 300, 140, 60, text="Quit", font=small, bg_color=(128,0,0), text_color=(255,255,255))

        restart_btn.draw(screen)
        quit_btn.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if restart_btn.is_clicked(event):
                return "restart"
            if quit_btn.is_clicked(event):
                return "quit"

        clock.tick(30)
# ...new file...