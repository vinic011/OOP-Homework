import turtle

def draw_poly(t,n,sz):
    angle = 360/n
    for _ in range(n):
        t.forward(sz)
        t.right(angle)  

draw_poly(turtle.Turtle(),6,50)
        