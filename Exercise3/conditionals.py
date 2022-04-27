import math

#Find day of week
def day_of_week(a):
    if a == 0:
        print("It's sunday")
    elif a == 1:
        print("Monday")
    elif a == 2:
        print("Tuesday")
    elif a == 3:
        print("Wednesday")
    elif a == 4:
        print("Thursday")
    elif a == 5:
        print("Friday")
    elif a == 6:
        print("Saturday")
    else:
        print("Enter correct Day number")

day_of_week(1)

#find day of week using first day and duration 
def find_day_of_the_week(first_day, dur):
    duration = (dur + first_day) - 1
    a = duration % 7
    print(a)
    day_of_week(a)

find_day_of_the_week(1,7)


#grading system
def grade(g):
    if g >= 75:
        print("First")
    elif g>=70 and g < 75:
        print("Upper Second")
    elif g>=60 and g < 70:
        print("Second")
    elif g>=50 and g < 60:
        print("Third")
    elif g >= 45 and g < 50:
        print("F1 Supp")
    elif g>= 40 and g < 45:
        print("F2")
    elif g < 40:
        print("F3")

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    grade(i)
    
#find hyptoenuse from the two sides of Right anled triangle
def find_hypot(l,w):
    sq = (l*l)+(w*w)
    h = math.sqrt(sq)
    print(h)

find_hypot(3,4)

#is it right angles triangle
def is_right_angled(a,b,c):
    arr = [a,b,c]
    for i in arr:
        if a > b and a > c:
            h = a
            l = b
            w = c
        elif b > a and b > c:
            h = b
            l = a
            w = c
        elif c > a and c > b:
            h = c
            l = a
            w = b
        else:
            h = a
            l = b
            w = c
            
    if h*h == (l*l)+(w*w):
        print("This is right angled triangle")
    else:
        print("This is not right angled triangle")

is_right_angled(5,5,4)

