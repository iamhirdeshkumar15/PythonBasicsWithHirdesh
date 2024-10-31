# String Creation and Length Calculation
str1 = "This is a string.\nwe are creating it in python."
print(str1)  # Prints the string with a newline
print("Length of str1:", len(str1))  # Calculates the length of str1 including the newline character

# Concatenation and Length
str2 = 'Sam Loves Kumar.'
str3 = """Both Loves Biryaani"""
print("Length of str2:", len(str2))  # Length of str2
print("Length of str3:", len(str3))  # Length of str3
final_str = str2 + " " + str3  # Concatenates str2 and str3 with a space in between
print("Concatenated string:", final_str)  # Prints the concatenated string
print("Length of final_str:", len(final_str))  # Length of the concatenated string

# Indexing
ch = str2[0]  # Accesses the first character of str2
print("First character of str2:", ch)
print("Second character of str1:", str1[1])  # Accesses the second character of str1

# Slicing (Accessing parts of a String)
str5 = "Hirdesh Sam"
print("Slice from index 4 to end of str5:", str5[4:])  # Slices str5 from index 4 to the end
print("Slice from index 5 to 7 of str5:", str5[5:8])  # Slices str5 from index 5 to 7
print("Slice from beginning to index 5 of str5:", str5[:6])  # Slices str5 from the beginning to index 5

# Slicing with Negative Indexes
str4 = "Apple"
print("Slice from -3 to -1 of str4:", str4[-3:-1])  # Slices from the third-to-last to the second-to-last character
print("Slice from -5 to end of str4:", str4[-5:])  # Slices from the beginning to the end using negative indexes

# String Functions
str6 = "i am studying python from ApnaCollege"
str6 = str6.capitalize()  # Capitalizes the first character
print("Does str6 end with 'ge'? :", str6.endswith("ge"))  # Checks if str6 ends with "ge"
print("Capitalized str6:", str6)  # Prints the modified str6
print("Replace 'o' with 'a' in str6:", str6.replace("o", "a"))  # Replaces 'o' with 'a' in str6
print("Replace 'python' with 'javascript' in str6:", str6.replace("python", "javascript"))  # Replaces 'python' with 'javascript'
print("First occurrence of 'o' in str6:", str6.find("o"))  # Finds the first occurrence of 'o'
print("First occurrence of 'q' in str6:", str6.find("q"))  # Finds 'q' (not present, returns -1)
print("Count of 'a' in str6:", str6.count("a"))  # Counts occurrences of 'a'
print("Is str6 in uppercase?:", str6.isupper())  # Checks if str6 is in uppercase
