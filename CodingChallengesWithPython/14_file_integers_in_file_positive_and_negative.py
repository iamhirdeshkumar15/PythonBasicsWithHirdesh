# Write a Python program that reads a text file containing a mix of words,
# including both positive and negative integers. 
# The program should identify all integer values in the file (ignoring any non-numeric words), 
# sum them up, and print the total. Ensure that the program handles negative numbers correctly.

total = 0
with open('CodingChallengesWithPython/13_find_integers_in_file_and_sum_it.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            # Check if the word is a valid integer (could be negative)
            if word.lstrip('-').isdigit():
                total = total + int(word)

print(total)
