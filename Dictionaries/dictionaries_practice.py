#Empty dictionary
empty_dict = {}
empty_dict["First_element"] = "This is first element"
print(empty_dict["First_element"])

#Another way to create dictionary:
another_dict = {"first":"THis","second":"That"}

#Dictionary operation
del empty_dict["First_element"]

empty_dict["First_element"] = "This is now what it is "
print(empty_dict["First_element"])

#Dictionary Methods
#Keys
for k in empty_dict.keys():
    print(k)
#Values
a = empty_dict.values()
for i in a:
    print(i)
#Items
b = empty_dict.items()
for i in b:
    print(i)
#in and not in for keys
print("This" in empty_dict)

#Aliasing
alias = empty_dict
#Copying
copy = empty_dict.copy()

#Counting letters
letter_counts = {}
for letter in "Mississippi":
    letter_counts[letter] = letter_counts.get(letter,0) + 1


