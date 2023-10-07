import turtle
from random import randint, random

WIDTH = 800
HEIGHT = 480

def randomColor():
    #returns a random color
     rv = random()
     if rv < 0.2:
       return "black"
     elif rv < 0.5:
       return "red"
     elif rv < 0.8:
       return "yellow" 
     else:
       return "white"

def drawRectangle(x1, y1, x2, y2, t):
    #Draws a rectangle with the given corner points using a random color
    color = randomColor()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()

def mondrian(x1, y1, x2, y2, level, t):
    #Draws rectangle at level 0, other wise call itself recursively
    if level ==  0:
        drawRectangle(x1, y1, x2, y2, t)
        return
    #split at longer edge
    vertical = (x2 - x1) > (y2 - y1)
    #split at 0.2 - 0.8 ratio
    splitFactor = randint(2, 8) / 10
    if vertical:              
       mondrian(x1, y1, (x2 - x1) * splitFactor + x1, y2, level - 1, t)
       mondrian((x2 - x1) * splitFactor + x1, y1, x2, y2, level - 1, t)
    else:
       mondrian(x1, y1, x2, y1 + (y2 - y1) * splitFactor, level - 1, t)
       mondrian(x1, y1 + (y2 - y1)  * splitFactor, x2, y2, level - 1, t)

def main():
    # Create a window
    wn = turtle.Screen()
    wn.setworldcoordinates(0, 0, WIDTH+1, HEIGHT+1)
    t = turtle.Turtle()
    t.pensize(5)
    t.speed(0)
    t.hideturtle()

    # Draw the art
    level = randint(4, 7)
    print(level)
    mondrian(0, 0, WIDTH, HEIGHT, level, t)
    wn.exitonclick()

if __name__ == '__main__':
    main()
