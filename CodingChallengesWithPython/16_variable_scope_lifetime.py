# Write a code scoping and lifetime of variable in python.

glob = "Hi I am GLOBALLY available."
def func1():
    """
    Testing Scope & Lifetime of a Variable
    """
    local = "Hi I am LOCALLY available."
    print(local)
    print(glob)
func1()
print(glob)
print(local) # NameError 