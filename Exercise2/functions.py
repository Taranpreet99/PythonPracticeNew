import turtle


def draw_square(t,n):
    for i in range(4):
        t.forward(n)
        t.left(90)
    print(t.position())


bg = turtle.Screen()
bg.bgcolor("White")

alex = turtle.Turtle()

for i in range(5):
    draw_square(alex, 20)


#sum of all integers starting from 1 up to the number mentioned in function
def sum_to(n):
    a = 0
    for i in range(n):
        a = a + (i+1)
    return a

print(sum_to(10))

# area of a circle function

def area_of_circle(r):
    return ((3.14)*r*r)

print(area_of_circle(5)) 

bg.mainloop()
