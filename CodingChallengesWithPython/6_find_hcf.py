# Question: Write a code to find HCF of two numbers.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
while num2 != 0:
    num1, num2 = num2, num1 % num2
    
print(num1)