# WAF to print the length of a list
def print_len(lst):
    print("Length of the list:", len(lst))

# Example lists
cities = ["Delhi", "Kolkata", "Punjab", "Noida", "Chennai", "Mumbai"]
heroes = ["Captain America", "Iron Man", "Thor", "Hulk", "Captain Marvel", "Shaktiman"]

# Function calls
print_len(cities)
print_len(heroes)

# WAF to print the elements of a list in a single line
def print_list(lst):
    for item in lst:
        print(item, end=" ")
    print()  # To add a new line after printing all items

# Function call
print_list(heroes)

# WAF to find the factorial of n
def calc_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n}:", fact)

# Function call
calc_fact(5)

# WAF to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83  # Assuming 1 USD = 83 INR
    print(f"{usd_val} USD = {inr_val} INR")

# Function call
converter(100)

# Recursive function to calculate the sum of the first n natural numbers
def calc_sum(n):
    if n == 0:
        return 0
    else:
        return n + calc_sum(n - 1)

# Function call
print("Sum of first 10 natural numbers:", calc_sum(10))

# Recursive function to print all elements in a list
def k_list(lst, idx=0):
    if idx == len(lst):  # Base case
        return
    else:
        print(lst[idx])
        k_list(lst, idx + 1)

# Function call
alpha = ["a", "b", "c", "d", "e", "f", "g"]
print("Elements of the list:")
k_list(alpha)
