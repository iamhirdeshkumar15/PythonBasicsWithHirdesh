# Print Numbers from 1 to 100
print("Numbers from 1 to 100")
i = 1
while i <= 100:
    print(i)
    i += 1
print("Completed")

# Print Numbers from 100 to 1
print("Numbers from 100 to 1")
i = 100
while i >= 1:
    print(i)
    i -= 1
print("Completed")

# Print the multiplication table of a number n
n = int(input("Enter a number for its multiplication table: "))
i = 1
while i <= 10:
    print(n, "*", i, "=", n * i)
    i += 1

# Print the elements of a given list
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Elements of the list:")
for num in nums:
    print(num)

# Search for a number x in a tuple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to search in the tuple: "))
found = False
for i, val in enumerate(tup):
    if val == x:
        print(f"Number found at index {i}")
        found = True
if not found:
    print("Number not found in the tuple")

# Print numbers from 1 to 100 using for and range()
print("Numbers from 1 to 100 using for loop:")
for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1 using for and range()
print("Numbers from 100 to 1 using for loop:")
for j in range(100, 0, -1):
    print(j)

# Sum of first n natural numbers using while
n = 10
sum_n = 0
i = 1
while i <= n:
    sum_n += i
    i += 1
print(f"Sum of first {n} natural numbers is:", sum_n)

# Factorial of a number using while loop
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(f"Factorial of {num} using while loop is:", fact)

# Factorial of a number using for loop
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} using for loop is:", fact)
