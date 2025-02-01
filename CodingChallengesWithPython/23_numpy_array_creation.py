# Demonstrate NumPy array creation and execution.
# Creating 1D and 2D arrays using np.array().

import numpy as np
# Creating 1D
# Integer Homogeneous
list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1)
print(array1)
print(type(array1))

# Float Homogeneous 
list2 = [10, 20.40, 30, 40, 50]
array2 = np.array(list2)
print(array2)
print(type(array2))

# Character Homogeneous
list3 = [10, "H", 30, 40, 50]
array3 = np.array(list3, dtype = 'U32')
print(array3)
print(type(array3))

# Creating 2D

lists1 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
array4 = np.array(lists1)
print(array4)
print(type(array4))

# using arange() for 1D
array5 = np.arange(1,10)
print(array5)

# using arange() and reshape() for 2D
array6 = np.arange(11, 17).reshape((2, 3))
print(array6)

# using zeros() for 1D generate floating value.
array7 = np.zeros(4)
print(array7)

# using zeros() for 2D generate floating value.
array8 = np.zeros((4, 2))
print(array8)

# using ones() for 1D generate floating value.
array9 = np.ones(4)
print(array9)

# using ones() for 2D generate floating value.
array10 = np.ones((4, 2))
print(array10)