
# Python code demonstrate creating
# pandas DataFrame with indexed by
 
# DataFrame using arrays.
import pandas as pd
 
# initialize data of lists.
data = {'Name':['Tom', 'Jack', 'nick', 'juli'],
        'marks':[99, 98, 95, 90]}
 
# print the data
print(pd.DataFrame(data, index=['a','b','c','d']))

# Python program to demonstrate creating
# pandas Datadaframe from lists using zip.

# List1
Name = ['tom', 'krish', 'nick', 'juli']

# List2
Age = [25, 30, 26, 22]

#list3
adress = [1, 2, 3, 4]

# get the list of tuples from two lists.
# and merge them by using zip().
list_of_tuples = list(zip(Name, Age, adress))

# Assign data to tuples.
list_of_tuples


# Converting lists of tuples into
# pandas Dataframe.
df = pd.DataFrame(list_of_tuples,
				columns = ['Name', 'Age', 'Adress'])
	
# Print data.
print(df)

# importing numpy as np
import numpy as np
 
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 45, 56],
        'Third Score':[52, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print(df)
