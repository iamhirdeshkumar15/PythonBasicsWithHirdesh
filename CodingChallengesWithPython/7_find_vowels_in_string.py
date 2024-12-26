# Write a code to find vowel's in given string by user
input_val = input("Enter String: ").lower()  # Convert input to lowercase
vowels = ""
if "a" in input_val:
    vowels = vowels + "a"
if "e" in input_val:
    vowels = vowels + "e"
if "i" in input_val:
    vowels = vowels + "i"
if "o" in input_val:
    vowels = vowels + "o"
if "u" in input_val:
    vowels = vowels + "u"

print("Vowels in the string:", vowels)

# Using loop 
# Check for vowels in the input string
vowels1 = ""
for vowel in "aeiou":
    if vowel in input_val:
        vowels1 += vowel
        
print("Vowels in the string:", vowels1)