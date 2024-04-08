import pygame
from classes import *
from constants import *
import os
pygame.init()


WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TETRIS") 
def window_draw():
    WIN.fill(WHITE)
    pygame.display.update()









def game():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        window_draw()
  
if __name__=="__main__":        
    game()           
    