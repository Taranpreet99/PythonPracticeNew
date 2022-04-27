import turtle 

#input from user - bgColor
#print("Please enter the background color")
col = input("Enter a color")


wn = turtle.Screen()
wn.bgcolor(col)
wn.title("Hello, Tess!")

alex = turtle.Turtle()
alex.color("blue")
alex.pensize(3)

alex.forward(50)
alex.left(120)
alex.forward(50)

wn.mainloop()

#push test 