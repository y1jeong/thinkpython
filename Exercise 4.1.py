import turtle
import math

bob = turtle



def draw_arc(t, r, theta):
    arc_length= (theta/360)*2*(math.pi)*r 
    n = int(arc_length/3)+1
    step_angle = theta/n
    step_length = arc_length/n
    

    for i in range(int(arc_length/step_length)):   
        t.fd(step_length)
        t.lt(step_angle)

def mirror_arc(t, r, theta):
    arc_length= (theta/360)*2*(math.pi)*r 
    n = int(arc_length/3)+1
    step_angle = theta/n
    step_length = arc_length/n
    
    t.lt(theta+theta)
    
    for i in range(int(arc_length/step_length)):  
        t.rt(-step_angle) 
        t.fd(step_length)
        


def draw_petal(t, r, theta):
    draw_arc(t, r, theta)
    mirror_arc(t, r, theta)
    
    
draw_petal(bob, 100, 60)
turtle.mainloop()
    