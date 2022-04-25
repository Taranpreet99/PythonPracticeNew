import turtle

bg = turtle.Screen()
bg.bgcolor("White")

pen = turtle.Turtle()
pen.color("black")

for i in range(5):
    pen.forward(100)
    pen.right(144)


bg.mainloop()