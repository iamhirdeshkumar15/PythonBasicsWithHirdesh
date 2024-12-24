# OOPs in Python (Chapter 8)
# Class and Object in Python

# # creating class

class Student:
    name = "Abhay Yadav"

# # creating object (instance)

s1 = Student()
print(s1.name)



class Car:
    color = "Red"
    brand = "BMW"

car1 = Car()
print(car1.color)
print(car1.brand)


class Student:
    def __init__(self):
        print(self)
        print("adding new student in Database.")


s1 = Student()





class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database.")


s1 = Student("Hirdesh",90)
print(s1.name, s1.marks) 

s2 = Student("Abhay",92)
print(s2.name,s2.marks)




class Student:


    # default constructor
    def __init__(self):
        pass

    # parametrized constructor
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database.")


s1 = Student("Hirdesh",90)
print(s1.name, s1.marks) 

s2 = Student("Abhay",92)
print(s2.name,s2.marks)




# Class and Instance Attributes

# Class Attributes -> common for all object

class Student1:
    college_name = "ABC"
    name = "anonymous"  # class attributes
    def __init__(self, name):
        self.name = name  # Instance Attributes


s1 = Student1("kumar")
print(s1.name)
    
# Instance Attributes -> different for each other

class Student2:
    college_name = "LPU"  # class attributes
    def __init__(self,name,marks):
        self.name = name  # Instance Attributes
        self.marks = marks  # Instance Attributes


s1 = Student2("hirdesh", 89)
print(s1.name, s1.marks)
print(s1.college_name)


# Note -> Object Attributes > Instance Attributes


# Methods

# Creating Class
class Student3:
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks


    def hello(self):
        print("hello", self.name)

    def get_marks(self):
        return self.marks

# Creating Object
s1 = Student3("Abhay", 89)
s1.hello()
print(s1.get_marks())





# static method

class Student:
    @staticmethod
    def college():
        print("Hello World!")

Student.college()




##OOPS

# Abstraction

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")

car1 = Car()
car1.start()