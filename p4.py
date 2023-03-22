import turtle

skk = turtle.Turtle()
for i in range(40):
    skk.right(90)
    skk.forward(5*(i+1))
    
skk.penup()
skk.forward(150)
skk.pendown()
for i in range(40):
    skk.right(90+i/15)
    skk.forward(5*(i+1))
turtle.done()