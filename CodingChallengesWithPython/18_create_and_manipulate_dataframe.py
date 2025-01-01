# Write a Code for creating and manipulating DataFrames using pandas.

import pandas as pd
std_data = [(1,'Kumar',25,'Male','Mukundgadh'),
            (2,'Sami',22,'Female','Labani'),
            (3,'Shiva',28,'Male','Semari'),
            (4,'Sunil',28,'Male','Parsahwa'),
            (5,'Pratik',19,'Female','Kapilvastu')]

df = pd.DataFrame(std_data, columns=['Stu_id','Name','Age','Gender','Address'])
print(df)


import pandas as pd1
df =  pd.read_csv("CodingChallengesWithPython/Student.csv")
print(df)
