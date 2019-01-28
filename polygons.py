'''
Created on 20-Sep-2018

@author: rishab katta
@author: akhil karrothu
'''
import turtle
import sys

'''
use "python polygons.py 8 FILL" for the maximum size of the polygon
'''

sidelength = 200
colors = ['lightgreen', 'green', 'purple', 'pink', 'blue', 'black', 'grey', 'yellow', 'violet', 'brown', 'orange',
              'red']



def init():
    '''
    :pre: relative pos(0,0), heading (east), up
    :post: relative pos(-250,0), heading(east), up
    :return: turtle and screen objects
    '''
    # Initializes and returns the turtle and screen objects, sets the world coordinates, writes author names
    s = turtle.Screen()
    s.screensize(500, 500)
    s.title("polygons")
    s.bgcolor("white")
    s.setworldcoordinates(-600, -600, 600, 600)
    t = turtle.Turtle()
    t.up()
    t.goto(-600, 600)
    t.write("A1: Rishab A2: Akhil", font=("Arial", 10, "normal"))
    t.goto(0, 0)
    t.backward(250)
    t.down()
    turtle.Screen().tracer(0, 0)
    return t, s


def draw_polygons_1(t, numberofsides, sidelength, isFill):
    '''
    :pre: relative pos(0,0), heading (east), up
    :post: relative pos(0,0), heading(east), up
    :return: total sum of sides in all of the polygons in figure
    '''
    # draws polygons of decreasing length recursively and returns the sum of sides of all the polygons drawn
    sumofsides = 0
    if numberofsides == 2:
        return sumofsides
    else:
        if (isFill == "fill"):
            t.fillcolor(colors[numberofsides])
            t.begin_fill()
        if isFill == "unfill":
            t.pencolor(colors[numberofsides])
            t.pensize(numberofsides - 2)
        for i in range(numberofsides):
            t.forward(sidelength)
            t.left(360 / numberofsides)
            sumofsides += sidelength
        if (isFill == "fill"):
            t.end_fill()
        for j in range(numberofsides):
            t.forward(sidelength)
            t.left(360 / numberofsides)
            sumofsides += draw_polygons_1(t,numberofsides - 1, sidelength / 2, isFill)
    return sumofsides


def draw_polygons_2(t,numberofsides, sidelength, isFill):
    '''
    :pre: relative pos(0,0), heading (east), up
    :post: relative pos(0,0), heading(east), up
    :return: total sum of sides in all of the polygons in figure
    '''
    # draws polygons of increasing length recursively and returns the sum of sides of all the polygons drawn
    # This polygon is drawn for the "intrestingness" part of the homework
    sumofsides = 0
    if numberofsides == 2:
        return sumofsides
    else:
        if isFill == "fill":
            t.fillcolor(colors[numberofsides])
            t.begin_fill()
        if isFill == "unfill":
            t.pencolor(colors[numberofsides])
            t.pensize(numberofsides - 2)
        for i in range(numberofsides):
            t.forward(sidelength)
            t.left(360 / numberofsides)
            sumofsides += sidelength
        if isFill == "fill":
            t.end_fill()
        for j in range(numberofsides):
            t.forward(sidelength)
            t.left(360 / numberofsides)
            sumofsides += draw_polygons_1(t,numberofsides - 1, sidelength * 1.5, isFill)
    return sumofsides


def main():
    '''
    :pre: relative pos(0,0), heading (east), up
    :post: relative pos(0,0), heading(east), up
    :return: total sum of sides in all of the polygons in figure
    '''
    # Main function calls init function for initializing the turtle and screen objects and draw_polygons function for
    # drawing all the polygons recursively.

    numberofsides = int(sys.argv[1])
    assert (numberofsides >= 3 and numberofsides <= 8), "number of sides must be in range 3-8"
    isFill = str(sys.argv[2])
    isFill = isFill.lower()
    t, s =init()
    print("sum of sides of polygon1 ", draw_polygons_1(t, numberofsides, sidelength, isFill))
    t.penup()
    t.forward(700)
    t.pendown()
    print("sum of sides of polygon2 ", draw_polygons_2(t, numberofsides, sidelength, isFill))

main()
turtle.Screen().mainloop()
