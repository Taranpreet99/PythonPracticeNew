import turtle

#Heart

bg = turtle.Screen()
bg.bgcolor('black')

taran = turtle.Turtle()
taran.color('White')

def curve():
    for i in range(200):
        taran.right(1)
        taran.forward(1)
    
taran.fillcolor('White')
taran.begin_fill()
taran.left(140)
taran.forward(113)

curve()
taran.left(120)

curve()

taran.forward(112)
taran.end_fill()

taran.up()
taran.setpos(-105,-85)
taran.down()

taran.color('white')
taran.write("Kiddan Sohneyo?", font=("Verdana", 18, "bold"))

taran.ht()

bg.mainloop()
