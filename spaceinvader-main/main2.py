import pygame
#initialize
pygame.init()
#screen created
screen=pygame.display.set_mode((800,600))
#title and window icon
pygame.display.set_caption("space invader")
icon=pygame.image.load("logo.png")
pygame.display.set_icon(icon)
run=True
#game loop
while run:
    #event for closing
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #fill color of screen
    screen.fill((128,128,128))#it not update it fill
    pygame.display.update()#update the screen

    




