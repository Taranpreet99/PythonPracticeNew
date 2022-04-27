import turtle

bg = turtle.Screen()
bg.bgcolor("white")

tess = turtle.Turtle() 
tess.color("black")

values = [48, 117, 200, -240, 160, 260, 220] 


def draw_bar(t, height, width):
    if height >= 200:
        tess.color("Red")
    elif height >= 100 and height < 200:
        tess.color("Yellow")
    elif height < 100:
        tess.color("Green")

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.penup()
    t.forward(10) #small gaps
    t.pendown()
    t.end_fill()

for v in values:
    draw_bar(tess,v,40)

bg.mainloop()

