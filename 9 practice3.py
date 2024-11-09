# WAP to check if a number entered by the user is even or odd.

num = int(input("Enter the Number to Check EVEN or ODD : "))

if(num % 2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")
####################################################

num = int(input("Enter the Number to Check EVEN or ODD : "))

rem = num % 2

if(rem == 0):
    print("Number is Even",num)
else:
    print("Number is Odd ",num)




#WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if(num1 >= num2 and num1 >= num3):
    print("Number1 is greater and number is ",num1)
elif(num2 >= num3 and num2 >= num1):
    print("Number2 is greater and number is ",num2)
else:
    print("Number3 is Greater and number is ",num3)



# WAP to check if a number is multiple of 7 or not.
num = int(input("Enter the number multiple of 7 : "))

if(num % 7 == 0):
    print("Multiple of 7 and number is ",num)
else:
    print("Not Multiple of 7 and number is ",num)

mul = int(input("Enter the multiple number : "))
num = int(input("Enter the number to check is multiple of given number : "))

if(num % mul == 0):
    print("Multiple of ",mul, "and number is ",num)
else:
    print("Not Multiple of ",mul, " and number is ",num)