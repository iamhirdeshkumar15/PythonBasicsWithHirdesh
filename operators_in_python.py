# Arithmetic Operators
a = 5
b = 2

print(a + b)   # Addition: 7
print(a - b)   # Subtraction: 3
print(a * b)   # Multiplication: 10
print(a / b)   # Division: 2.5
print(a % b)   # Modulus (Remainder): 1
print(a ** b)  # Power: 5 raised to 2

# Relational / Comparison Operators
d = 50
c = 20

print(c == d)  # Checks if c is equal to d (False)
print(c != d)  # Checks if c is not equal to d (True)
print(c >= d)  # Checks if c is greater than or equal to d (False)
print(c > d)   # Checks if c is greater than d (False)
print(c <= d)  # Checks if c is less than or equal to d (True)
print(c < d)   # Checks if c is less than d (True)

# Assignment Operators
num = 10

# Increment num by 10
num += 10
print("num:", num)  # Outputs 20

# Additional assignment operations
num += 10  # num = num + 10
num -= 10  # num = num - 10
num *= 10  # num = num * 10
num /= 10  # num = num / 10
num %= 10  # num = num % 10
num **= 10 # num = num ** 10

# Logical Operators
print(not False)    # Logical NOT of False (True)
print(not True)     # Logical NOT of True (False)

e = 50
f = 30

print(not (e > f))  # NOT of (e > f), evaluates to False
print(not (f > e))  # NOT of (f > e), evaluates to True

# AND and OR operations
val1 = True
val2 = False

print("and operator:", val1 and val2)     # Logical AND (False)
print("or operator:", val1 or val2)       # Logical OR (True)

print("and operator:", (e == f) and (e > f))  # AND of two expressions (False)
print("or operator:", (e == f) or (e > f))    # OR of two expressions (True)
