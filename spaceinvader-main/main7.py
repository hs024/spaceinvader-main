import pygame
import random

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
#enemy
enemyimg=pygame.image.load("enemy1.png")
enemyx=random.randint(0,800)#random places
enemyy=random.randint(50,150)
enemyx_change=1
enemyy_change=40
def enemy(x,y):
    screen.blit(enemyimg,(x,y))#draw enemy
##################################################################33#####3
#background image
background=pygame.image.load("bg1.png")
##############################################################################
#bullet mechanics
#bullet
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=480#initial with player
bulletx_change=0
bullety_change=5
bullet_state="ready"
#ready--you cant see bullet on screen
#fire -- you see bullet on screen with fire
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))#draw bullet
    #bullet appear on center of screen
####################################################################################################

#game loop
while run:
    #first thing to do fill color
    # screen.fill((130,128,150))#it not update it fill
    screen.blit(background,(0,0))# background
    #background slow down the speed of palyer so we have to increase the value of change
    #event for closing
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #if key stroke press left or right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                #for left
                playerx_change=-5
            if event.key==pygame.K_RIGHT:
                #for right
                playerx_change=+5
            if event.key==pygame.K_SPACE:
                #for fire
                if bullet_state=="ready":
                    fire_bullet(playerx,bullety)
                    bulletx=playerx
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                #remove of key
                playerx_change=0

    #bullet movement
    if bullety<=0:
        bullety=480
        bullet_state="ready"

    if bullet_state=="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    #player variable
    playerx += playerx_change
    if playerx<=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    #enemy variable from left to right direction
    enemyx +=enemyx_change
    if enemyx<=0:
        enemyx_change=+1
        enemyy+=enemyy_change
    elif enemyx >=736:
        enemyx_change=-1
        enemyy+=enemyy_change
    player(playerx,playery)#calling player to draw #if it is above screen fill so it below this 
    enemy(enemyx,enemyy)
    
    
    pygame.display.update()#update the screen

    



