# Write a code for Sum of Sum of Natural Numbers.
# series 
# 1 + (1 + 2) + (1 + 2 + 3) + ........ + (1 + 2 + 3 + 4 + ...... + n ) is a sum of Sums of First n natural numbers.

n = int(input("Enter the number: "))
total = 0
for i in range (1, n + 1):
    for j in range (1, i + 1):
        total = total + j

print(total)