# Checking age eligibility for voting and license
age = 24
if age >= 18:
    print("Can Vote & apply For License")
else:
    print("Cannot Vote")

# Traffic light instructions
light = "yellow"
if light == "red":
    print("STOP")
elif light == "green":
    print("GO")
elif light == "yellow":
    print("LOOK")
else:
    print("Light is Broken")

# Number comparison with separate if statements
num = 5
if num > 3:
    print("greater than 3")
if num > 2:
    print("greater than 2")

# Student grade calculation with input validation
try:
    marks = int(input("Enter Student Marks (0-100): "))
    if 0 <= marks <= 100:
        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        else:
            grade = "D"
        print("Grade of the Student ->", grade)
    else:
        print("Please enter marks between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter an integer.")

# Driving eligibility check with nested conditions
age = 18
if age >= 18:
    if age >= 80:
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")
