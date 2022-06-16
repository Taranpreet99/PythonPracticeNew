#1 reads a file and write to new file in reversed order
myfile = open("new_file.txt","w")
myfile.write("Today is Friday\n")
myfile.write("It's beautiful day outside\n")
myfile.write("Brought pasta for lunch today. \n")
myfile.write("Adding snake to this line for testing.")
myfile.close()

mynewhandlge = open("new_file.txt","r")
xs = mynewhandlge.readlines()
mynewhandlge.close()

xs.sort(reverse= True)

g = open("reversed_file.txt","w")
for v in xs:
    g.write(v)
g.close

#2 read file and print only lines that have snake in it
handle2 = open("new_file.txt","r")
while True:
    theline = handle2.readline()
    if len(theline) == 0:
        break

    if "snake" in theline:
        print(theline)
handle2.close()

#3 Copy text from another file and Add numbers in front of the line
handle4 = open("file2.txt","w")
handle3 = open("new_file.txt","r")
while True:
    theline = handle3.readline()
    if len(theline) == 0:
        break
    handle4.write("1 2 3 4 {0}".format(theline))
handle3.close()
handle4.close()

handle5 = open("file2.txt","r")
while True:
    theline = handle5.readline()
    if len(theline) == 0:
        break
    print(theline)
