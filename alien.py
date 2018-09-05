import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像与碰撞体
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #创建外星人位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)