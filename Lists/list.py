import sys

list(range(10,0,-2))

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

#tess.forward(100)
alex.forward(100)
#color changes for both turtles as they are both pointing to the same source

#3
a = [1,2,3]
for i in a:
    print(i)
b = a[:] #Cloning list, aliasing is a = b
b[0] = 5
for q in b:
    print(q)
for r in a:
    print(r)

#4
this = ["I","am","not","a","crook"]
that = ["I","am","not","a","crook"]
print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))
#Explanation for this is that even though in the first print, it has same contents, they are still referring to different objects, now when we equate them - They are both referring to the same object

#6 Scalar_mult function
def scalar_mult(s,v):
    new_list = []
    for i in v:
        new_list.insert(i,s*i)
    return new_list
lista = [1,2,3]
mult_list = scalar_mult(2,lista)
for i in mult_list:
    print(i)

test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])







