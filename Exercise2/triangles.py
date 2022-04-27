import turtle

bg = turtle.Screen()
bg.bgcolor("white")

pen = turtle.Turtle()
pen.color("black")

def draw_triangle():
    for i in range(5):
        pen.forward(100)
        pen.right(144)

def move():
    pen.penup()
    pen.forward(350)
    pen.pendown()
    pen.right(144)


for i in range(5):
    draw_triangle()
    move()


bg.mainloop()