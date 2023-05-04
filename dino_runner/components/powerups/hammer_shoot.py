import pygame
from pygame.sprite import Sprite
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import HAMMER

class HammerShoot(Sprite):
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.center = (self.dinosaur.dino_rect.x + 100, self.dinosaur.dino_rect.y + 20)
        self.speed_hammer = 100
        self.hammer = False
        self.shoot = False

    def update(self, user_input):
        if user_input[pygame.K_q] or user_input[pygame.K_SPACE] and not self.shoot:
            self.shoot = True
            self.hammer = True 
            self.rect.x += self.speed_hammer
