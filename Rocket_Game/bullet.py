import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, rg_game):
        super().__init__()
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.color = rg_game.settings.bullet_color

        self.rect = pygame.rect(0,0,self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midright = rg_game.rocket.image_rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)