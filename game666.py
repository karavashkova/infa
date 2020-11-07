import pygame
from pygame.draw import *
from random import *
pygame.init()

size = [1200, 900]
main = pygame.display.set_mode(size)
pygame.display.set_caption("панк группа шары")

FPS = 60
a = []
s1 = []
sum = 0

def click (event):
    global a
    a=(event.pos[0], event.pos[1])

def ball (x,y,r,color):
    circle(main, color, (x, y), r)
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False
vx1 = choice([-4, -3, -2, -1, 1, 2, 3, 4])
vy1 = choice([-4, -3, -2, -1, 1, 2, 3, 4])
r1 = randint(30,50)
x1 = randint(50,1150)
y1 = randint(50,850)
c1=(randint(50, 255), randint(50, 255), randint(50, 255))
c2=(randint(50, 255), randint(50, 255), randint(50, 255))
v2 = randrange(-5, 6, 2)
vx2 = v2
vy2 = v2
r2 = randint(30,50)
x2 = randint(50,1150)
y2 = randint(50,850)

x3 = randint(300,900)
y3 = randint(300,600)
r3 = randint(70, 100)
v3 = choice([-1, 1])
sqcolor = (0, 0, 0)
secret=0
click1=False

while click1==False:
    fontObj = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj = fontObj.render('START', True, (200, 200, 200), (0, 150, 100))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (600, 200)

    fontObj1 = pygame.font.Font('freesansbold.ttf', 50)
    textSurfaceObj1 = fontObj1.render('СHOOSE NICKNAME', True, (200, 200, 200), (0, 150, 100))
    textRectObj1 = textSurfaceObj1.get_rect()
    textRectObj1.center = (600, 300)

    main.blit(textSurfaceObj,textRectObj)
    main.blit(textSurfaceObj1,textRectObj1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            if (a[0]>395 and a[0]<747) and (a[1]>177 and a[1]<227):
                click1=True
            elif (a[0]>350 and a[0]<850) and (a[1]>278 and a[1]<325):
                click2=True



    
    
rect(main, (0, 0, 0), (0, 0, 1200, 900))
a = []

while finished==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    while finished==False:
        font = pygame.font.Font(None, 25)

        # Вывести переменную
        text = font.render("Score: "+str(sum),True,(100, 150, 130))
        main.blit(text, [0,0])
        font = pygame.font.Font(None, 50)
        text2 = font.render("l l", False, (250, 2, 150))
        main.blit(text2, [1150, 0])
        ball(x1, y1, r1, c1)
        ball(x2, y2, r2, c2)
        if secret==1:
            ball(x3, y3, r3, sqcolor)
        pygame.display.update()
        rect(main, (0, 0, 0), (0, 0, 100, 20))
        ball(x1, y1, r1, (0, 0, 0))
        ball(x2, y2, r2, (0, 0, 0))
        if secret==1:
            ball(x3, y3, r3, (0, 0, 0))
        x1+=vx1
        y1+=vy1
        x2+=vx2
        y2+=vy2
        r3+=v3
        click3=False

        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
                if ((a[0]-x1)**2 + (a[1]-y1)**2) <= r1**2:
                    sum+=10
                    print('dadadadada', sum)
                    vx1 = choice([-4, -3, -2, -1, 1, 2, 3, 4])
                    vy1 = choice([-4, -3, -2, -1, 1, 2, 3, 4])
                    r1 = randint(30,50)
                    x1 = randint(50,1150)
                    y1 = randint(50,850)
                    c1=(randint(50, 255), randint(50, 255), randint(50, 255))
                    secret = randint(0, 4)
                    sqcolor=(200, 0, 0)
                elif ((a[0]-x2)**2 + (a[1]-y2)**2) <= r2**2:
                    sum+=10
                    print('dadadadada', sum)
                    c2=(randint(50, 255), randint(50, 255), randint(50, 255))
                    vx2 = choice([-4, -3, -2, -1, 1, 2, 3, 4])
                    vy2 = choice([-4, -3, -2, -1, 1, 2, 3, 4])
                    r2 = randint(30,50)
                    x2 = randint(50,1150)
                    y2 = randint(50,850)
                    secret = randint(0, 4)
                    sqcolor=(200, 0, 0)
                elif ((a[0]-x3)**2 + (a[1]-y3)**2) <= r3**2:
                    sum+=50
                    print('yeeeeeeeeeees', sum)
                    x3 = randint(300,900)
                    y3 = randint(300,600)
                    r3 = randint(70, 120)
                    v3 = choice([-3, -2, -1, 1, 2, 3])
                    sqcolor = (0, 0, 0)
                    secret = 0
                elif (a[0]>1150 and a[0]<1175) and (a[1]>3 and a[1]<27):
                    a=[]
                    while click3==False:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                click(event)
                                if (a[0]>1150 and a[0]<1200) and (a[1]>3 and a[1]<27):
                                    click3=True
            elif event.type == pygame.QUIT:
                finished = True
        if x1>=(1200-r1):
            vx1*=(-1)
        elif x1<=(0+r1):
            vx1*=(-1)
        if y1>=(900-r1):
            vy1*=(-1)
        elif y1<=(0+r1):
            vy1*=(-1)
        if x2>=(1200-r2):
            vx2*=(-1)
        elif x2<=(0+r2):
            vx2*=(-1)
        if y2>=(900-r2):
            vy2*=(-1)
        elif y2<=(0+r2):
            vy2*=(-1)
        if r3>120 or r3<20:
            v3*=-1