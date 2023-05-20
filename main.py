from pygame import *
from button import Button

window = display.set_mode((700,600))
clock = time.Clock()
bkrnd_img = image.load('tur.png')
bkrnd = transform.scale(bkrnd_img, (700,500))
game = True

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
            self.rect.x = 50 
        if keys[K_s]:
            self.rect.x = 150
        if keys[K_d]:
            self.rect.x = 300
        if keys[K_f]:
            self.rect.x = 450


    def fire(self):
        bullet = Bulet(15,20,self.rect.centerx,self.rect.top,'bullet.png',3 )
        bullets.add(bullet)

class Bulet(Sprite):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y <= 0 :
            self.kill()

bullets = sprite.Group()




player = Player (100,50,50 , 400,  "player.png" , 40)
start = Button (250,150, 150,90,"start.png")
Lord_exit = Button (250,250, 150,90,"стрілок.jpg")
exit = Button (590,560, 100,40,"стрілок.jpg")
pausa = Button (590,0, 100,40,"stop.png")
eses = Button (250,150, 150,90,"стрілок.jpg")
normale = Button (250,250, 150,90,"стрілок.jpg")
hurd = Button (250,350, 150,90,"стрілок.jpg")
run1 = False
run2 = True

lifes = 3
shoted = 0
patrons = 0
level = ""
while game :
    for e in event.get() :
        if e.type == QUIT :
            game = False
        if e.type == KEYDOWN :
            if e.key == K_ESCAPE:
                run2 = not run2 
                
    if run2 == True:
        window.fill((255,0,0))



        if start.draw(window):
            run1 = True
           
        if Lord_exit.draw(window):
            game = False
        
            

    print (run1,run2)
    if run1 == True :
        run2 = False
        if eses.draw(window):
            level = "easy"
            run1 = False

        if normale.draw(window):
            level = "normale"
            run1 = False

        if hurd.draw(window):
            level = "hurd"
            run1 = False
    if run1 == False and run2 == False :
        window.fill((255,0,0))
        player.draw()

        #if level == "easy" :

            


        
    clock.tick(60)
    display.update()




