from pygame import *
from button import Button
from time import sleep
from random import *
window = display.set_mode((700,700))
clock = time.Clock()
bkrnd_img = image.load('cona.png')
bkrnd = transform.scale(bkrnd_img, (700,700))
game = True
bkrnd_wert = image.load('fon.jpg')
bkrnd_wer = transform.scale(bkrnd_wert, (700,700))
record = 0

class Sprite(sprite.Sprite):
    def __init__(self, h , w , x ,y , image_name, speed ):
        super().__init__()
        sprite.Sprite.__init__(self)
        self.image = image.load(image_name)
        self.image = transform.scale(self.image, (w , h))
        self.h = h
        self.w = w
        
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw (self):
        window.blit(self.image , (self.rect.x, self.rect.y))
    def killed(self):
        self.kill()

class Player(Sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x = -70 
            self.rect.y = 530
        if keys[K_s]:
            self.rect.x = 100
            self.rect.y = 530
        if keys[K_d]:
            self.rect.x = 285
            self.rect.y = 530
        if keys[K_f]:
            self.rect.x = 455
            self.rect.y = 530



    def fire(self):
        bullet = Bulet(15,20,self.rect.centerx,self.rect.top,'bullet.png',3 )
        bullets.add(bullet)
        bullet = Bulet(50,40,self.rect.centerx,self.rect.top,'bullet.png',6 )
        keys = key.get_pressed()

        if mouse.get_pressed()[0]==1:
            global patrons
            patrons
            bullets.add(bullet)


class Bulet(Sprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y <= 0 :
            self.kill()
        if self.rect.y <= 500 :
            self.kill()
class Bomb(Sprite):
    def update(self):
        self.kill()   
class Enemy (Sprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global record
        if self.rect.y >= 650 :
            self.rect.y = 0
            a = randint(1,4)
            if a == 1 :
                self.rect.x = -80
                self.rect.x = -70

            if a == 2 :
                self.rect.x = 50
            if a == 3 :
                self.rect.x = 255
            if a == 4 :
                self.rect.x = 445
            if record >=10:
                self.speed = randint(2,3)
                record = record +  1
            elif record >=20 :
                self.speed = randint(2,6)
                record = record + 1
            elif record >= 30 :
              self.speed = randint(3,10)
              record = record + 1
            elif record <= 30 :
              self.speed = randint(5,10)
              record = record + 1
        #if  self.rect.y == 530:
        #    lifes = lifes - 1
        #def cill() :

def zoombi_kill():
    for i in zoombis:
            for j in bullets:
                if i.rect.colliderect(j.rect):
                    Ko = False






bullets = sprite.Group()

zoombi = sprite.Group()
zoombis = sprite.Group()

for i in range(1,6):
    zoombi = Enemy(100,50,-70,50,'zoombi.png',50)
    zoombis.add(zoombi)

bg = transform.scale(image.load("cona.png"),(700,700))
bt = transform.scale(image.load("fon.jpg"),(700,700))
player = Player (300,300,400 , 530,  "player.png" , 40)
start = Button (250,150, 200,150,"start.png")
Lord_exit = Button (250,350, 200,150,"stop.png")
exit = Button (590,560, 100,40,"start.png")
pausa = Button (590,0, 100,40,"stop.png")
easy = Button (450,200, 150,150,"easy2.png")
normale = Button (-260,200, 500,350,"normal.png")
hurd = Button (-260,350, 500,350,"hard.png")
run1 = False
run2 = True
mixer.init()
mixer.music.load("musik.mp3")
mixer.music.play()
lifes = 3
record = 0
patrons = 0
gold = 0

level = ""
font.init()
font = font.SysFont('Arial',24)
while game :
    for e in event.get() :
        if e.type == QUIT :
            game = False
        if e.type == KEYDOWN :
            if e.key == K_ESCAPE:
                run2 = not run2
        elif e.type == KEYDOWN:
            if e.key == K_SPACE :
                player.fire() 
                
    if run2 == True:
        window.blit(bt,(0,0))
        if start.draw(window):
            run1 = True
           
        if Lord_exit.draw(window):
            game = False
        
    if run1 == True :
        window.blit(bt,(0,0))
        run2 = False
        if easy.draw(window):
            level = "easy"
            run1 = False
        if normale.draw(window):
            level = "normale"
            run1 = False
        if hurd.draw(window):
            level = "hurd"
            run1 = False

    if run1 == False and run2 == False :
        window.blit(bg,(0,0))
        player.draw()
        player.move()
        zoombi.update()
        zoombi.draw()
        bullets.draw(window)
        bullets.update()
        mixer.init()
        mixer.music.load("musik.mp3")
        mixer.music.play()
        player.fire()

        text = font.render('Пропущено:'  + str(lifes),True, (255,255,255))
        window.blit(text,(20,20))



        for i in zoombis:
            for j in bullets:
                if i.rect.colliderect(j.rect):
                    i.kill()
                    #i.rect.x = -50


        #if level == "easy":
        #    lifes = 5
        #    patrons = 15

        if level == "easy":
            lifes = 5
            patrons = 150
            gold = 0
            if patrons == 0 :
                if gold <= 1 :
                    gold = gold - 10 
                    patrons += 150
                elif gold == 0 :
                    ran2 = True








        
            
    clock.tick(60)
    display.update()

