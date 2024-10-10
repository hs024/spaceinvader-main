import pygame
#initialize
pygame.init()
#screen created
screen=pygame.display.set_mode((800,600))

run=True
#game loop
while run:
    #event for closing
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    




