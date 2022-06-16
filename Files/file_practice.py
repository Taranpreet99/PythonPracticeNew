#first file
myfile = open("test.txt","w")
myfile.write("My first file written from Python\n")
myfile.write("-------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

#Reading from file
mynewhandle = open("test.txt","r")
while True:
    theline = mynewhandle.readline()
    if len(theline) == 0:
        break
    print(theline, end="")
mynewhandle.close()

#Turning a file into a list of lines
f = open("test.txt","r")
xs = f.readlines() #returns list of strings
f.close()

xs.sort()

g = open("sortedList.txt","w")
for v in xs:
    g.write(v)
g.close()

#copying binary file
f = open("somefile.zip","rb")
g = open("thecopy.zip","wb")

while True:
    buf = f.read(1024)
    if len(buf) == 0:
        break
    g.write(buf)

f.close()
g.close()

