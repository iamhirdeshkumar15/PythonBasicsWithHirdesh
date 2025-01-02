# Write Code of statistical operstions on 1D Array with using some function like 
# max(),min(),sum(),mean() or more.

import numpy as np

array = np.array([4,2,3,9,7,6])
max_value = np.max(array)  # Maximum value
min_value = np.min(array)  # Minimum value
total_sum = np.sum(array)  # Sum of elements
mean_value = np.mean(array)  # Mean value
std_deviation = np.std(array)  # Standard deviation
variance = np.var(array)  # Variance
product = np.prod(array) # Product
medi = np.median(array) #Median

print("Array:", array)
print("Maximum:", max_value)
print("Minimum:", min_value)
print("Sum:", total_sum)
print("Mean:", mean_value)
print("Standard Deviation:", std_deviation)
print("Variance:", variance)
print("Product:", product)
print("Median:", medi)