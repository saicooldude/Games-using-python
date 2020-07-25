import pygame
import random
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
###icon setting and caption#####
icon = pygame.image.load('enemy.png')
pygame.display.set_caption('space-invaders.png')
pygame.display.set_icon(icon)
##############background image##########
backgroundimage = pygame.image.load('background.png')
#########palyerimage###################
playerimg = pygame.image.load('space-invaders.png')
playerx = 370
playery = 400
playerxchange = 0
playerychange = 0
mixer.music.load('background.wav')
mixer.music.play(-1)

def player(x, y):
    screen.blit(playerimg, (x, y))


##########enemy iamge################
enemyimage = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
noofenemies=6
for i in range(noofenemies):
    enemyimage.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyxchange.append(1)
    enemyychange.append(10)


def enemy(x, y,i):
    screen.blit(enemyimage[i], (x, y))


##############bullet image#########
bulletimage = pygame.image.load('bullet.png')
bulletx = playerx
bullety = 480
bulletychange = 4
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage, (x + 16, y + 10))


##############collision########
def collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
    if distance < 27:
        return True
    else:
        return False
##################score##############
score_value=0

font = pygame.font.Font('freesansbold.ttf', 32)
def show_score(x,y):
    score=font.render("score is : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))


#########game over text################
def game_over_text():
    pass


while running:

    screen.blit(backgroundimage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerxchange = 5
            if event.key == pygame.K_LEFT:
                playerxchange = -5
            if event.key == pygame.K_UP:
                playerychange = -5
            if event.key == pygame.K_DOWN:
                playerychange = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletx = playerx
                    bullety = playery
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerychange = 0

    playerx = playerx + playerxchange
    playery = playery + playerychange
    if (playerx <= 0):
        playerx = 0
    elif (playerx >= 736):
        playerx = 736
    if(playery<=0):
        playery=0
    elif(playery>=736):
        playery=736
    for i in range(noofenemies):
        if enemyy[i]>=500:
            for j in range(noofenemies):
                enemyy[j]=2000
            game_over_text()
            break
        if (enemyx[i] < 0):
            enemyxchange[i] = 4
            enemyy[i] += enemyychange[i]
        if (enemyx[i] > 736):
            enemyxchange[i] = -4
            enemyy[i] += enemyychange[i]
        enemyx[i] += enemyxchange[i]
        collisio = collision(enemyx[i], enemyy[i], bulletx, bullety)
        if collisio:
            collision_sound=mixer.Sound('explosion.wav')
            collision_sound.play()
            bullety = playery
            score_value=score_value+1

            bullet_state = "ready"
            enemyx[i] = random.randint(0, 173)
            enemyy[i] = random.randint(50, 150)
        enemy(enemyx[i], enemyy[i],i)



    if bullety <= 0:
        bullety = playery
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety = bullety - bulletychange


    player(playerx, playery)
    show_score(10,10)##it shows the score at top left edge
    pygame.display.update()
