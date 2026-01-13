import pygame
import assets
import config

class Spaceship(pygame.sprite.Sprite):
    
    def __init__(self, *groups, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self, *groups)
        pygame.sprite.Sprite.add(self, *groups)
        self.image = assets.get_asset("spaceship")
        self.width = 50
        self.height = 38
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.pos = pygame.math.Vector2()
        self.pos.x = pos_x
        self.pos.y = pos_y
        self.velocity = 0 # start at 1 pix
        self.acceleration = 0.1 # pix per frame^2
        self.direction = 0 # -1 for left, 1 for right, 0 for no movement
        self.terminal_velocity = 4  # max speed

    def calculate_new_position(self, current_position, direction):
        self.velocity = min(self.velocity + self.acceleration, self.terminal_velocity)
        if direction == "left":
            new_position = current_position - self.velocity
        elif direction == "right":
            new_position = current_position + self.velocity
        else:
            new_position = current_position
        return new_position

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.direction != -1:
                self.velocity = 0  # reset velocity when changing direction
                self.acceleration = 0.1  # reset acceleration when changing direction
            self.direction = -1
        elif keys[pygame.K_RIGHT]:
            if self.direction != 1:
                self.velocity = 0  # reset velocity when changing direction
                self.acceleration = 0.1  # reset acceleration when changing direction

            self.direction = 1
        
        if self.direction != 0:
            if self.direction == -1:
                new_x = self.calculate_new_position(self.pos.x, "left") 
            else:
                new_x = self.calculate_new_position(self.pos.x, "right")
            self.rect.x = new_x
        else:
            self.velocity = 0  # reset velocity when no key is pressed
            self.acceleration = 0.1  # reset acceleration when no key is pressed

        #clamp within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > config.SCREEN_LENGTH:
            self.rect.right = config.SCREEN_LENGTH

        self.pos.x = self.rect.x
        self.pos.y = self.rect.y
# 
        # print current velocity and position for debugging
        # print(f"Velocity: {self.velocity}, Position X: {self.pos.x}")




        




        

  