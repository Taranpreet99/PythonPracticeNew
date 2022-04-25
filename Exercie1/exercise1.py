import turtle

#Print 1000 times
#for i in range(1000):
 #   print("we like Python's turtles")



#Print months
#for i in ["January","Feb","March","April"]:
    #print(i)


#use for loop to draw polygons
bg = turtle.Screen()
bg.bgcolor("white")


tess = turtle.Turtle()

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in angles:
    tess.left(i)
    tess.forward(100)

bg.mainloop() 


print(type(tess))


