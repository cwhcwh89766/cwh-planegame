import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/myplane.png").convert_alpha()
        self.destroy_images = []
        # 绘制飞机摧毁后图片切换
        self.destroy_images.extend([
            pygame.image.load('images/bomb0.png').convert_alpha(),
            pygame.image.load('images/bomb1.png').convert_alpha(),
            pygame.image.load('images/bomb2.png').convert_alpha(),
            pygame.image.load('images/bomb3.png').convert_alpha(),
            pygame.image.load('images/bomb4.png').convert_alpha(),
            pygame.image.load('images/bomb5.png').convert_alpha()
        ])
        # 设置飞机的位置
        self.rect = self.image.get_rect()
        self.widht, self.height = bg_size[0], bg_size[1]
        # 飞机在屏幕上的初始位置
        self.rect.left, self.rect.top = (self.widht - self.rect.width) // 2, \
                                        self.height - self.rect.height - 60
        self.speed = 10  # 飞机的飞行速度
        self.active = True  # 飞机存活
        self.mask = pygame.mask.from_surface(self.image)  # 将非透明部分标记为mask

    # 如果飞机飞出边框之外则停止在边框
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 20:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 20

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.widht:
            self.rect.left += self.speed
        else:
            self.rect.right = self.widht
