import pygame
import random
import math
from pygame import mixer

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
################################################################r
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
enemyimg=[]
enemyy=[]
enemyx=[]
enemyx_change=[]
enemyy_change=[]
num0fenemy=6
for i in range(num0fenemy):
    enemyimg.append(pygame.image.load("enemy1.png"))
    enemyy.append(random.randint(50,150))
    enemyx.append(random.randint(0,730))#random places
    enemyx_change.append(1)
    enemyy_change.append(40)

def enemy(x,y):
    screen.blit(enemyimg[i],(x,y))#draw enemy
##################################################################33#####3
#background image
background=pygame.image.load("bg1.png")
#music
mixer.music.load("background.wav")
mixer.music.play(-1)






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
#collision detection of bullet enemy
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2 + (enemyy-bullety)**2)
    if distance<27:
        return True
    else:
        return False
###############################################################3
score_value=0
font=pygame.font.Font("freesansbold.ttf",26)
scorex=10
scorey=10
def showscore(x,y):
    score=font.render("score value:"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
######################33################3
overfont=pygame.font.Font("freesansbold.ttf",64)

def gameover():
    
    overtext=overfont.render("GAME OVER ",True,(255,255,255))
    screen.blit(overtext,(200,190))
    overtext2=overfont.render("Total Score : "+str(score_value),True,(255,255,255))
    screen.blit(overtext2,(190,280))



###############################################################################3
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
                    bulletsound=mixer.Sound("laser.wav")
                    bulletsound.play()
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
    for i in range(num0fenemy):
        if enemyy[i]>400:
            for j in range(num0fenemy):
                enemyy[j]=2000
            gameover()
            break
        enemyx[i] +=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=+1
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i] >=736:
            enemyx_change[i]=-1
            enemyy[i]+=enemyy_change[i]
        
   
        #collision checking enemy bullet
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            explosion=mixer.Sound("explosion.wav")
            explosion.play()
            bullety=480
            bullet_state="ready"
            score_value+=1
            enemyx[i]=random.randint(0,730)#random places
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i])
    player(playerx,playery)#calling player to draw #if it is above screen fill so it below this 
    showscore(scorex,scorey)
    pygame.display.update()#update the screen

    




