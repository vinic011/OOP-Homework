import turtle
skk = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Turtle")

for i in range(5):
    skk.pendown()
    for j in range(4):
        skk.forward(20*(i+1))
        skk.right(90)
    skk.penup()
    skk.forward(-10)
    skk.right(90)
    skk.forward(-10)
    skk.right(270)
    
turtle.done()
