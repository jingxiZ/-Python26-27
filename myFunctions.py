import turtle
bob = turtle.Turtle()

def halfCircle():
    for times in range(200):
        bob.right(1)
        bob.forward(1)

def heart(p):
    bob.fillcolor(p)
    bob.begin_fill()
    bob.left(140)
    bob.forward(113)
    halfCircle()
    bob.left(120)
    halfCircle()
    bob.forward(112)
    bob.end_fill()
    bob.right(220)

def heartShape():
    bob.pencolor("white")
    bob.left(140)
    bob.forward(113)
    halfCircle()
    bob.left(120)
    halfCircle()
    bob.forward(112)
    bob.right(220)


def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def bg(c):
    bob.fillcolor(c)
    bob.begin_fill()
    for times in range(2):
        bob.forward(800)
        bob.right(90)
        bob.forward(50)
        bob.right(90)
    bob.end_fill()

def dot(si,k):
    bob.fillcolor(k)
    bob.begin_fill()
    bob.circle(si)
    bob.end_fill()
    
