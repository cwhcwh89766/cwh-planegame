import pygame
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/enemy1.png').convert_alpha()
        # self.destroy_images = []
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 3
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)  # 将非透明部分标记为mask
        # 敌机出现的位置 随机坐标
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-2 * self.height, 0)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-2 * self.height, 0)


class MidEnemy(pygame.sprite.Sprite):
    energy = 4
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/enemy2.png').convert_alpha()
        # self.destroy_images = []
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)  # 将非透明部分标记为mask
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-4 * self.height, -self.height)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-4 * self.height, -self.height)


class BigEnemy(pygame.sprite.Sprite):
    energy = 10
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load('images/boss0.png').convert_alpha()
        self.image2 = pygame.image.load('images/boss1.png').convert_alpha()
        # 创建图片列表存放
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load('images/bossbomb1.png').convert_alpha(),
            pygame.image.load('images/bossbomb2.png').convert_alpha(),
            pygame.image.load('images/bossbomb3.png').convert_alpha(),
            pygame.image.load('images/bossbomb4.png').convert_alpha(),
            pygame.image.load('images/bossbomb5.png').convert_alpha(),
            pygame.image.load('images/bossbomb6.png').convert_alpha(),
            pygame.image.load('images/bossbomb7.png').convert_alpha(),
            pygame.image.load('images/bossbomb8.png').convert_alpha(),
            pygame.image.load('images/bossbomb9.png').convert_alpha(),
            pygame.image.load('images/bossbomb10.png').convert_alpha(),
            pygame.image.load('images/bossbomb11.png').convert_alpha(),
            pygame.image.load('images/bossbomb12.png').convert_alpha(),
            pygame.image.load('images/bossbomb13.png').convert_alpha(),
            pygame.image.load('images/bossbomb14.png').convert_alpha(),
            pygame.image.load('images/bossbomb15.png').convert_alpha(),
            pygame.image.load('images/bossbomb16.png').convert_alpha(),
            pygame.image.load('images/bossbomb17.png').convert_alpha(),
            pygame.image.load('images/bossbomb18.png').convert_alpha(),
            pygame.image.load('images/bossbomb19.png').convert_alpha(),
            pygame.image.load('images/bossbomb20.png').convert_alpha()
        ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.mask = pygame.mask.from_surface(self.image1)  # 将非透明部分标记为mask
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-6 * self.height, -2 * self.height)


    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-6 * self.height, -2 * self.height)
