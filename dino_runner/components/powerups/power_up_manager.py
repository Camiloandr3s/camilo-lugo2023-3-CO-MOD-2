import pygame
import random 

from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint (3, 5)
        self.appears_when = random.randint(200, 300)

    def generate_power_up(self):
        power_up = random.randint(0,1)
        if random.randint(0,1) == 0:
            self.appears_when += random.randint(200, 300)
            power_up = Shield()
            self.power_ups.append(power_up)
        else: 
            self.appears_when += random.randint(300, 400)
            power_up = Hammer()
            self.power_ups.append(power_up)

    def update(self, game):
        if len(self.power_ups) == 0 and self.appears_when == game.score.count:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration * 800)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.appears_when = random.randint(200, 300)
