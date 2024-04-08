import pygame
from constants import *
from main import WIN

class Button:
    def __init__(self,string,x,y):
        self.button=pygame.Rect(250,100,x,y)
        Button.bliter(string,x,y)
    def bliter(self,string,x,y):
        WIN.blit(self.button,(x,y))
        text=get_text(string)
        WIN.blit(text, (x+5,y+5))
        


        
