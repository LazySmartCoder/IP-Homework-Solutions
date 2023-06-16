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
