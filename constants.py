import pygame
pygame.init()
WIDTH,HEIGHT,THICKNESS=1250,800,20
RATIO=HEIGHT//2
screen_info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = screen_info.current_w, screen_info.current_h

# Set up constants
RECT_WIDTH_PERCENTAGE = 0.2  # Percentage of screen width for the rectangle
RECT_HEIGHT_PERCENTAGE = 0.1  # Percentage of screen height for the rectangle

# Calculate rectangle size based on screen resolution
RECT_WIDTH = int(SCREEN_WIDTH * RECT_WIDTH_PERCENTAGE)
RECT_HEIGHT = int(SCREEN_HEIGHT * RECT_HEIGHT_PERCENTAGE)
WHITE=(255,255,255);BLACK=(0,0,0);RED=(255,0,0);YELLOW=(255,200,0);FPS=60



def get_text(text,size=50,colour=WHITE,font="arial",Bold=True):
    FONT = pygame.font.SysFont(font, size,bold=Bold)
    return  FONT.render(text,True,colour)