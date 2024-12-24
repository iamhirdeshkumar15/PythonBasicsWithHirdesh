# student_and_account_classes
# create student class that takes name & marks of 3 subjects as agruments in constructor.
# then create a method to print the average.


class Student:
    def __init__(self,name,marks):  
        self.name = name
        self.marks = marks
        
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name, "your avg score is:", sum/3)


s1 = Student("Hirdesh",[79,89,99]) 
s1.average()

s1.name = "Kumar"
s1.average()



########################################################################


#  create Account class with attributes balance & account number.
# create a method for debit, credit & priniting the balance.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ",self.get_balance())


    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ",self.get_balance())



    def get_balance(self):
        return self.balance



acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

