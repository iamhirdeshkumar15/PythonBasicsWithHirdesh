# Sum of two numbers
a = 5
b = 6
sum = a + b
print("Sum of a and b:", sum)

# Function to calculate sum of two numbers
def calc_sum(a, b):
    return a + b

# Function calls with arguments
print("Sum using function (2, 3):", calc_sum(2, 3))
print("Sum using function (15, 15):", calc_sum(15, 15))

# Function to print "hello"
def print_hello():
    print("hello")

# Function call
print_hello()

# Average of three numbers
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print("Average of three numbers:", avg)
    return avg

# Function call to calculate average
calc_avg(12, 5, 4)

# Recursive function to demonstrate decremental calls
def show(n):
    if n == 0:  # Base case
        return
    print(n)
    show(n - 1)

# Function call for recursion
print("Recursive countdown:")
show(5)

# Recursive function to calculate factorial
def fact(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * fact(n - 1)

# Function call to calculate factorial
print("Factorial of 5:", fact(5))
