import pygame
from config import load_font, SCREEN_LENGTH, SCREEN_HEIGHT, FPS
from spaceship import Spaceship
from asteroid import Asteroid
from random import randint, uniform
import startscreen
import endscreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Dodge the Asteroids")

    running = True
    while running:
        startscreen.draw_start_screen(screen)
        action = main_game(screen, clock)
        if action == "quit":
            running = False

    pygame.quit()

def main_game(screen, clock):
    try:
        font = load_font()
    
    except Exception as e:
        print(f"Error loading font: {e}")
        pygame.quit()
        return "quit"

    all_sprites = pygame.sprite.Group()
    spaceship = Spaceship(all_sprites, pos_x=SCREEN_LENGTH // 2, pos_y=SCREEN_HEIGHT - 50)

    score = 0

    for _ in range(5):
        x_pos = randint(0, SCREEN_LENGTH)
        y_pos = 0
        speed = uniform(4.0, 6.0)
        size = randint(20,50)
        asteroid = Asteroid(all_sprites, pos_x=x_pos, pos_y=y_pos, speed=speed, size=size)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(topleft=(10, 10))

        for asteroid in all_sprites:
            if isinstance(asteroid, Asteroid):
                if spaceship.rect.colliderect(asteroid.rect):
                    all_sprites.remove(spaceship)
                    all_sprites.remove(asteroid)
                    action = endscreen.draw_end_screen(screen, score)
                    return action

        screen.fill("#010101")
        screen.blit(text_surface, text_rect)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    
    return "quit"

if __name__ == "__main__":
    main()