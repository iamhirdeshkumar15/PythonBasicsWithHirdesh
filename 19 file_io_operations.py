# File I/O

f = open("file_name.txt","mode")


f = open("C:\Python VS\demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close


####
# Reading a file

# read()
f = open("C:\Python VS\demo.txt", "r")

data = f.read(5) 
print(data)
print(type(data))
f.close


###
# readline()
f = open("C:\Python VS\demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close


###
# Writing to a file

f = open("C:\Python VS\demo.txt","w")

f.write("I am new in Python.")

f.close()


f = open("C:\Python VS\demo.txt","a")

f.write("I am learning python.")
f.write("\nI am learning python.")

f.close()


# If file is not exits then it create a file
f = open("sample.txt","w")

f.write("This is Sample file which created by Hirdesh using File I/O write mode.")
f.close

 

f = open("C:\Python VS\demo.txt","a+")
f.write("abc")
print(f.read())
f.close()



# Deleting a file

import os

os.remove("C:\Python VS\demo.txt")