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
        self.dash_cooldown = 0  # frames until next dash allowed
        # dash state for smooth dash (moves over several frames)
        self.is_dashing = False
        self.dash_frames_total = 12
        self.dash_frames_remaining = 0
        self.dash_distance = 100
        self.dash_speed_per_frame = 0
        self.dash_direction = 0

    def calculate_new_position(self, current_position, direction):
        self.velocity = min(self.velocity + self.acceleration, self.terminal_velocity)
        if direction == "left":
            new_position = current_position - self.velocity
        elif direction == "right":
            new_position = current_position + self.velocity
        else:
            new_position = current_position
        return new_position

    def get_cooldown(self):
        return self.dash_cooldown

    def update(self, *args):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] < self.rect.centerx:
            if self.direction != -1:
                self.velocity = 0.5  # reset velocity when changing direction
                self.acceleration = 0.1  # reset acceleration when changing direction
            self.direction = -1


        elif mouse_pos[0] > self.rect.centerx:
            if self.direction != 1:
                self.velocity = 0.5  # reset velocity when changing direction
                self.acceleration = 0.1  # reset acceleration when changing direction
            self.direction = 1

        else:
            self.direction = 0
        
        if keys[pygame.K_SPACE] and self.dash_cooldown == 0 and self.direction != 0:
            self.is_dashing = True
            self.dash_frames_remaining = self.dash_frames_total
            self.dash_direction = self.direction
            self.dash_speed_per_frame = self.dash_distance / float(self.dash_frames_total)
            self.dash_cooldown = 50  # set cooldown frames after dash

        
        if self.dash_cooldown > 0:
            self.dash_cooldown -= 1

        if self.is_dashing:
            # during dash, move at dash speed and skip normal acceleration
            move_amount = self.dash_speed_per_frame * self.dash_direction
            self.pos.x += move_amount
            self.dash_frames_remaining -= 1
            if self.dash_frames_remaining <= 0:
                self.is_dashing = False
                self.velocity = 0
                self.acceleration = 0.1
            self.rect.x = int(self.pos.x)
        
        else:

            if self.direction != 0:
                if self.direction == -1:
                    new_x = self.calculate_new_position(self.pos.x, "left") 
                else:
                    new_x = self.calculate_new_position(self.pos.x, "right")
                self.rect.x = int(new_x)
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

        




        

  