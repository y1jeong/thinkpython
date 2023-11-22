import turtle
import math

bob = turtle
bob.speed = 300


def draw_arc(t, r, theta):
    arc_length= (theta/360)*2*(math.pi)*r 
    n = int(arc_length/3)+1
    step_angle = theta/n
    step_length = arc_length/n
    

    for i in range(int(arc_length/step_length)):   
        t.fd(step_length)
        t.lt(step_angle)


def draw_petal(t, r, seg):
    
    theta = 360/seg
    
    arc_length= (theta/360)*2*(math.pi)*r 
    n = int(arc_length/3)+1

    for i in range(seg):
        draw_arc(t, r, theta)
        t.lt((180-theta))
        draw_arc(t, r, theta)    
        t.lt(theta)
    
    turtle.done
 
draw_petal(bob, 200, 6)
