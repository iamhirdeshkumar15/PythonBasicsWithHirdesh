info = {
    "key" : "value",
    "name" : "Sami",
    "learning" : "python_coding",
    "age" : 35,
    "is_adult" : True,
    "marks" : 94.4,
}
print(info)
print(type(info))

null_dict = {} # empty dictionary syntax 
print(null_dict)
print(type(null_dict))


info1 = {
    "name" : "apnaworld",
    "subjects" : ["python", "C", "Java"],
    "topics" : ("dict", "set"),
    "age" : 24,
    "is_adult" : True,
    "marks" : 94.4,
}

print(info1)
print(type(info1))
print(info["name"])
print(info["marks"])

info["name"] = "Kumar"
print(info)


############
#Nested Dictionary

student = {
    "name" : "kumar",
    "subjects" : {
        "chem" : 97,
        "phy" : 98,
        "math" : 95,
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(student.values())
print(student.items())
print(list(student.values()))

print(student.items())
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])
print(pairs[1])


print(student["name"]) 
# print(student["name2"])     # Error
print(student.get("name")) 
print(student.get("name2"))  #No Error -> None


print("hi")
print("welcome to")
print(student["name2"])
print("my world")
print("we are leatrning")
print("I Love My Attitude")


student.update({"city" : "delhi"})
print(student)
new_dict = {"city" : "delhi" , "age" : 21, "subjects" : {
    "english" : 89,
}}
student.update(new_dict)
print(student)


#################################################

#Set in Python

nums = {1, 2, 3, 4}
print(nums)
print(type(nums))
sets  = {1, 2, 2, 2}
print(sets)
print(type(sets))
# repeated elements stored only once, so it resolved to {1, 2}


collection = {1, 2, 3, 4, "Hello", "Kumar"}

print(collection)
print(type(collection))


collection1 = {1, 2, 2, 2, 3, 4, "Hello", "Kumar", 5}

print(collection1)
print(type(collection1))
print(len(collection1))


######### 

null_sets = set() # empty set syntax
print(null_sets)
print(type(null_sets ))


collection1 = set()
collection1.add(1)
collection1.add(2)
collection1.add(2)

collection1.add("KumarHirdesh")
collection1.add((1, 2, 3, 4))
collection1.add([1, 2, 3, 4]) # TypeError: unhashable type: 'list'
collection1.add({1, 2, 3, 4}) # TypeError: unhashable type: 'set'
print(collection1)
print(type(collection1))
print(len(collection1))


collection1.clear()

print(len(collection1))


collection1.remove(7) # does not exist

############

collection = {"hello",  "apnacollege", "world", "coding", "python"}

print(collection)
print(collection.pop())
print(collection.pop())


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # {1, 2, 3, 4, 5}
print(set1)
print(set2)
# Dictionary Operations
info = {
    "key": "value",
    "name": "Sami",
    "learning": "python_coding",
    "age": 35,
    "is_adult": True,
    "marks": 94.4,
}
print("Dictionary info:", info)
print("Type of info:", type(info))

# Empty dictionary
null_dict = {}  # empty dictionary syntax
print("Empty dictionary:", null_dict)
print("Type of null_dict:", type(null_dict))

# Another dictionary with lists and tuples as values
info1 = {
    "name": "apnaworld",
    "subjects": ["python", "C", "Java"],
    "topics": ("dict", "set"),
    "age": 24,
    "is_adult": True,
    "marks": 94.4,
}
print("Dictionary info1:", info1)
print("Type of info1:", type(info1))
print("Access 'name' in info:", info["name"])
print("Access 'marks' in info:", info["marks"])

# Update value in dictionary
info["name"] = "Kumar"
print("Updated info:", info)

# Nested Dictionary
student = {
    "name": "kumar",
    "subjects": {
        "chem": 97,
        "phy": 98,
        "math": 95,
    }
}
print("Nested Dictionary student:", student)
print("Subjects in student:", student["subjects"])
print("Chemistry marks:", student["subjects"]["chem"])

# Dictionary Methods
print("Keys in student:", list(student.keys()))
print("Number of keys in student:", len(list(student.keys())))
print("Values in student:", list(student.values()))
print("Items in student:", list(student.items()))

# Using get method
print("Name in student:", student.get("name"))
print("Non-existent key (name2) in student:", student.get("name2"))

# Update dictionary with new data
student.update({"city": "delhi"})
new_dict = {
    "city": "delhi",
    "age": 21,
    "subjects": {
        "english": 89,
    }
}
student.update(new_dict)
print("Updated student dictionary:", student)

#################################################

# Set Operations
nums = {1, 2, 3, 4}
print("Set nums:", nums)
print("Type of nums:", type(nums))

# Demonstrating duplicate removal in sets
sets = {1, 2, 2, 2}
print("Set with duplicates (resolved):", sets)

# Mixed data type set
collection = {1, 2, 3, 4, "Hello", "Kumar"}
print("Mixed type set collection:", collection)

# Add and clear operations in sets
collection1 = set()
collection1.add(1)
collection1.add(2)
collection1.add("KumarHirdesh")
collection1.add((1, 2, 3, 4))

# Attempting to add unhashable types
try:
    collection1.add([1, 2, 3, 4])  # TypeError: unhashable type: 'list'
except TypeError as e:
    print("Error adding list to set:", e)

try:
    collection1.add({1, 2, 3, 4})  # TypeError: unhashable type: 'set'
except TypeError as e:
    print("Error adding set to set:", e)

print("Updated collection1 set:", collection1)
collection1.clear()
print("Cleared collection1:", collection1)

# Union and Intersection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union of set1 and set2:", set1.union(set2))      # {1, 2, 3, 4, 5}
print("Intersection of set1 and set2:", set1.intersection(set2))  # {3}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2)) # {1, 2, 3, 4, 5}
print(set1)
print(set2)