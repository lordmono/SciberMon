from threading import currentThread
from tkinter import Menu
import pygame,sys,datetime
from random import *
from math import *

pygame.init()
winW,winH = 480,480
win = pygame.display.set_mode((winW,winH))
clock = pygame.time.Clock()
font = pygame.font.SysFont('FRAMD.ttf',24)


def cmds():
    global x01a
    for event in pygame.event.get():
        mousPos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if feed.isOver(mousPos):
                if x01a.belly < 150:
                    x01a.belly += 25
                if x01a.belly > 150:
                    x01a.belly += 25
                    x01a.happines -= 10
                    if x01a.belly > 200:
                        x01a.belly = 200

        if event.type == pygame.MOUSEMOTION:
            if feed.isOver(mousPos):
                feed.color = '#339933'
            else:
                feed.color = '#333333'

class Mon:
    def __init__(self,name):
        self.name = name
        self.shape = randint(0,0)
        self.color = randint(0,8)
        self.horns = randint(0,1)
        self.x = 200
        self.y =170
        self.speed = randint(1,3)
        self.maxMoveTimer = 50*self.speed
        self.curMoveTimer = self.maxMoveTimer
        self.belly = 100
        self.maxEn = 100
        self.curEn = self.maxEn
        self.activeTime = randint(0,1)
        self.sleep = False
        self.mhp = 100
        self.chp = self.mhp
        self.happines = 100

        if self.color == 0 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_black.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 0 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_black_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 1 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_white.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 1 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_white_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 2 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_gray.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 2 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_gray_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 3 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_red.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 3 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_red_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 4 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_blue.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 4 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_blue_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 5 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_green.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 5 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_green_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 6 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_yellow.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 6 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_yellow_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 7 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_purple.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 7 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_purple_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 8 and self.horns == 0:
            self.img = pygame.image.load('resources\sq_teal.png')
            self.img = pygame.transform.scale(self.img,(70,70))
        if self.color == 8 and self.horns == 1:
            self.img = pygame.image.load('resources\sq_teal_h.png')
            self.img = pygame.transform.scale(self.img,(70,70))

    def move(self):     
        if self.curMoveTimer == 0:
            rDir = randint(0,2)
            if rDir == 1:
                self.x -= 35
                self.belly -= 0.1
                self.curEn -= 0.1*self.speed
                self.curMoveTimer = self.maxMoveTimer
            if rDir == 2:
                self.x += 35
                self.belly -= 0.1
                self.curEn -= 0.1*self.speed
                self.curMoveTimer = self.maxMoveTimer

            if self.x < 0:
                self.x = 0
            if self.x+70 > winW:
                self.x = winW-70

            self.happines -= 0.1
            if self.happines < 0:
                self.happines = 0

        else:
            self.curMoveTimer -= 1

    def draw(self):
        if self.speed == 3:
            speed = font.render(f'Speed: Slow',True,'white')
        if self.speed == 2:
            speed = font.render(f'Speed: Average',True,'white')
        if self.speed == 1:
            speed = font.render(f'Speed: Fast',True,'white')

        name = font.render(f'Name: {self.name}',True,'white')
        belly = font.render(f'Fullness: {int(self.belly)}%',True,'white')
        energy = font.render(f'Energy: {int(self.curEn)}%',True,'white')
        if self.activeTime == 0:
            active = font.render(f'Active: 6am-10pm',True,'white')
        if self.activeTime == 1:
            active = font.render(f'Active: 12pm-4am',True,'white')
        hp = font.render(f'HP: {self.chp}/{self.mhp}',True,'white')
        happy = font.render(f'Happiness: {int(self.happines)}',True,'white')

        win.blit(self.img,(self.x,self.y))
        win.blit(name,(5,(winH/2)+5))
        win.blit(hp,(5,(winH/2)+20))
        win.blit(energy,(5,(winH/2)+35))
        win.blit(belly,(5,(winH/2)+60))
        win.blit(speed,(5,(winH/2)+75))
        win.blit(active,(5,(winH/2)+90))
        win.blit(happy,(5,(winH/2)+115))

        if self.sleep == True:
            sleep = pygame.image.load('resources\sleep.png')
            sleep = pygame.transform.scale(sleep,(70,70))
            eyes = pygame.image.load('resources\eyes_closed.png')
            eyes = pygame.transform.scale(eyes,(50,20))
            win.blit(eyes,(self.x+10,self.y+10))
            win.blit(sleep,(self.x+70,self.y-70))
            # isAsleep = font.render(f'Sleeping: {self.sleep}',True,'white')
            # win.blit(isAsleep,(10,100))
        if self.sleep == False:
            eyes = pygame.image.load('resources\eyes_open.png')
            eyes = pygame.transform.scale(eyes,(40,20))
            win.blit(eyes,(self.x+15,self.y+15))
        


    def update(self):
        curTime = datetime.datetime.now().time()

        if self.activeTime == 0:
            start = datetime.time(6, 0, 0)
            end = datetime.time(22, 0, 0)
            if curTime >= start and curTime <=end:
                self.sleep = False
                self.move()
            else:
                self.sleep = True
                self.curEn += 0.1

        if self.activeTime == 1:
            start = datetime.time(12, 0, 0)
            end = datetime.time(4, 0, 0)
            if curTime >= start or curTime <=end:
                self.sleep = False
                self.move()
            else:
                self.sleep = True
                self.curEn += 0.1

        if self.curEn > self.maxEn:
            self.curEn = self.maxEn

        self.draw()

class BgPart:
    reg = []
    def __init__(self,x,y,w,h,t,c):
        self.x,self.y,self.w,self.h,self.t = x,y,w,h,t
        self.color = c
        BgPart.reg.append(self)

    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(win,self.color,self.rect,self.t)

    def update(self):
        self.draw()

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('FRAMD.ttf',24)
            text = font.render(self.text, 1, 'white')
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

feed = Button('#333333',180,250,40,25,'Feed')
x01a = Mon('X01A')
skyBox = BgPart(0,0,winW,winH/2,0,'#00aaff')
stars = []

text = ""
input_active = True
menuState = 0

def makeName():
    global text,input_active,menuState,x01a
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                x01a.name = text
                menuState = 1
                main()
                return None
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode

        win.fill(0)
        mnb = pygame.Rect(155,190,200,75)
        pygame.draw.rect(win,'blue',mnb)
        mnt = font.render('Enter partners name',True,'white')
        win.blit(mnt,(175,200))
        mnc = pygame.Rect(165,225,180,25)
        pygame.draw.rect(win,'white',mnc)
        text_surf = font.render(text, True, (255, 0, 0))
        win.blit(text_surf, text_surf.get_rect(center = win.get_rect().center))
        pygame.display.flip()

def main():
    global menuState
    day = datetime.time(6, 0, 0)
    night = datetime.time(21, 0, 0)
    run = True

    while run:
        if menuState == 0:
            makeName()
        if menuState == 1:
            curTime = datetime.datetime.now().time()
            win.fill('black')
            cmds()

            rect0 = pygame.Rect(0,240,155,240)
            rect1 = pygame.Rect(154,240,winW-155,240)
            rect3 = pygame.Rect(0,294,155,2)
            rect4 = pygame.Rect(0,350,155,2)
            pygame.draw.rect(win,'white',rect0,2)
            pygame.draw.rect(win,'white',rect1,2)
            pygame.draw.rect(win,'white',rect3)
            pygame.draw.rect(win,'white',rect4)

            if curTime >= day and curTime <= night:
                skyBox.color = '#00aaff'
                for s in stars:
                    del s
                stars.clear()
            if curTime >= night or curTime <= day:
                skyBox.color = '#333333'
                if len(stars)<50:
                    for s in range(50):
                        s = BgPart(randint(skyBox.x+1,skyBox.x+(skyBox.w-1)),randint(skyBox.y+1,skyBox.y+(skyBox.h-1)),2,2,0,'#aaaa00')
                        stars.append(s)

            for b in BgPart.reg:
                b.update()

            rect2 = pygame.Rect(0,230,winW,10)
            pygame.draw.rect(win,'#009900',rect2)

            feed.draw(win,'#888833')
            x01a.update()
            
            pygame.display.flip()
            clock.tick(60)

main()