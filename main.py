from pygame import *
from button import Button

window = display.set_mode((700,700))
clock = time.Clock()
game = True

#class Sprite ()
btm1 = Button (150,150, 150,150,"стрілок.jpg")
btm2 = Button (400,400, 150,150,"стрілок.jpg")
run = False

while game :
    for e in event.get() :
        if e.type == QUIT :
            game = False
        if e.type == KEYDOWN :
            if e.key == K_ESCAPE:
                run = False
                
    if run == True:
        window.fill((255,255,255))
    else:
        window.fill((255,0,0))



        if btm1.draw(window):
            run = True
        if btm2.draw(window):
            game = False

    clock.tick(60)
    display.update()




