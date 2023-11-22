import turtle
import math

bob = turtle
bob.speed = 100


def draw_pies(f, r, n):
    k = 360/n
    theta=(180-k)/2
    
    for i in range(n):
        f.fd(r)
        f.lt(180-theta)
        f.fd(2 * r * math.sin(math.radians(k) / 2))
        f.lt(180-theta)
        f.fd(r)
        f.lt(180)
        

    turtle.done()
    
draw_pies(bob, 50, 5)
    
    