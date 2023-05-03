import random
import pygame

from dino_runner.components.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import LARGE_AND_SMALL_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):        
        if len(self.obstacles) == 0:
            step_index = random.randint(1,2)
            if step_index % 2 == 0:
                cactus = Cactus(LARGE_AND_SMALL_CACTUS)
                self.obstacles.append(cactus)
            elif step_index % 2 == 1:
                bird = Bird(BIRD)
                self.obstacles.append(bird)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            #pygame.time.delay(100)
            if game.player.dino_rect.colliderect(obstacle.rect):
               game.playing = False
               break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []