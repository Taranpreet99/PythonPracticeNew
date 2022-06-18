filename = input("SomeFile")
try:
    f = open(filename, "r")
except:
    print("There is no file named",filename)

def exists(filename):
    try:
        f =open(filename)
        f.close()
        return True
    except:
        return False

def get_age():
    age = int(input("Please enter your age"))
    if age < 0:
        #Create a new instance of an exception
        my_error = ValueError("{0} is not a valid age".format(age))
        raise my_error
    return age

from tkinter import N
import turtle, time
from typing import final

def show_poly():
    try:
        win = turtle.Screen()
        tess = turtle.Turtle()

        n= int(input("How many sides do you want in your polygon?"))
        angle = 360/n
        for i in range(n):
            tess.forward(10)
            tess.left(angle)
        time.sleep(3) #Make programs wait a few seconds
    finally:
        win.bye()

show_poly()
