import pygame 
import random
import time
pygame.init()

screenWidth = 500
screenHeight = 500 
gridSpacing = 25

snakeWidth = gridSpacing 
snakeLength = gridSpacing 
x = 0
y = 0
vel = gridSpacing 
direction = 0

screen = pygame.display.set_mode((screenWidth + 25,screenHeight + 50))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

def redraw(): 
    i = 0
    while i <= screenHeight / gridSpacing: 
        pygame.draw.rect(screen, (255,255,255), (0,i*gridSpacing, screenWidth,2))
        i += 1

    j = 0
    while j <= screenWidth / gridSpacing: 
        pygame.draw.rect(screen, (255,255,255), (j*gridSpacing,0, 2,screenHeight))
        j += 1
    pygame.draw.rect(screen, (255,255,255), (x,y, gridSpacing,gridSpacing))
    
    pygame.draw.rect(screen, (0,0,0), (0,screenHeight+2, screenWidth,20))
    scoretext = scoreFont.render("Score: {0}".format(score), 1, (255,255,255))
    screen.blit(scoretext, (5, screenHeight))
    
    pygame.display.update() 

    
arrx = [0]
arry = [0]
    
xrand = random.randint(0,screenWidth/gridSpacing - 1) * gridSpacing
yrand = random.randint(0,screenHeight/gridSpacing - 1) * gridSpacing

scoreFont = pygame.font.SysFont("Arial",20,True)

score = 0

run = True 

#main loop
while run == True: 
    
    clock.tick(27)
    pygame.time.delay(100)
    
    xlast = x
    ylast = y
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if direction == 1: 
            run = False
        else: 
            direction = 0
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]: 
        if direction == 0: 
            run = False
        else: 
            direction = 1
    elif keys[pygame.K_UP] or keys[pygame.K_w]: 
        if direction == 3: 
            run = False
        else: 
            direction = 2
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if direction == 2: 
            run = False
        else: 
            direction = 3
    
    if direction == 0: 
        x += vel
    if direction == 1: 
        x -= vel
    if direction == 2: 
        y -= vel
    if direction == 3: 
        y += vel
        
    
    
    pygame.draw.rect(screen, (0,255,0), (xrand,yrand, gridSpacing,gridSpacing))
    
    pygame.draw.rect(screen, (0,0,0), (arrx[0],arry[0], gridSpacing,gridSpacing))
    
    
    
    if x < 0: 
        x = screenWidth - gridSpacing
    if x > screenWidth - gridSpacing: 
        x = 0
    if y < 0: 
        y = screenHeight - gridSpacing 
    if y > screenHeight - gridSpacing: 
        y = 0
    if len(arrx) >= 4 and ((x in arrx[0:-2:1]) and (y == arry[arrx.index(x)])):
        run = False
        
    if x == xrand and y == yrand: 
        xrand = random.randint(0,screenWidth/gridSpacing - 1) * gridSpacing
        yrand = random.randint(0,screenHeight/gridSpacing - 1) * gridSpacing
        score += 1
    else: 
        arrx.pop(0)
        arry.pop(0) 
        
    arrx.append(x)
    arry.append(y)
    
    redraw()
    
time.sleep(3)

pygame.quit()
