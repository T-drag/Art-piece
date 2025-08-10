import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Art: Spiral and Initials T & D")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# List of bright colors
colors = ["red", "orange", "yellow", "lime", "cyan", "blue", "magenta"]

def draw_spiral_squares():
    """
    Draws a spiral of rotated colorful squares.
    """
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for i in range(120):
        pen.color(random.choice(colors))
        pen.forward(i * 2)
        pen.left(91)

def draw_initial_T(x, y):
    """
    Draws a capital 'T' using turtle movement at a given location. Initial for Tudor.
    """
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color("white")
    pen.forward(40)
    pen.backward(20)
    pen.right(90)
    pen.forward(60)

def draw_initial_D(x, y):
    """
    Draws a capital 'D' with a straight vertical bar and curved outer line. Initial for Dragusanu.
    """
    pen.penup()
    pen.goto(x, y)
    pen.setheading(90)
    pen.pendown()
    pen.color("white")
    pen.forward(60)
    pen.right(90)
    
    for _ in range(18):
        pen.forward(5)
        pen.right(10)

# Draw central square spiral
draw_spiral_squares()

# Draw initials centered under the spiral
draw_initial_T(-40, -30)   # T on the left
draw_initial_D(10, -30)    # D on the right

# Finish
pen.hideturtle()
turtle.done()
