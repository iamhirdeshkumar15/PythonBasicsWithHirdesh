# Write code for Iterative() vs Recursive().

# iterative()
def iterative(n):
    total = 0
    for i in range (n):
        total = total + 2 ** i 
    return total
n = int(input("Enter Number: "))
print(iterative(n))


# recursive()
def recursive(n):
    if n == 1:
        return 1
    return 2 ** (n-1) + recursive (n-1)
n = int(input("Enter Number: "))
print(recursive(n))