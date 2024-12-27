# Write a code to check given password is valid or not.
password = input("Enter Password: ")
valid = False
if 6 <= len(password) <= 30:
    if 'A' <= password[0] <= 'Z':
        if not ('/' in password or '=' in password or "'" in password or '\"' in password or ' ' in password):
            valid = True
print(valid)