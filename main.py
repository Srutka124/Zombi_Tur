from pygame import *
from button import Button
from time import sleep
from random import *
window = display.set_mode((700,700))
clock = time.Clock()
bkrnd_img = image.load('cona.png')
bkrnd = transform.scale(bkrnd_img, (700,700))
game = True
record = 0

class Sprite(sprite.Sprite):
    def __init__(self, h , w , x ,y , image_name, speed ):
        super().__init__()
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

class Bulet(Sprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y <= 0 :
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
            if a == 2 :
                self.rect.x = 50
            if a == 3 :
                self.rect.x = 255
            if a == 4 :
                self.rect.x = 445
            if record >=10:
                self.speed = randint(1,3)
            elif record >=20 :
                self.speed = randint(2,6)
            elif record >= 30 :
              self.speed = randint(3,10)
            elif record <= 30 :
              self.speed = randint(5,10)
        if  self.rect.y == 530:
            lifes = lifes - 1
    def kill()  :
        
bullets = sprite.Group()

zoombi = sprite.Group()

for i in range(1,6):
    zoombi = Enemy(300,300,-70,50,'zoombi.png',50)


bg = transform.scale(image.load("cona.png"),(700,700))

player = Player (300,300,400 , 530,  "player.png" , 40)
start = Button (250,150, 200,150,"start.png")
Lord_exit = Button (250,350, 200,150,"start.png")
exit = Button (590,560, 100,40,"start.png")
pausa = Button (590,0, 100,40,"stop.png")
easy = Button (0,300, 150,90,"start.png")
normale = Button (250,300, 150,90,"start.png")
hurd = Button (550,300, 150,90,"start.png")
run1 = False
run2 = True
mixer.init()
mixer.music.load("musik.mp3")
mixer.music.play()
lifes = 3
record = 0
patrons = 0
level = ""
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
        window.fill((255,0,0))



        if start.draw(window):
            run1 = True
           
        if Lord_exit.draw(window):
            game = False
        
    if run1 == True :
        window.fill((255,0,0))
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

        if level == "easy":
            lifes = 5



        
        if lifes == 0:
            game = True
        
        if  lifes == 2 :
            color = (0,255,0)
        elif lifes == 1 :
            color = (255,255,0)
        else:
            color = (255,0,0)


        text = font.player(str(lifes), True , color)
    else :
        finish = False
        shoted = 0 
        lpost = 0 
        lifes = 3
        for b in bullets :
            b.kill()
 #       for m in zoombi :
 #           m.kill()
        for i in range(1,6):
            zoombi = Enemy(50,50,-70,50,'zoombi.png',50)


            



    clock.tick(60)
    display.update()




