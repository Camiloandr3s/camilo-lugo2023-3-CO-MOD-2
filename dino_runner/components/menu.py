import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT 

class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2

    def __init__(self, screen):
        screen.fill((175, 175, 175))
        self.font = pygame.font.Font(FONT_STYLE, 30)
    
    def update(self, game):
        self.hundle_event_on_menu(game)
        pygame.display.update()

    def draw(self, screen, message, x = half_screen_width, y = half_screen_height):
        text = self.font.render(message, True, (81, 77, 76))
        text_rect = text.get_rect()
        text_rect.center = (x,y)
        screen.blit(text, text_rect)

    def reset_screen_color(self, screen):
        screen.fill((175, 175, 175))

    def hundle_event_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                game.run()
