import pygame
###########################################################
#initialize
pygame.init()
#screen created width,height
screen=pygame.display.set_mode((800,600))
#title and window icon
pygame.display.set_caption("space invader")
icon=pygame.image.load("logo.png")
pygame.display.set_icon(icon)
run=True
##################################################
#player image
playerimg=pygame.image.load("player.png")
playerx=370
playery=480
def player():
    screen.blit(playerimg,(playerx,playery))#draw player
########################################################


##############################################################################
#game loop
while run:
    #first thing to do fill color
    screen.fill((128,128,128))#it not update it fill
    #event for closing
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    #fill color of screen
    
    player()#calling player to draw #if it is above screen fill so it below this 
    pygame.display.update()#update the screen

    




