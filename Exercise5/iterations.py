#iterations practice

import math 


#Function to count odd numbers in a list
from lib2to3.pgen2.token import EQUAL

a = [1,2,3,4,5,6]


def find_odd_numbers(list):
    count = 0
    for i in list:
        if i%2 != 0:
            count = count + 1
    return count

print(find_odd_numbers(a))

#sum of all the even numbers in the list 

def sum_all_even_num(list):
    sum = 0
    for i in list:
        if i%2 == 0:
            sum = sum + i
    return sum

print (sum_all_even_num(a))

#sum of all negative numbers in a list
def sum_all_negative_Num(list):
    sum = 0 
    for i in list:
        if i < 0:
            sum = sum + i
    return sum

#count words with lenght > 5
def words_length_five(list):
    count = 0
    for i in list:
        if len(i) == 5:
            count = count +1
    return count

#sum of all elements but not including first even number
def sum_except_first_even(list):
    sum = 0
    count = 0
    for i in list:
        if i%2 == 0 and count == 0:
            count = 1
        elif i%2 == 0 and count != 0:
            sum = sum + i
        else:
            sum = sum + i
    return sum


print(sum_except_first_even(a))

#count words until Sam(including sam) occurs
def count_words_sam(list):
    count = 0
    total_words = 0
    for i in list:
        if count == 0:
            if i == "sam":
                count = count + 1
                total_words = total_words + 1
            else:
                total_words = total_words + 1
    return total_words

c = ["Taran","Singh","sam","kida","Sohneyo","sam"]
print(count_words_sam(c))

#Newton's sqrt function
def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
       # print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better
    return approx

print(sqrt(25))

#print triangualr numbers
def print_triangular_numbers(n):
    b=0
    for i in range(n):
        a=i+1
        b= b + a
        print(a,"\t",b)

print_triangular_numbers(5)

#Check if number is prime or no
def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
        else:
            return True

print(is_prime(3))

