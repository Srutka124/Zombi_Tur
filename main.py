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
bkrnd_Mony = image.load('Mony.png')
#bkrnd_Mon = transform.scale(bkrnd_Mony, (50,50))
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
        self._pressed = False
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
        bullet = Bulet(50,50,self.rect.centerx,self.rect.top,'bullet.png',7 )
        keys = key.get_pressed()
        
        if mouse.get_pressed()[0]==1 and self._pressed==False:
            global patrons
            patrons = patrons - 1
            bullets.add(bullet)
            self._pressed =True

        if mouse.get_pressed()[0]==0:
            self._pressed = False
    def bombe (self):
        bomb = Bomb (400,500 , 300 , [bf1, bf2,bf3])
        bombs.add(bomb)


        



bf1 = transform.scale(image.load("fire_1.png"),(50,50))
bf2 = transform.scale(image.load("fire_2.png"),(50,50))
bf3 = transform.scale(image.load("fire_3.png"),(50,50))
class Bulet(Sprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y <= 0 :
            self.kill()
        if self.rect.y <= 10 :
            self.kill()

class Bomb(sprite.Sprite):
    def __init__ (self , x ,y , radius , image_list):
        super().__init__()
        self.image = image_list[0]
        self.rect = self.image.get_rect()
        self.frame = len(image_list) - 1 
        self.image_list = image_list
        self.rect.x = x
        self.rect.y = y
        self.count = 5 
        self.time = 10
    def update(self):
        if self.count == 0:
            self.count = 5
            self.image = self.image_list[self.frame]
            self.frame -= 1 
            
            if self.frame < 0 :
                self.frame = len(self.image_list) - 1 
            
        else : 
            self.count -= 1 
        window.blit(self.image , (self.rect.x ,self.rect.y))
        if self.time == 0 :
            self.kill()
        else : 
            self.time -= 1
            window.blit(self.image , (self.rect.x ,self.rect.y))
    def mowe (self):
        keys = key.get_pressed()
        if keys[K_1]: 
            self.rect.y = 530
        if keys[K_2]:
            self.rect.y = 200
        if keys[K_3]:
            self.rect.y = 100
        if keys[K_4]:
            self.rect.y = 300
        

class Enemy (Sprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        global lifes
        global record
        if self.rect.y >= 650 :
            lifes -= 1
            self.rect.y = 0
        a = randint(1,4)
        if a == 1 :
            self.rect.x = 650

        elif a == 2 :
            self.rect.x = 100
        elif a == 3 :
            self.rect.x = 255
        elif a == 4 :
            self.rect.x = 445
        if record >= 10000:
            self.speed = randint(2,3)
            record = record +  1
        elif record >=20000 :
            self.speed = randint(2,6)
            record = record + 1
        elif record >= 300000 :
            self.speed = randint(3,10)
            record = record + 1
        elif record <= 300000 :
            self.speed = randint(5,10)
            record = record + 1 
    def recet(self):
        self.rect.y = -100 
        
       
        #if  self.rect.y == 530:
        #    lifes = lifes - 1
        #def cill() :






bombs = sprite.Group()

bullets = sprite.Group()


zoombis = sprite.Group()

for i in range(1,6):
    zoombi = Enemy(100,50,100,50,'zoombi.png',1)
    zoombis.add(zoombi)
    #zoombi = Enemy(100,255,100,100,'zoombi.png',1)
    #zoombis.add(zoombi)
    #zoombi = Enemy(100,445,100,100,'zoombi.png',1)
    #zoombis.add(zoombi)
    #zoombi = Enemy(100,650,100,100,'zoombi.png',1)
    #zoombis.add(zoombi)
bh = transform.scale(image.load("Herd.png"),(50,50))
bb = transform.scale(image.load("bullet.png"),(50,50))
bm = transform.scale(image.load("Mony.png"),(50,50))
bg = transform.scale(image.load("cona.png"),(700,700))
bt = transform.scale(image.load("fon.jpg"),(700,700))
player = Player (300,300,400 , 530,  "player.png" , 40)
start = Button (250,150, 200,150,"start.png")
Lord_exit = Button (250,350, 200,150,"stop.png")
exit = Button (590,560, 100,40,"start.png")
pausa = Button (590,0, 100,40,"stop.png")
easy = Button (100,200, 150,90,"easys.png")
normale = Button (450,270, 150,90,"normal.png")
hurd = Button (100,350, 150,90,"hard.png")
#bomb = Bomb (400,500 , 100 , [bf1, bf2,bf3])
run1 = False
run2 = True
mixer.init()
mixer.music.load("musik.mp3")
mixer.music.play()
lifes = 10
record = 0
patrons = 150
gold = 0
bom = 0
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
            lifes = 10
            patrons = 150
            gold = 0
        if normale.draw(window):
            level = "normale"
            run1 = False
            lifes = 7
            patrons = 125
            gold =  0
        if hurd.draw(window):
            level = "hurd"
            run1 = False
            lifes = 5
            patrons = 100
            gold = 0

    if run1 == False and run2 == False :
        window.blit(bg,(0,0))
        player.draw()
        player.move()
        zoombis.update()
        zoombis.draw(window)


        
        bullets.draw(window)
        bullets.update()
        bombs.update()
        bombs.mowe()

        mixer.init()
        window.blit(bh,(20,0))
        player.fire()
        player.bombe()
        text = font.render(''  + str(lifes),True, (255,255,255))
        window.blit(text,(40,0))



        window.blit(bb,(20,50))
        text = font.render(''  + str(patrons),True, (255,255,255))
        window.blit(text,(40,50))


        window.blit(bm,(20,100))
        text = font.render(''  + str(gold),True, (255,255,255))
        window.blit(text,(40,100))

        text = font.render('Живу'  + str(record),True, (255,255,255))
        window.blit(text,(20,150))



        for i in sprite.groupcollide(zoombis,bullets,True,True):
            zoombi = Enemy(100,50,50,50,'zoombi.png',1)
            zoombis.add(zoombi)
            gold = gold + 1 
        for e in sprite.groupcollide(zoombis,bombs,True,True):
            zoombi = Enemy(100,50,50,50,'zoombi.png',1)
            zoombis.add(zoombi)
            gold = gold + 1 
        


        #if level == "easy":
        #    lifes = 5
        #    patrons = 15

        if level == "easy":
            

            if patrons == 0 :
                if gold >= 100 :
                    gold = gold - 100 
                    patrons += 150
                elif gold <= 0 :
                    ran2 = True
            

        if lifes <= 0 :
            for i in zoombis :
                i.recet()
                print()
            
            run2 = True
    

    








        
    record += 1       
    clock.tick(60)
    display.update()

