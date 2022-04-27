import turtle

def draw_poly(t,n, sz):
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)


tess = turtle.Turtle()
tess.color("black")

background = turtle.Screen()
background.bgcolor("White")

#draw_poly(tess,8,50)

#void function that calls draw_poly to draw equilateral triangle

def draw_equitriangle(t, sz):
    draw_poly(t,3,sz)


draw_equitriangle(tess,100)

background.mainloop()