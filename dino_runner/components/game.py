import pygame
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, ICON_DEFEAT, DEFAULT_TYPE, RESET
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menu import Menu
from dino_runner.components.counter import Counter
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.cloud import Cloud

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_manager = PowerUpManager()
        self.menu = Menu(self.screen)
        self.running = False
        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()
        self.cloud = Cloud()
        self.color_screen = True
        self.has_power_up = True
        self.death = False

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
         
    def run(self):
        self.reset_game()
        self.playing = True               # <------------------ Game loop: events - update - draw
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_manager.update(self)
        self.score.update()
        self.update_score()
        self.cloud.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((176, 176, 176))
        self.paint_draw()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_manager.draw(self.screen)        
        self.score.draw(self.screen, self.color_screen)
        self.power_up()
        self.cloud.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.color_screen = True
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        if self.death_count.count == 0:
            self.menu.draw(self.screen, "Please press any key to start game..")
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_height - 140))
        else:
            self.update_highest_score()
            self.menu.draw(self.screen, "Press any key to restard to game")
            self.menu.draw(self.screen, f"Your score: {self.score.count}", half_screen_width, 350, )
            self.menu.draw(self.screen, f"Highest score: {self.highest_score.count}", half_screen_width, 400, )
            self.menu.draw(self.screen, f"Deaths: {self.death_count.count}", half_screen_width, 450, )

            self.screen.blit(ICON_DEFEAT, (half_screen_width - 180, half_screen_height - 200))
            self.screen.blit(RESET, (half_screen_width - 50, half_screen_height - 140))

        self.menu.update(self)

    def update_score(self):
        if self.score.count % 100 == 0 and self.game_speed < 500:
            self.game_speed += 1
        
        if self.score.count == 1500:
            self.color_screen = False

        #print (f"Score: {self.score} Speed: {self.game_speed}")
    
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = self.GAME_SPEED
        self.score.reset()
        self.player.reset()
        self.power_manager.reset_power_ups()

    def paint_draw(self):
        if self.color_screen == True:
            self.screen.fill((176, 176, 176))
 
        elif self.color_screen == False:
            self.screen.fill((0, 0, 0))
 
    def power_up(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) /800, 2 )
            if time_to_show >= 0:
                self.menu.draw(self.screen, f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", 500, 50)
            else: 
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

                               