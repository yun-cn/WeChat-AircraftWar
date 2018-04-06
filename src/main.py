#_*_ coding:utf-8 _*_

import pygame
from pygame.locals import *
import time


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 300
        self.screen = screen_temp
        self.image = pygame.image.load('./src/../image/hero.png')

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def left_move(self):
        self.x -=5
    def right_move(self):
        sefl.y +=5

def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 568), 0, 32)
    background = pygame.image.load('./src/../image/background.png')
    hero = HeroPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    hero.left_move()
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    hero.right_move()
                elif event.key == K_SPACE:
                    print('space')

        time.sleep(0.01)

if __name__ == "__main__":
    main()
