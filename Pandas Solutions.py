'''MADE BY ANIRBAN BHATTACHARYA RESPECT++++'''

import pandas as pd
import numpy as np

# Q.1- Why do we need to use Pandas?
# Pandas allows us to analyze big data and make conclusions based on statistical 
# theories. Pandas can clean messy data sets, and make them readable and relevant.

# Q.2- State whether True or False
# a. A series object is size mutable. -> False
# b. A Dataframe object is value mutable -> True

# Q.3- Consider a given Series ,
# Series1:200 700
# 201 700
# 202 700
# 203 700
# 204 700
# Write a program in Python Pandas to create the series and display it.
sr = pd.Series(700, index = [200, 201, 202, 203, 204])

# Q.4- Consider the following Series object,
#  IP 95
# Physics 89
# Chemistry 92
# Math 95
# i. Write the Python syntax which will displayonly IP.
# ii. Write the Python syntax to increase marks of all subjects by 10.
sr = pd.Series([95, 89, 92, 95], index = ["IP", "Physics", "Chemistry", "Math"])
print(sr["IP"])
inc = sr + 10

# Q5 Consider a given series : SQTR
# QTR1 50000
# QTR2 65890
# QTR3 56780
# QTR4 89000
# QTR5 77900
# Write a program in Python Pandas to create and display the series
sr = pd.Series([50000, 65890, 56780, 89000, 77900], index = ["QTR1", "QTR2", "QTR3", "QTR4", "QTR5"])
print(sr)

# Q6 What will be the output produced by the following programming statements 1 & 2?
# import pandas as pd
# S1=pd.Series(data=[31,41,51])
# print(S1>40) -->Statement1
# print(S1[S1>40]) -->Statement2
# Statement 1
# 0    False
# 1     True
# 2     True
# Statement 2
# 1    41
# 2    51

# Q7 Given two series S1 and S2
# S1   S2
# A 39 A 10
# B 41 B 10
# C 42 D 10
# D 44 F 10
# Find the output for following python pandasstatements?
# a. S1[ : 2]*100
# b. S1 * S2
# c. S2[ : : -1]*10
# A output
# A 3900
# B 4100
# B output
# A    390
# B    410
# C    420
# D    440
# C output
# D    100
# C    100
# B    100
# A    100

# Q8 Given the following Series S1 and S2:
# S1 S2
# A 10 A 5
# B 20 B 4
# C 30 C 6
# D 40 D 8
# Write the command to find the multiplication ofseries S1 and S2
s1 = pd.Series([10, 20, 30, 40], index = ["A", "B", "C", "D"])
s2 = pd.Series([5, 4, 6, 8], index = ["A", "B", "C", "D"])
print(s1*s2)

# Q9 Consider a given Series ,
# Subject:ENGLISH 75
#  HINDI 78
#  MATHS 82
#  SCIENCE 86
# Write a program in Python Pandas to create thisseries
sr = pd.Series([75, 78, 82, 86], index = ["ENGLISH", "HINDI", "MATHS", "SCIENCE"])

# Q10 Consider the following Series object, “company” and its profit in Crores
# TCS 350
# Reliance 200
# L&T 800
# Wipro 150
# i. Write the command which will display the name of the company having profit>250.
# ii. Write the command to name the series as Profit.
sr = pd.Series([350, 200, 800, 150], index = ["TCS", "Reliance", "L&T", "Wipro"], name = "company")
# i:-
print(sr[sr>25])
# ii:-
sr.name = "Profit"

# Q11 Consider two objects a and b. a is a list whereas b is a Series. Both have values10,20,25,50.
# What will be the output of the following two statements considering that the above objects
# have been created already
# a. print(a*2)
# b. print(b*2) 
# Justify your answer.
# A will print the following:-
# 0     20
# 1     40
# 2     50
# 3    100
# and B will print the following:-
# [10, 20, 25, 50, 10, 20, 25, 50]
# The reason behind is that when you multipy any list datatype with any number it
# repeates the elements in that list for the number of times we multiply it.
# But on the other hand when we multiply any pandas series with a number
# it multiplies all the elements of that series with that number. This is because
# pandas series code is written in that way. Mainly panadas back end code is inspired from
# numpy concepts. And in numpy when we multiplied any array with a number all the items
# got multiplied.

# Q12 Sequences section and contribution store the section name ( 'A','B','C','D','E') and contribution
# (8900,8700,7800,6500,nil) for charity. Your school has decided to donate more contribution by
# each section, so donation has been doubled. Write code to create series object that stores the
# contribution amount as the values and section name as indexes with data type as float32.
sr = pd.Series([8900,8700,7800,6500,np.nan], index = ["A", "B", "C", "D", "E"], dtype = np.float32)
print(sr*2)

# Q13 Given a Series object shown below:
# A 6700
# B 8000
# C 5400
# D 3400
# dtype : int64
# Why is following code producing error whileworking on Series object s13?
# import pandas as pd
# s13.index=range(0,5)
# print(s13)
# The code will produce an error because the series has only 4 elements and we
# are changing the index to 0 to 4 (0, 1, 2, 3, 4) which is 5 elements.
# Expected axis=0 item length is 4 but 5 is provided.
# For this reason it will produce an error.

# Q14 What is the output of the following program:
# import pandas as pd
# import numpy as np
# data=np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# s=pd.Series(data)
# print(s[:4])
# print(s[-4:])
# First print statement
# 0    Mon
# 1    Tue
# 2    Wed
# 3    Thu
# Second print statement
# 3    Thu
# 4    Fri
# 5    Sat
# 6    Sun

# Q15 What do you mean by positional index and labeled index?
# Positional index takes an integer value that corresponds to its position 
# in the series starting from 0, whereas labelled index takes any user-defined 
# label as index.

# Q16 What type of data can be passed to create a non-empty Series object in Python Pandas?
# You can create a list of elements and pass that list in data parameter of Series.
# This will create a non empty series.

# Q17 Differentiate between NumPy Arrays and Pandas Series.
# The difference between numpy array and pandas series is that numpy arrays do not show
# its index in the output. On the other hand pandas series has shows its
# index on output. One more diffrence between numpy array and series is that we cannot change
# the indexing in numpy i.e it is implicit index and we can change the index in pandas series as per user
# i.e it is explicit index.

# Q18 What is the use of the drop() and reindex() method? Explain with an example.
# Nahi aata. sorry

# Q19 Write a program to store a population of 4 cities with an index of the previous 4 years.
# Page 3
# Write functions to do the following:
# i) Print the average population of the recent two years.
# ii) Print the grand total of populations.
# iii) Print the highest population.
# iv) Print the difference between the first year and last year.
# v) Delete entry of one year from the series.
# nahi aata. ig question hi galat hai. mujhe samaj nahi aaya question

# Q20 Explain the following series attributes with an example:
# 1. values
# 2. dtype
# 3. nbytes
# 4. size
# 5. hasnans
# 6. index.name
# 7. shape
# 8. ndim
# 9. empty
# 10. index
# 1. values - This gives the data which we inserted while creating the series
# For eg:-
# sr = pd.Series([95, 89, 92, 95])
# sr.values

# 2. dtypes - This gives the datatype of the values inserted
# For eg:-
# sr = pd.Series([95, 89, 92, 95])
# sr.dtype

# 3. nbytes - This gives total bites consumed from a series or array
# For eg:-
# sr = pd.Series([95, 89, 92, 95])
# sr.nbytes

# 4. size - This gives the total number of elements in a series or an array no matter it is 2d or nd array
# sr = pd.Series([95, 89, 92, 95])
# sr.size

# 5. hasnans - This returns a boolean value. If any element is NaN then it will return True and vice versa
# sr = pd.Series([95, 89, 92, 95])
# sr.hasnans

# 6. index.name - Nahi maalum

# 7. shape - This returns the shape of series or an array means the dimensions and number of rows and columns
# sr = pd.Series([95, 89, 92, 95])
# sr.shape

# 8. ndim - This returns the dimesnions of a series or an array
# sr = pd.Series([95, 89, 92, 95])
# sr.ndim

# 9. empty - This returns a boolean telling wheather a series is empty or not
# sr = pd.Series([95, 89, 92, 95])
# sr.empty

# 10. index - This returns the index values of any series
# sr = pd.Series([95, 89, 92, 95]))
# sr.index

'''MISSION PASSED SUCCESSFULLY!!'''
