#_*_ coding:utf-8 _*_

import pygame
import time


def main():
    pygame.init()
    screen = pygame.display.set_mode((320, 568), 0, 32)
    background = pygame.image.load('./src/../image/background.png')
    hero = pygame.image.load('./src/../image/hero.png')

    x = 210
    y = 320
    while True:
        pygame.event.get()
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        pygame.display.update()
        x+=1
        time.sleep(0.01)

if __name__ == "__main__":
    main()
