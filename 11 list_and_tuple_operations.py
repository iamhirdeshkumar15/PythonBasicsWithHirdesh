marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.1


marks = [94.4, 87.5, 95.2, .4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

student = ["Sami", 95, "Nepal"]
print(student)
print(student[0])
student[0] = "Hirdesh"
print(student)


# String -> immutable (do not Change)
# List -> mutable (Change)

# List Slicing
marks = [85,94,76,63,48]
print(marks[1:4])
print(marks[1:])
print(marks[:4])
print(marks[-3:-1])


##########################################
#List Methods

list = [2, 1, 3]
list.append(4)
print(list)

print(list.sort())
print(list)

print(list.sort(reverse=True))
print(list)

print(list.reverse())
print(list)

print(list.insert(2, 9))
print(list)

list1 = ["banana","litchi","apple"]
print(list1)
print(list1.sort())
print(list1)


list2 = [2, 1, 3, 1]
list2.remove(1)
print(list2)

list2.pop(2)
print(list2)


#########################
#Tuples

tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])
print(tup[1])
# tup[0]=5 # Error

tup1 = (1,)

print(tup1)
print(type(tup1))
print(tup[1:3])

tup = (2, 1, 3, 1, 2, 2)
print(tup.index(2))
print(tup.count(2))