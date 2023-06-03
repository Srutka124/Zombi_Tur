from pygame import *

class Button(sprite.Sprite):
    def __init__(self , x,y ,w ,h , imagename ):
        self.image = transform.scale(image.load(imagename),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.kliked = False
    def draw (self,window):
        astion =False
        poss = mouse.get_pos()
        if self.rect.collidepoint(poss):
            if mouse.get_pressed()[0] == 1 and self.kliked == False :
                self.kliked = True
                astion = True
        if mouse.get_pressed()[0] == 0:
            self.kliked = False
        window.blit(self.image,(self.rect.x ,self.rect.y))
        return astion
    




#class Recht ():
 #   def __init__(self , x,y ,w ,h , imagename ):
#        self.image = transform.scale(image.load(imagename),(w,h))
#        self.rect = self.image.get_rect()
#        self.rect.x = x
#        self.rect.y = y
#        def draw (self):
#            window.blit(self.image , (self.rect.x, self.rect.y))



                


