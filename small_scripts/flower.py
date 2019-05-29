"""
Flawer drawn by the turtle.
"""

import turtle


def arc(my_turtle, r, angle):
    arc_length = 2 * 3.14159 * r * (angle/360)
    n = int(arc_length / 3) + 1
    step_length = arc_length/n
    step_angle = angle/n
    my_turtle.color('black', 'yellow')
    my_turtle.begin_fill()
    for i in range(n):
        my_turtle.fd(step_length)
        my_turtle.lt(step_angle)
    my_turtle.end_fill()

def petal(my_turtle, r, angle):
    for i in range(2):
        arc(my_turtle, r, angle)
        my_turtle.lt(180-angle)

def flower(my_turtle, n, r, angle):
    for i in range(n):
        petal(my_turtle, r, angle)
        my_turtle.lt(360.0/n)

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
flower(my_turtle, 10, 300, 45)
turtle.exitonclick()
# my_turtle.mainloop()
