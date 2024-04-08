import pygame
import os
pygame.init()
'''---------------------------------------------------------------------------'''
WIDTH,HEIGHT,THICKNESS=1250,800,20
RATIO=HEIGHT//2
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("FROG JUMP GAME")    
WHITE=(255,255,255);BLACK=(0,0,0);RED=(255,0,0);YELLOW=(255,200,0);FPS=60

'''---------------------------------------------------------------------------'''
L1=pygame.Rect(150,500,100,100)
L2=pygame.Rect(300,500,100,100)
L3=pygame.Rect(450,500,100,100)
empty=pygame.Rect(600,500,100,100)
R1=pygame.Rect(1050,500,100,100)
R2=pygame.Rect(900,500,100,100)
R3=pygame.Rect(750,500,100,100)
x=-1
#LIST=[x,x,L1,L2,L3,empty,R3,R2,R1,x,x]
LEFT=[L1,L2,L3];RIGHT=[R1,R2,R3]
'''---------------------------------------------------------------------------'''
run=True
'''---------------------------------------------------------------------------'''
WATER=pygame.Rect(0,RATIO,WIDTH,HEIGHT//2)
SKY=pygame.Rect(0,0,WIDTH,HEIGHT//2)
'''---------------------------------------------------------------------------'''
reset_button=pygame.Rect(100,100,200,70)
exit_button=pygame.Rect(950,100,200,70)
'''---------------------------------------------------------------------------'''
R_FROG=pygame.image.load('frog.png')
R_FROG=pygame.transform.scale(R_FROG,(100,100))
L_FROG=pygame.image.load('frog2.png')
L_FROG=pygame.transform.scale(L_FROG,(100,100))
#L_FROG=pygame.transform.flip(L_FROG,True,False)
L_FROG1=L_FROG2=L_FROG3=L_FROG
R_FROG1=R_FROG2=R_FROG3=R_FROG
'''---------------------------------------------------------------------------'''

LEAF=pygame.image.load('leaf.png')
LEAF=pygame.transform.scale(LEAF,(120,120))
LEAF_LIST=[(150,500),(300,500),(450,500),(600,500),(750,500),(900,500),(1050,500)]

'''---------------------------------------------------------------------------'''
WON=pygame.Rect(370,150,500,500)
WON_img=pygame.image.load("WON.png")
WON_img=pygame.transform.scale(WON_img,(550,300))
won=pygame.Rect(WIDTH//8,HEIGHT//8,WIDTH//4,HEIGHT//4)
'''---------------------------------------------------------------------------'''
LOST=pygame.Rect(370,150,500,500)
LOST_img=pygame.image.load("LOST.png")
LOST_img=pygame.transform.scale(LOST_img,(550,300))
'''---------------------------------------------------------------------------'''
font = pygame.font.SysFont("arial", 80,bold=True)
font1 = pygame.font.SysFont("arial", 50,bold=True)
text_surface1= font1.render("RESET",True, WHITE)
text_surface2= font1.render("EXIT",True, WHITE)
text_surface = font.render("FROG  JUMP  GAME",True, (100, 100, 0))
WIN_center = (305,0)

os.chdir(os.getcwd())
'''---------------------------------------------------------------------------'''
def grid():
    for i in range(0,WIDTH,50):
        GRID_V=pygame.Rect(i,0,5,HEIGHT)
        pygame.draw.rect(WIN,BLACK,GRID_V)
    for i in range(0,HEIGHT,50):
        GRID_H=pygame.Rect(0,i,WIDTH,5)
        pygame.draw.rect(WIN,BLACK,GRID_H)
        
'''---------------------------------------------------------------------------'''
def draw_win(L1,L2,L3,R1,R2,R3):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,(0,100,150),WATER)
    pygame.draw.rect(WIN,(0,200,250),SKY)
    for j in LEAF_LIST:
        WIN.blit(LEAF,(j[0],j[1]))
    WIN.blit(L_FROG1,(L1.x,L1.y))
    WIN.blit(L_FROG2,(L2.x,L2.y))
    WIN.blit(L_FROG3,(L3.x,L3.y))
    WIN.blit(R_FROG1,(R1.x,R1.y))
    WIN.blit(R_FROG2,(R2.x,R2.y))
    WIN.blit(R_FROG3,(R3.x,R3.y))
    pygame.draw.rect(WIN,RED,reset_button)
    pygame.draw.rect(WIN,RED,exit_button)
    WIN.blit(text_surface, WIN_center)
    #WIN.blit(WON_img,(WON.x,WON.y))
    #grid()
    WIN.blit(text_surface1, (130,105))
    WIN.blit(text_surface2, (1005,105))
    pygame.display.update()
    
'''---------------------------------------------------------------------------'''
def reset(L1,L2,L3,empty,R1,R2,R3,LIST):
    L1.x,L1.y=150,500
    L2.x,L2.y=300,500
    L3.x,L3.y=450,500
    empty.x,empty.y=600,500
    R1.x,R1.y=1050,500
    R2.x,R2.y=900,500
    R3.x,R3.y=750,500
    LIST=[x,x,L1,L2,L3,empty,R3,R2,R1,x,x]
    game()
'''---------------------------------------------------------------------------'''

def menu():
    pass
    
'''---------------------------------------------------------------------------'''
def game():
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        #pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        
    pygame.quit()

'''---------------------------------------------------------------------------'''
if __name__=="__main__":
    game()