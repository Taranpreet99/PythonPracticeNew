import turtle

#window size
turtle.setup(400,500)
wn = turtle.Screen()
#window title, background color
wn.title("Handling Keypresses")
wn.bgcolor("lightgreen")
#Create turtle
tess = turtle.Turtle()


#Event handlers functions
def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)
def h4():
    wn.bye() #To close the window
#Functon to change color of the tess depending on the input
#lets choose, 0 - R, 1 - G, 2- B
def color_red():
    tess.color("Red")
def color_green():
    tess.color("Green")
def color_blue():
    tess.color("Blue")

#function to increase size of the tess
def increase():
    global tess
    if tess.pensize()<20:
        tess.pensize(tess.pensize()+1)

#function to decrease size of the tess
def decrease():
    global tess
    if tess.pensize()>1:
        tess.pensize(tess.pensize()-1)



#Events
wn.onkey(h1,"Up")
wn.onkey(h2,"Left")
wn.onkey(h3,"Right")
wn.onkey(h4,"q")
wn.onkey(color_red,"r")
wn.onkey(color_green,"g")
wn.onkey(color_blue,"b")
wn.onkey(increase,"+")
wn.onkey(decrease,"-")

#start listening for the events, without listen() method it won't notice keypress
wn.listen() 
wn.mainloop()


