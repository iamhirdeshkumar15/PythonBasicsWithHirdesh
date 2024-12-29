# Write a code to find all integer values from a file and calculate their sum.

total = 0
with open('13_find_integers_in_file_and_sum_it.txt','r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word.isdigit():
                total = total + int(word)
print(total)