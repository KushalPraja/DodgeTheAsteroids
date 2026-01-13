import pygame
import assets
import config
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, all_sprites, pos_x, pos_y, speed, size):
        pygame.sprite.Sprite.__init__(self, all_sprites)
        self.image = assets.get_asset("asteroid")
        self.width, self.height = size, size
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
        self.acceleration = 0.05

    def update(self, *args):
        self.rect.y += self.speed 
        self.speed += self.acceleration
        
        if self.rect.y > config.SCREEN_HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, config.SCREEN_LENGTH)
            self.speed = random.uniform(4.0, 6.0)
            self.size = random.randint(20, 50)
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        
        if self.rect.left > config.SCREEN_LENGTH or self.rect.right < 0:
            self.rect.y = 0
            self.rect.x = random.randint(0, config.SCREEN_LENGTH)
            self.speed = random.uniform(4.0, 6.0)  
            self.size = random.randint(20, 50)
            self.image = pygame.transform.scale(self.image, (self.size, self.size))
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

