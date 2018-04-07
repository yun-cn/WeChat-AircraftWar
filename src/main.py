#_*_ coding:utf-8 _*_

import pygame
from pygame.locals import *
import time


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 30
        self.y = 460
        self.screen       =  screen_temp
        self.image        =  pygame.image.load('./src/../image/hero.png')
        self.bullet_list  =  []  #An object that stores a bullet

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

    def left_move(self):
        self.x -=5
    def right_move(self):
        self.x +=5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x,  self.y))


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image  = pygame.image.load('./src/../image/bullet.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5


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
    screen = pygame.display.set_mode((320, 568), 0, 32)
    background = pygame.image.load('./src/../image/background.png')
    hero = HeroPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)

if __name__ == "__main__":
    main()
