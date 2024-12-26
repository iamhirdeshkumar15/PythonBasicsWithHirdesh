# Write a code to check if a string is a palindrome or not

n = input()
rev = ''
for char in n:
    rev = char + rev
if n == rev:
    print("Yes, String is Palindrome.")
else:
    print("No, String is Not Palindrome.")
