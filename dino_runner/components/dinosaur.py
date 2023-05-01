import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

class Dinosaur:
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    DUCK_SPEED = 8.0

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.dino_run = True
        self.step_index = 0
        self.dino_jump = False
        self.jump_speed = self.JUMP_SPEED
        self.dino_duck = False
        self.duck_speed = self.DUCK_SPEED

    def update(self, user_input):

        if self.dino_run: 
            self.run()

        if self.step_index > 10:
            self.step_index = 0

        if self.dino_jump:
            self.jump()

        if self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True   
            if user_input[pygame.K_DOWN] and not self.dino_duck:
                self.dino_duck = True
                self.dino_run = False
            elif not self.dino_duck:
                self.dino_duck = False
                self.dino_run = True

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_speed*4
        self.jump_speed -= 0.8
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect.y = self.Y_POS
        self.duck_speed = 0.8
        if self.duck_speed < +self.DUCK_SPEED:
            self.dino_rect.y = 345
            self.dino_duck = False
            self.duck_speed = self.DUCK_SPEED

