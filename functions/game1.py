import pgzrun 
import random
WIDTH =  600
HEIGHT = 600
b1= Rect((10, 10),(50,50))
b2= Rect((300, 300),(75, 100))
music.play("m1")
def draw ():
    screen.clear()
    screen.draw.filled_rect(b1,'red')
    screen.draw.filled_rect(b2, 'blue')
    screen.draw.text("game", (300,10),
                    color="white", fontsize=50)
def move(box, axis, speed=1):
    if axis =='x':
        if box.x>WIDTH:
            box.x=0
        box.x+=speed
    if axis == 'y':
        if box.y> HEIGHT:
            box.y=0
        box.y+=speed
def update():
    print('running')
    move(b1, 'x',75)
    move(b2, 'y',50)

pgzrun.go()