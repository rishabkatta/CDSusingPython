import turtle
import math
import random


s = turtle.Screen()
s.screensize(5000, 5000)
s.title("forest at night")
s.bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
t.up()
t.backward(250)
t.down()
turtle.Screen().mainloop()
turtle.setworldcoordinates(-800, -800, 800, 800)


def draw_trunk(maxh):
    height = random.randint(50, maxh)
    t.left(90)
    t.pendown()
    t.forward(height)
    t.backward(height)
    t.right(90)
    t.penup()
    return height

def draw_polygon(sides):
    t.pendown()
    for i in range(sides):
        t.forward(50)
        t.left(360/sides)
    t.penup()
def draw_circle(radius):
    t.pendown()
    t.circle(radius)
    t.penup()

def gapbetweenthings():
    t.forward(100)

def draw_star():
    t.pendown()
    for _ in range(8):
        t.forward(20)
        t.backward(20)
        t.right(45)
    t.penup()


draw_star()























