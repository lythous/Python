import pygame
import sys
from math import *


def main():
    screen_size = 720, 480
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: print("Down! ")
        
        t = pygame.time.get_ticks()/1000.0
        screen.fill(vis_function(1,1,t))
        pygame.display.flip()
        
        pygame.time.Clock().tick(50)
        print(t)


def vis_function(x, y, t):
    r = int(128+127*sin(t)**3)
    g = int(128+127*sin(3*t))
    b = int(128+127*sin(5*t))
    return (r, g, b)


if __name__ == "__main__":
    main()
