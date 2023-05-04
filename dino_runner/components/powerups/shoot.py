import pygame 
from pygame.sprite import Sprite

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.utils.constants import HAMMER

class Shoot(Sprite):
    def __init__(self):
        self.dinosaur = Dinosaur()
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.center = (self.dinosaur.dino_rect.x + 100, self.dinosaur.dino_rect.y + 20)
        self.hammer_speed = 100
        self.hammer = False
        self.shoot = False

    def update(self, user_input):
        if user_input[pygame.K_q] and not self.shoot:
            self.shoot = True
            self.hammer = True
            self.rect.x += self.hammer_speed
