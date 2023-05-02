import pygame

from dino_runner.components.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            #pygame.time.delay(100)
            if game.player.dino_rect.colliderect(obstacle.rect):
               game.playing = False
               break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)