# WAP to ask user to enter names of their 3 favorite movies & store them in a list.

movies = []

mov1 = input("Enter Movies 1: ")
mov2 = input("Enter Movies 2: ")
mov3 = input("Enter Movies 3: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
# #####################################
movie = []

# # number of elements as input
num = int(input("Enter a number how many names of their favorite movies you enter: "))

for i in range(0, num): # iterating till the range
    mov = input("enter names of their favorite movies: ")
    movie.append(mov) # adding the element

print(movie)
#####################################

movies = []

mov = input("Enter Movies 1: ")
movies.append(mov)
mov = input("Enter Movies 2: ")
movies.append(mov)
mov = input("Enter Movies 3: ")
movies.append(mov)

print(movies)


#####################################
movies = []
movies.append(input("Enter Movies 1: "))
movies.append(input("Enter Movies 2: "))
movies.append(input("Enter Movies 3: "))

print(movies)

# WAP to check list contains a palindrome of elements.(Hint: use copy() method)

# list1 = [1, 2, 1]
list1 = ["ma'am"]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome ", list1)
else:
    print("Not Palindrome ", list1)

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome ", list2)
else:
    print("Not Palindrome ", list2)

#################################################

# WAP to count the number of students with the Grade "A" in the following tuple.

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))


# WAP to Store the above values in a list & sort them from "A" to "D".

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
