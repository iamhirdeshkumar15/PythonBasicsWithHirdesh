# Explain the difference in memory usage between generating a list using creater() 
# and using a generator with yield in creater1().
# How does next() work with the generator?

import sys

# Simple Method Using List
def creater():
    list = []
    i = 1
    while i <= 200:
        list.append(i)
        i += 1
    return list

# Print generated list and check memory size
created_list = creater()
print(created_list)
z = sys.getsizeof(created_list)  # Check the size of the generated list
print(f"Size of list: {z} bytes")

# Adding 10 to every number in the list
print([num + 10 for num in created_list])

# Using the range function to generate numbers
numbers = list(range(1, 201))
print(numbers)

# Using Yield Function to create a generator
def creater1():
    i = 1
    while i <= 200:
        yield i  # Pauses and yields the current value, resuming on next call
        i += 1

# Print generator object
generator_object = creater1()
print(generator_object)  # Output: generator object
print(next(generator_object))  # First number generated
print(next(generator_object))  # Second number generated
print(list(generator_object))  # Generate the remaining numbers and print the entire list
