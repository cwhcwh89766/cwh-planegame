# -*- coding: utf-8 -*-
# 描述     ：
# @Time    : 2019/12/2 17:49
# @Author  : 成少雷
# @Site    : online.codingfans.cc
# @File    : game.py
# @Email   : landmark_csl@126.com
import random

import pygame
from pygame.locals import *

WINDOWSIZE = (300, 600)  # 屏幕尺寸
screen = None  # 屏幕
enemys = []  # 敌人
plane = None  # 我方


class Plane:
    def __init__(self, image_name, screen, xy):
        self.image = pygame.image.load(image_name)
        self.screen = screen
        self.x = xy[0]
        self.y = xy[1]
        self.bullets = []

    def show(self):
        # 显示飞机
        self.screen.blit(self.image, (self.x, self.y))
        # 判断是否移出边界，如果移出边界则删除
        for i in range(len(self.bullets) - 1, -1, -1):
            if self.bullets[i].is_out():
                self.bullets.pop(i)
        # 显示子弹
        for bullet in self.bullets:
            bullet.move()
            bullet.show()

    def show_bullet(self):
        for bullet in self.bullets:
            print(bullet, end=" ")
        print()

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def forward(self):
        self.y -= 10

    def fire(self):
        bullet = MyBullet("images/bullet.png", (self.x + 10, self.y - 10), self.screen)
        self.bullets.append(bullet)


class Enemy:
    def __init__(self, image_name, xy, screen):
        self.image = pygame.image.load(image_name)
        self.x = xy[0]
        self.y = xy[1]
        rec = self.image.get_rect()
        self.position = Rect(self.x, self.y, rec.width, rec.height)
        self.screen = screen
        self.bullets = []

    def show(self):
        self.screen.blit(self.image, (self.x, self.y))
        self.forward()

    def move_left(self):
        self.x += 5
        self.position.x = self.x

    def move_right(self):
        self.x -= 5
        self.position.x = self.x

    # def move_up(self):
    #     self.y += 5
    #     self.position.y = self.y
    #
    # def move_down(self):
    #     self.y -= 5
    #     self.position.y = self.y

    def forward(self):
        self.y += 5
        self.position.y = self.y


class Bullet:
    def __init__(self, image_name, xy, screen):
        self.x = xy[0]
        self.y = xy[1]
        self.screen = screen
        self.image = pygame.image.load(image_name)
        rec = self.image.get_rect()
        self.position = Rect(self.x, self.y, rec.width, rec.height)

    def __str__(self):
        return f"({self.x},{self.y},{self.position.width},{self.position.height})"

    def is_out(self):  # 是否移出边界
        pass

    def move(self):
        pass

    def show(self):
        self.position = self.screen.blit(self.image, (self.x, self.y))


class MyBullet(Bullet):
    def move(self):
        self.y -= 5

    def is_out(self):
        return self.y <= 0


class EnemyBullet(Bullet):
    def move(self):
        self.y += 5

    def is_out(self):
        return self.y > WINDOWSIZE[1]


def game_init():
    pygame.init()
    global screen
    screen = pygame.display.set_mode(WINDOWSIZE)

    pygame.display.set_caption("碰碰")
    screen.fill((255, 255, 255))


def generate_enemy():
    enemy = Enemy("images/enemy.png", (random.randint(50, WINDOWSIZE[0] - 50), 0), screen)
    enemys.append(enemy)


def enemy_bump_mybullet():
    for i in range(len(enemys) - 1, -1, -1):
        index = -1
        for j in range(len(plane.bullets) - 1, -1, -1):
            if pygame.Rect.colliderect(enemys[i].position, plane.bullets[j].position):
                enemys.pop(i)
                plane.bullets.pop(j)
                return


def main():
    global plane
    ALERT = USEREVENT + 1
    pygame.time.set_timer(ALERT, 5000)
    game_init()
    plane = Plane("images/plane.png", screen, (150, 550))
    res = plane.image.get_rect()

    running = True
    while running:
        screen.fill((255, 255, 255))
        plane.show()
        for enemy in enemys:
            enemy.show()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:  # 按空格开火
                    plane.fire()
                # if event.key == K_RIGHT: # 右移
                #     plane.move_right()
                # elif event.key == K_LEFT: # 左移
                #     plane.move_left()
                # elif event.key == K_SPACE: # 按空格开火
                #     print("dddd")
                #     plane.fire()
            elif event.type == ALERT:
                print("alert")
                generate_enemy()

        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_UP]:
            plane.move_up()
        if key_list[pygame.K_LEFT]:
            plane.move_left()
        if key_list[pygame.K_RIGHT]:
            plane.move_right()
        if key_list[pygame.K_DOWN]:
            plane.move_down()

        pygame.time.Clock().tick(60)
        # 碰撞检测
        # 我方子弹和敌方飞机
        enemy_bump_mybullet()
        pygame.display.flip()


if __name__ == "__main__":
    main()
