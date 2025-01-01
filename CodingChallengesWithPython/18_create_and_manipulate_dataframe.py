# Write a Code for creating and manipulating DataFrames using pandas.

import pandas as pd
# Creating a DataFrame manually from a list of tuples.
std_data = [(1,'Kumar',25,'Male','Mukundgadh'),
            (2,'Sami',22,'Female','Labani'),
            (3,'Shiva',28,'Male','Semari'),
            (4,'Sunil',28,'Male','Parsahwa'),
            (5,'Pratik',19,'Female','Kapilvastu')]

df = pd.DataFrame(std_data, columns=['Stu_id','Name','Age','Gender','Address'])
print(df)

# Loading data into a DataFrame from a CSV file.
df =  pd.read_csv("CodingChallengesWithPython/Student.csv")
print(df)

#Extended DataFrame program with exploration methods like head, tail, shape, and column operations.

print("\nFirst 5 rows of DataFrame:")
print(df.head())

print("\nLast 5 rows of DataFrame:")
print(df.tail())

print("\nShape of DataFrame (rows, columns):")
print(df.shape)

print("\nColumns in DataFrame:")
print(df.columns)

print("\nTotal elements in DataFrame:")
print(df.size)

print("\nData types of each column:")
print(df.dtypes)

print("\nDataFrame values as numpy array:")
print(df.values)

print("\nIndex of DataFrame:")
print(df.index)

print("\nColumn 'Age':")
print(df.Age)

print("\nSubset of DataFrame with 'Age' and 'City':")
print(df[['Age','City']])
