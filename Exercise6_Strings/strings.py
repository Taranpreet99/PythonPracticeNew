from os import remove
import string

from test import test

#String functions
print("Python"[1])
print(len("wonderful"))
print("Mystery"[:4])
print("p" in "Pineapple")
print("pear" not in "Pineapple")
print("apple">"pineapple")
print("pineapple" < "Peach")

#prefix - suffix

prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u"+suffix)
    else:
        print(letter + suffix)

#function count letters
def count_letters(str,ltr):
    count = 0
    for char in str:
        if char == ltr:
            count += 1
    return count

print(count_letters("Taran","a"))

#remove punctutation in the text, count number of words and words that contains "e"

paragraph = "Being different doesnt imply inferior or superior to others, especially inferior, dont confuse being different with being lesser, different simply means different. A woman is not less than a man because she is a woman, a man is not more than a woman because he is a man, their differences are necessary because of their purposes."

#paragraph without punctutation
new_paragraph= [paragraph.translate(str.maketrans('','',string.punctuation))]

#Created an array of words from the given paragraph
para_array = new_paragraph[0].split()
count = 0
for i in para_array:
    if "e" in i:
        count += 1
print("Your text contains {0} words, of which {1} contain an 'e'".format(len(para_array),count))


#Multiplication table
num_array=[1,2,3,4,5,6,7,8,9,10,11,12]
print(" \t\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12")
print(":-------------------------------")
for i in range(1,13):
    print("")


#Reverse string
def reverse(some_string):
    return some_string [::-1]

print(reverse("Taran"))

#tests to check if code is working fine
test(reverse("happy") == "yppah")
test(reverse("Python") == "nohtyP")
test(reverse("") == "")
test(reverse("a") == "aa")

#Function to remove given letter from a string
def remove_letter(char,str):
    return str.replace(char,"")

print(remove_letter('a','Taran'))

#tests to verify remove_letter works fine
test(remove_letter("a","apple") == "pple")
test(remove_letter("a","banana") == "bnn")