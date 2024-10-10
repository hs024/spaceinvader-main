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
################################################################
#player image
playerimg=pygame.image.load("player.png")
playerx=370
playery=480
playerx_change=0
playery_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))#draw player
##################################################################33#####3


##############################################################################
#game loop
while run:
    #first thing to do fill color
    screen.fill((130,128,150))#it not update it fill
    #event for closing
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #if key stroke press left or right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                #for left
                playerx_change=-0.3
            if event.key==pygame.K_RIGHT:
                #for right
                playerx_change=+0.3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                #remove of key
                playerx_change=0


    
    playerx += playerx_change
    if playerx<=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    player(playerx,playery)#calling player to draw #if it is above screen fill so it below this 
    pygame.display.update()#update the screen

    



