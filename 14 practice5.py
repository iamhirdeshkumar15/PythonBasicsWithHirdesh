# Task 1: Create a dictionary with word meanings
new_dict = {
    "cat": "a small animal",
    "table": ["a piece of furniture", "list of facts & figures"]
}
print("Dictionary of word meanings:", new_dict)

# Task 2: Calculate the number of classrooms needed for unique subjects
subjects = {"python", "java", "C++", "python", "javaScript", "java", "python", "java", "C++", "C"}
num_classrooms = len(subjects)
print("Number of classrooms needed:", num_classrooms)

# Task 3: Enter marks for 3 subjects and store them in a dictionary
marks = {}
physics_marks = int(input("Enter the Physics Mark: "))
chemistry_marks = int(input("Enter the Chemistry Mark: "))
math_marks = int(input("Enter the Math Mark: "))

marks.update({"physics": physics_marks, "chemistry": chemistry_marks, "math": math_marks})
print("Marks Dictionary:", marks)

# Task 4: Store 9 and 9.0 as separate values in a set using tuples
values = {("float", 9.0), ("int", 9)}
print("Set with distinct 9 and 9.0 values:", values)
