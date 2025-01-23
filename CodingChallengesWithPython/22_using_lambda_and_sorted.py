# Added program demonstrating the use of lambda functions and sorted() in Python.
numbers = [11,13,20,31,40,51,60,71,80,91,100]
def even(x):
    return x % 2 == 0

# Using list() and filter()
evens = list(filter(even,numbers))
print("Even Numbers: ",evens)

# Using list() and filter() and lambda
evenn = list(filter(lambda x: x % 2 == 0 and x > 50,numbers))
print("Even Numbers greater than 50 : ",evenn)


# Using sorted()
city = ['Jaipur', 'Mumbai', 'Delhi', 'Punjab', 'Bihar', 'Uttar Pradesh', 'Pune', 'Lumbini']
def length(city):
    return len(city)

sort = sorted(city,key=length)
print("Sorted words by lenght: ",sort)

# Using sorted() and lambda
sort1 = sorted(city, key=lambda x:len(x))
print("Sorted Words by length: ",sort1)

# using reverse
sort2 = sorted(city, key=lambda x:len(x), reverse= True)
print("Sorted Words by length: ",sort2)