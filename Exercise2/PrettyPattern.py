import turtle

bg = turtle.Screen()
bg.bgcolor("white")

pen = turtle.Turtle()
pen.color("black")

def draw_square():
    for i in range(4):
        pen.forward(100)
        pen.left(90)    

boxes = 20

for i in range(boxes):
    draw_square()
    pen.left(360/boxes)

draw_square()

bg.mainloop()