#_*_ coding:utf-8 _*_

import pygame
from pygame.locals import *
import time
import random

class BasePlane(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x             =  x
        self.y             =  y
        self.screen        = screen_temp
        self.image         =  pygame.image.load(image_name)
        self.bullet_list   = []


class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 30, 460, './src/../image/hero.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)



    def left_move(self):
        self.x -=5
    def right_move(self):
        self.x +=5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x,  self.y))


class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, './src/../image/enemy-1.png')
        self.direction   =   "right"

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def move(self):
        if self.x > 280:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'

        if self.direction     == "right":
            self.x += 5
        elif self.direction   == "left":
            self.x -= 5

    def fire(self):
        if random.randint(1, 20) == 10:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class BaseBullet(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x           =   x
        self.y           =   y
        self.screen      =   screen_temp
        self.image       =   pygame.image.load(image_name)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+40, y-20, './src/../image/bullet-1.png')

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 15, y + 27, './src/../image/bullet-2.png')

    def move(self):
        self.y  +=  5

    def judge(self):
        if self.y < 568:
            return True
        else:
            return False



def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.left_move()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.right_move()
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()


def main():
    pygame.init()
    screen      =   pygame.display.set_mode((320, 568), 0, 32)
    background  =   pygame.image.load('./src/../image/background.png')
    hero        =   HeroPlane(screen)
    enemy       =   EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
