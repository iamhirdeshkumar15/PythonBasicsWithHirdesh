# Infinite loop example
# Uncomment to test, as this will print "Hello" endlessly
# while True:
#     print("Hello")


# Example 1: Controlled iteration with a while loop
count = 1  # Iterator
while count <= 5:  # Iteration limit
    print("hello")
    count += 1
print("Final count:", count)


# Example 2: Print "hello" with incremental counter
i = 1  # Iterator
while i <= 5:  # Iteration limit
    print("hello", i)
    i += 1


# Example 3: Print numbers from 1 to 5
i = 1  # Iterator
while i <= 5:  # Iteration limit
    print(i)
    i += 1
print("Loop Ended")


# Example 4: Reverse counting from 5 to 1
i = 5  # Iterator
while i >= 1:  # Iteration limit
    print(i)
    i -= 1
print("Loop Ended")


#######################################################
# Break and Continue examples

# Example 5: Using Break in a loop
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("End of Loop")


# Example 6: Search for a number x in a tuple using a loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0  # Initialization
while i < len(tup):
    if tup[i] == x:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1
print("End of Loop")


# Example 7: Using Continue in a loop
i = 1
while i <= 10:
    if i == 3:
        i += 1
        continue  # Skip when i equals 3
    print(i)
    i += 1


# Example 8: Only print even numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue  # Skip odd numbers
    print(i)
    i += 1


# Example 9: Only print odd numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue  # Skip even numbers
    print(i)
    i += 1


##########################################
# For Loop examples

# Example 10: Loop through a list of numbers
nums = [1, 2, 3, 4, 6, 7, 8, 9]
for val in nums:
    print(val)


# Example 11: Loop through a list of vegetables
veggies = ["potato", "brinjal", "ladyfinger", "cucumber"]
for val in veggies:
    print(val)


# Example 12: Loop through a tuple of numbers
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for num in tup:
    print(num)
else:
    print("End")


# Example 13: Loop through a string
str_example = "Samiksha Yadav"
for char in str_example:
    print(char)
else:
    print("End")


# Example 14: Find a specific character in a string
str_example = "Samiksha Yadav"
for char in str_example:
    if char == 'h':
        print("h found")
        break
    print(char)
print("End")


################################################
# range() examples

# Example 15: Using range to print numbers
for i in range(5):
    print(i)

# Example 16: Specified range with step
for i in range(2, 10, 2):
    print(i)  # Prints even numbers from 2 to 8

# Example 17: Print all even numbers from 2 to 100
for i in range(2, 100, 2):
    print(i)

# Example 18: Print all odd numbers from 1 to 99
for i in range(1, 100, 2):
    print(i)


##############################
# Using pass in a loop and conditional statements

for i in range(10):
    pass  # Placeholder for future code

print("Some useful work after pass statement")

if i > 5:
    pass  # Placeholder in if-statement

print("Some useful work after conditional pass statement")
