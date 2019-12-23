import pygame
import sys
import myplane
import enemy
import bullet

from pygame.locals import *
from random import *

# 初始化pygame跟音乐
pygame.init()
pygame.mixer.init()

bg_size = wight, height = 480, 600
screen = pygame.display.set_mode(bg_size)

background = pygame.image.load('images/background.png').convert()

# 载入音乐

pygame.mixer.music.load('music/game_music.mp3')
pygame.mixer.music.set_volume(0.4)  # 设置音量


# bullet_sound = pygame.mixer.Sound('music/M1.wav')
# bullet_sound.set_volume(0.4)


def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def main():
    pygame.mixer.music.play(-1)

    # 生成我方飞机
    me = myplane.MyPlane(bg_size)

    # 生成一个敌机组
    enemies = pygame.sprite.Group()
    # 生成敌方小型飞机
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 3)
    # 生成敌方中型飞机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 2)
    # 生成敌方boss
    boss = enemy.BigEnemy(bg_size)
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies, enemies, 1)

    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4

    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet(me.rect.center))  # me.rect.midtop：机头位置
    # 设置帧数
    clock = pygame.time.Clock()

    # 中弹图片索引
    e1_destroy_index = 0
    e2_destroy_index = 0

    # 用于切换图片
    list_image = True

    # 用于延迟
    delay = 100
    sum = 0  # 计数器 计算敌机死亡数 到达一定数量刷新敌机
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 检测用户的键盘操作
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP] or key_pressed[K_w]:
            me.moveUp()
        if key_pressed[pygame.K_LEFT] or key_pressed[K_a]:
            me.moveLeft()
        if key_pressed[pygame.K_RIGHT] or key_pressed[K_d]:
            me.moveRight()
        if key_pressed[pygame.K_DOWN] or key_pressed[K_s]:
            me.moveDown()

        screen.blit(background, (0, 0))

        # 发射子弹
        if not (delay % 10):
            bullet1[bullet1_index].reset(me.rect.midtop)
            bullet1_index = (bullet1_index + 1) % BULLET1_NUM

        # 检测子弹是否击中敌机
        for b in bullet1:
            if b.active:
                b.move()
                screen.blit(b.image, b.rect)
                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                if enemy_hit:
                    b.active = False
                    for e in enemy_hit:
                        if e in mid_enemies or e in big_enemies:
                            e.hit = True
                            e.energy -= 1
                            if e.energy == 0:
                                e.active = False
                            sum += 1
                        else:  # 是小型敌机
                            e.active = False
                        sum += 1

                    if sum == 1:
                        add_small_enemies(small_enemies, enemies, 1)
                    elif sum == 2:
                        add_mid_enemies(mid_enemies, enemies, 1)
                    elif sum == 3:
                        add_big_enemies(big_enemies, enemies, 1)
        sum = 0

        # 绘制大型敌机
        for each in big_enemies:
            if each.active:
                each.move()
                if list_image:
                    screen.blit(each.image1, each.rect)
                else:
                    screen.blit(each.image2, each.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                    e1_destroy_index = (e1_destroy_index + 1) % 20
                    if e1_destroy_index == 0:
                        each.reset()
        # 绘制中型敌机
        for each in mid_enemies:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
                if list_image:
                    screen.blit(each.image, each.rect)
            else:
                # 毁灭
                each.reset()

        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image, each.rect)
                if list_image:
                    screen.blit(each.image, each.rect)
            else:
                # 毁灭
                each.reset()

        # 检测我方飞机是否被撞
        enemies_down = pygame.sprite.spritecollide(me, enemies, False)
        if enemies_down:
            me.active = False
            for e in enemies_down:
                e.active = False

        # 绘制我方飞机
        if me.active:

            screen.blit(me.image, me.rect)
        else:
            if not (delay % 3):
                screen.blit(me.destroy_images[e2_destroy_index], me.rect)
                e2_destroy_index = (e2_destroy_index + 1) % 6
                if e2_destroy_index == 0:
                    print("Game Over!")
                    running = False

        if not (delay % 5):
            list_image = not list_image

        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
    pygame.quit()
