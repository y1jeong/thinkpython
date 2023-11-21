import turtle
import math

bob = turtle.Turtle()

def circle(t, r):
    circumference = 2 * math.pi * r
    num_steps = 360
    length = circumference / num_steps
    angle = 360 / num_steps

    for i in range(num_steps):
        t.fd(length)
        t.lt(angle)

circle(bob, 100)
turtle.done()