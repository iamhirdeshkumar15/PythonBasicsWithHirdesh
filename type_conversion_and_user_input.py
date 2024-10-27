# Type Conversion
a = 23                         # Initialize variable a with an integer value
b = 15.39                      # Initialize variable b with a float value
sum = a + b                    # Add a and b, Python will handle type conversion automatically
print("Sum of a and b:", sum)  # Print the result of the addition
print("Type of b:", type(b))   # Print the data type of variable b, which is a float

# Type Casting
x = "25"                       # Initialize x as a string representing an integer
print("Type of x before casting:", type(x))  # Print the type of x before conversion, which is str

c = int(x)                     # Cast x from a string to an integer and store it in c
print("Type of c after casting:", type(c))  # Print the type of c after conversion, which is int
sum1 = a + c                   # Add a and c, both are integers now
print("Sum of a and c:", sum1) # Print the result of the addition of a and c

f = 34                         # Initialize variable f with an integer value
g = str(f)                     # Cast f to a string and store it in g
print("Type of f:", type(f))   # Print the type of f, which is int
print("g as a string:", g)     # Print the string value of g
print("Type of g after casting:", type(g))  # Print the type of g after casting, which is str

# User Input and Data Type Conversion
name = input("Enter Name: ")   # Prompt the user to enter their name and store it in name
age = int(input("Enter Age: "))  # Prompt the user to enter their age, cast it to int, and store in age
marks = float(input("Enter Marks: "))  # Prompt the user to enter marks, cast to float, and store in marks
print("Welcome", name)         # Greet the user by their name
print("Age:", age)             # Print the user's age
print("Marks:", marks)         # Print the user's marks
