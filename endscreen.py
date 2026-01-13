import pygame
from button import Button
from config import load_font
import game_state

def draw_end_screen(screen, score):
    clock = pygame.time.Clock()

    new_high_score = False
    if score > game_state.BEST_SCORE:
        game_state.BEST_SCORE = score
        new_high_score = True

    while True:
        screen.fill((0,0,0))

        font = load_font(64)
        title = font.render("Game Over", True, (255,255,255))
        title_rect = title.get_rect(center=(400, 50))
        screen.blit(title, title_rect)

        font = load_font(32)
        if new_high_score:
            new_high_surf = font.render("New High Score!", True, (255,215,0))
            new_high_rect = new_high_surf.get_rect(center=(400, 100))
            screen.blit(new_high_surf, new_high_rect)

        best_score_surf = font.render(f"Best Score: {game_state.BEST_SCORE}", True, (255,255,255))
        best_score_rect = best_score_surf.get_rect(center=(400, 150))
        screen.blit(best_score_surf, best_score_rect)

        score_surf = font.render(f"Score: {score}", True, (255,255,255))
        score_rect = score_surf.get_rect(center=(400, 200))
        screen.blit(score_surf, score_rect)

        restart_btn = Button(250, 300, 140, 60, text="Restart", font=font, bg_color=(0,128,0), text_color=(255,255,255))
        quit_btn = Button(410, 300, 140, 60, text="Quit", font=font, bg_color=(128,0,0), text_color=(255,255,255))

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