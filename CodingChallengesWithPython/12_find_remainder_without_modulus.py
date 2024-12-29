# Write a code find the remainder without using "%" operator.

# Write a program to find Remainder when a positive number X  is divided with a positive number Y.
# You are allowed to use only +,&,-,symbol.
# Use of /,// or % is Prohibited.

def rem(X,Y):
    if X < Y:
        return X
    return rem(X - Y, Y)

X = int(input("Enter Number: "))
Y = int(input("Enter Number: "))
print(rem(X,Y))