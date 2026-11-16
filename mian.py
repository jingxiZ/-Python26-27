from myFunctions import *
from random import *
turtle.colormode(255)
bob.speed(0)

for times in range(26):
    jump(-400,300 - times*20)
    bob.pencolor("red")
    u = (255 - times*5,0,times)
    bg(u)
    

for times in range(10):
    x = randint(-300,300)
    y = randint(-300,130)
    jump(x,y)
    r = randint(170,255)
    p = (r,0,0)
    bob.pencolor("red")
    w = randint(1,5)
    bob.width(w)
    heart(p)

for times in range(40):
    x = randint(-500,500)
    y = randint(-500,500)
    jump(x,y)
    si = randint(1,10)
    bob.pencolor("white")
    dot(si,"white")

for times in range(3):
    x = randint(-370,370)
    y = randint(-100,100)
    jump(x,y)
    w = randint(1,10)
    bob.width(w)
    heartShape()

for times in range(5):
    x = randint(-400,400)
    y = randint(-400,400)
    jump(x,y)
    bob.pencolor("white")
    s = randint(50,80)
    w = randint(1,5)
    bob.width(w)
    bob.circle(s)
