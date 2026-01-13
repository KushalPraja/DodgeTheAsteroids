import pygame
from button import Button
from config import load_font, SCREEN_LENGTH, SCREEN_HEIGHT
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
        title_rect = title.get_rect(center=(SCREEN_LENGTH//2, SCREEN_HEIGHT//2 - 200))
        screen.blit(title, title_rect)

        font = load_font(32)
        small_font = load_font(24)
        
        if new_high_score:
            new_high_surf = font.render("New High Score!", True, (255,215,0))
            new_high_rect = new_high_surf.get_rect(center=(SCREEN_LENGTH//2, SCREEN_HEIGHT//2 - 100))
            screen.blit(new_high_surf, new_high_rect)

        best_score_surf = small_font.render(f"Best Score: {game_state.BEST_SCORE}", True, (255,255,255))
        best_score_rect = best_score_surf.get_rect(center=(SCREEN_LENGTH//2, SCREEN_HEIGHT//2))
        screen.blit(best_score_surf, best_score_rect)

        score_surf = small_font.render(f"Score: {score}", True, (255,255,255))
        score_rect = score_surf.get_rect(center=(SCREEN_LENGTH//2, SCREEN_HEIGHT//2 - 50))
        screen.blit(score_surf, score_rect)

        restart_btn = Button(SCREEN_LENGTH//2 - 150, SCREEN_HEIGHT//2 + 100, 140, 60, text="Restart", font=small_font, bg_color=(0,128,0), text_color=(255,255,255))
        quit_btn = Button(SCREEN_LENGTH//2 + 10, SCREEN_HEIGHT//2 + 100, 140, 60, text="Quit", font=small_font, bg_color=(128,0,0), text_color=(255,255,255))
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