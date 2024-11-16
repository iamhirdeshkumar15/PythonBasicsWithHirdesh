# create a new file "practice.txt" using python.
# Add the following data in it:

# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java.

f = open("practice.txt","w")
data = f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

f.close()



with open("practice1.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")




###
# WAF that replace all Occurrences of "java" with "python" in above file.

with open("practice1.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice1.txt","w") as f:
    f.write(new_data)

def word_replace():

    with open("practice1.txt","r") as f:
        data = f.read()
    new_data = data.replace("Java","Python")
    print(new_data)

    with open("practice1.txt","w") as f:
        f.write(new_data)

###
# Search if the word  "learning" exists in the file or not

word = "learning"
with open("practice1.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
    


def check_for_word():
    word = "learning"
    with open("practice1.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")


check_for_word()


###
# WAF to find in which line of the files does the word "learning" occur first Print-1 if word not found.


def check_for_word():
    word = "learning"
    with open("practice1.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")

# check_for_word()

def check_for_line():
    word = "Python"
    data = True
    line_no = 1
    with open("practice1.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1

check_for_line()






# From a file containing numbers separated by comma, print the count of even numbers.

with open("practice1.txt","r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

count = 0
with open("practice1.txt","r") as f:
    data = f.read()
    num = data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1

print(count)

        