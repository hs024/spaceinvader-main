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
running=True
################################################################
#player image
playerimg=pygame.image.load("player.png").convert_alpha()
playerx=370
playery=480
playerx_change=0
playery_change=0
def player(x,y):
    screen.blit(playerimg,(x,y))#draw player

##################################################################33#####3
#enemy
listofenemyimg=["enemy1.png","enemy2.png","enemy3.png","enemy4.png","enemy5.png"]
enemyimg=[]
enemyy=[]
enemyx=[]
enemyx_change=[]
enemyy_change=[]
num0fenemy=10
es=1
noof_enemy=len(listofenemyimg)-1
key=0#for incresae speed of enemy
for i in range(num0fenemy):
    var_forenemyimg=random.randint(0,noof_enemy)
    enemyimg.append(pygame.image.load(listofenemyimg[var_forenemyimg]).convert_alpha())
    enemyy.append(random.randint(50,150))
    enemyx.append(random.randint(0,730))#random places
    enemyx_change.append(1)
    enemyy_change.append(40)

def enemy(x,y):
    screen.blit(enemyimg[i],(x,y))#draw enemy
##################################################################33#####3
#background image
background=pygame.image.load("bg1.png").convert_alpha()
#music
mixer.music.load("background.wav")
mixer.music.play(-1)






##############################################################################
#bullet mechanics
#bullet
bulletimg=pygame.image.load("bullet.png").convert_alpha()
bulletx=0
bullety=480#initial with player
bulletx_change=0
bullety_change=5
maxbullet=5
bullet_state=["ready",]*maxbullet
#ready--you cant see bullet on screen
bullets=[]
def fire_bullet_from(x,y):
    bullets.append([x+16,y+10,"fire"])
#fire -- you see bullet on screen with fire
def fire_bullet(x,y,z):
    # global bullet_state
    # bullet_state[i]="fire"
    # z="fire"
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
######################33################3#################################################
overfont=pygame.font.Font("freesansbold.ttf",82)
overfont2=pygame.font.Font("freesansbold.ttf",42)

def gameover():
    
    overtext=overfont.render("GAME OVER ",True,(255,255,255))
    screen.blit(overtext,(160,190))
    overtext2=overfont2.render("Total Score : "+str(score_value),True,(255,255,255))
    screen.blit(overtext2,(250,290))
##############################################################################################

level_value=1
# font=pygame.font.Font("freesansbold.ttf",26)
levelx=680
levely=10
def showlevel():
    level=font.render("Level :"+str(level_value),True,(255,255,255))
    screen.blit(level,(levelx,levely))
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
            running=False
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
                if len(bullets)<5:
                    fire_bullet_from(playerx,bullety)
                    # bulletx=playerx
                    bulletsound=mixer.Sound("laser.wav")
                    bulletsound.play()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                #remove of key
                playerx_change=0

    #bullet movement
    # if bullety<=0:
    #     bullety=480
    #     bullet_state="ready"

    # if bullet_state=="fire":
    #     fire_bullet(bulletx,bullety)
    #     bullety-=bullety_change
    for b in bullets:
        if b[1]<=0:
            bullets.remove(b)
        if b[2]=="fire":
            fire_bullet(b[0],b[1],b[2])
            b[1]-=bullety_change

    #player variable
    playerx += playerx_change
    if playerx<=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    #enemy variable from left to right direction
    for i in range(num0fenemy):
        if enemyy[i]>440:
            for j in range(num0fenemy):
                enemyy[j]=2000
            gameover()
            break
        enemyx[i] +=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=+es
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i] >=736:
            enemyx_change[i]=-es
            enemyy[i]+=enemyy_change[i]
        
   
        #collision checking enemy bullet
        for b in bullets:
            collision=iscollision(enemyx[i],enemyy[i],b[0],b[1])
            if collision:
                explosion=mixer.Sound("explosion.wav")
                explosion.play()
                bullets.remove(b)
                b[2]="ready"
                score_value+=1
                enemyx[i]=random.randint(0,730)#random places
                enemyy[i]=random.randint(50,150)
                #new enemy appear
                var=random.randint(0,noof_enemy)
                enemyimg[i]=pygame.image.load(listofenemyimg[var])
            
        enemy(enemyx[i],enemyy[i])
    player(playerx,playery)#calling player to draw #if it is above screen fill so it below this 
    showscore(scorex,scorey)
    showlevel()
    if score_value%6==0 and key==1 and score_value>2:
        es+=0.3
        key=0
    if score_value%6==1 and key==0:
        key=1
    if score_value==25:
        run=False
    
    pygame.display.update()#update the screen
##################################################################################################################################################################33
    #########################################################################################################3
#################################################################################################    
#starting of new screen
level_value+=1

#mainvillian
villianx=250
villiany=50
villiany_change=30
villianx_change=3
villianimg=pygame.image.load("villian.png")
villian_health=5
def villian(x,y):
    screen.blit(villianimg,(x,y))

winfont=pygame.font.Font("freesansbold.ttf",72)

def wingame():
    
    wintext=winfont.render("YOU WIN",True,(255,255,255))
    screen.blit(wintext,(160,190))
    overtext2=overfont2.render("Total Score : "+str(score_value),True,(255,255,255))
    screen.blit(overtext2,(250,290))


# background2=pygame.image.load("bg.png")

while running:
    screen.blit(background,(0,0))# background
    #background slow down the speed of palyer so we have to increase the value of change
    #event for closing
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
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
                # if bullet_state=="ready":
                if len(bullets)<5:
                    fire_bullet_from(playerx,bullety)
                    # bulletx=playerx
                    bulletsound=mixer.Sound("laser.wav")
                    bulletsound.play()
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
                #remove of key
                playerx_change=0

    #bullet movement
    # if bullety<=0:
    #     bullety=480
    #     bullet_state="ready"

    # if bullet_state=="fire":
    #     fire_bullet(bulletx,bullety)
    #     bullety-=bullety_change
    for b in bullets:
        if b[1]<=0:
            bullets.remove(b)
            b[2]="ready"
        if b[2]=="fire":
            fire_bullet(b[0],b[1],b[2])
            b[1]-=bullety_change

    #player variable
    playerx += playerx_change
    if playerx<=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    if villian_health!=0:
        villianx +=villianx_change
        if villianx<=0:
            villianx_change=+2
            villiany+=villiany_change
        elif villianx >=736:
            villianx_change=-2
            villiany+=villiany_change
        villian(villianx,villiany)
    else:
        wingame()
    #collision checking enemy bullet
    for b in bullets:
        collision=iscollision(villianx,villiany,b[0],b[1])
        if collision:
            explosion=mixer.Sound("explosion.wav")
            explosion.play()
            bullets.remove(b)
            b[2]="ready"
            villian_health-=1
            score_value+=1
            if villian_health==0:
                wingame()
                villiany=2000
                
            villianx=random.randint(0,730)#random places
            villiany=random.randint(50,150)
    player(playerx,playery)#calling player to draw #if it is above screen fill so it below this 
    showscore(scorex,scorey)
    showlevel()
    pygame.display.update()#update the screen



