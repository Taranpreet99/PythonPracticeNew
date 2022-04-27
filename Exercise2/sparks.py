import turtle

bg = turtle.Screen()
bg.bgcolor("White")

pen = turtle.Turtle()

number = 5
for i in range(25):
    for n in range(4):
        pen.forward(number)
        pen.left(90)
        number = number + 5
    pen.right(1)

bg.mainloop()