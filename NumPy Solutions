'''MADE BY ANIRBAN BHATTACHARYA RSEPECT++'''

import numpy as np

# 1. Write a NumPy program to create a 1 D array having 12 elements using arrange
# ().Now convert this array into a 2 D array with size 4X3.
arr = np.arange(0, 12)
rarr = arr.reshape(4, 3)

# 2. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.
arr1 = np.zeros((10))
arr2 = np.ones((10))
arr3 = np.ones((10)) * 5
con = np.concatenate((arr1, arr2, arr3))

# 3. Write a NumPy program to create an array of integers from 30 to 70.
arr = np.arange(30, 71)

# 4. Write a NumPy program to create an array of all even integers from 30 to 70.
arr = np.arange(30, 71)
l = []
for i in arr:
  if i % 2 == 0:
    l.append(i)
arr1 = np.array(l)

# 5. Write a NumPy program to create a 3x3 identity matrix
arr = np.eye(3)
arr1 = np.identity(3)
# we can create an array using both of the wbove with 3x3 matrix.
# The only difference between both is that we can change the diagonals in eye func
# and cannot in identity func (K parameter)

# 6. Write a NumPy program to generate an array of 15 random numbers from a
# standard normal distribution.
arr = np.random.standard_normal(15)

# 7. Write a NumPy program to create a 3X4 array and iterate over it.
arr = np.random.randint(50, 100, 12).reshape(3, 4)
for i in np.nditer(arr):
  print(i)

# 8. Write a Numpy program to extract values at odd numbered position from a Numpy
# Array
arr = np.random.randint(50, 100, 12)
exctL = []
for i in range(arr.size):
  if i % 2 != 0:
    exctL.append(arr[i])

# 9. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
arr = np.arange(10, 22).reshape(3, 4)

# 10. Write a NumPy program to find the number of rows and columns in a given matrix
arr = np.arange(10, 22).reshape(3, 4)
arr.shape

# 11. Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with
# zeros on the main diagonal.

# kya backchod question hai yeh smajha nahi mein samaj aay to batana

# 12. Write a NumPy program to compute the sum of all elements, the sum of each
# column and the sum of each row in a given array
arr = np.arange(10, 22).reshape(3, 4)
arr.sum()

# 13. Write a NumPy program to convert a given list into an array, then again convert it
# into a list. Check initial list and final list are equal or not.
l = [4, 8, 9, 3, 2]
arr = np.array(l)
l1 = arr.tolist()
if l == l1:
  print("Both the lists are euqal!")

# 14. Write a NumPy program to check whether two arrays are equal (element wise) or
# not
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr2 = np.array([[4, 7, 9, 3, 0], [3, 7, 0, 3, 9]])
if arr1.size == arr2.size:
  print("Both the arrays have same size.")
else:
  print("Arrays do not have same length.")

# 15. Write a NumPy program to swap rows and columns of a given array in reverse
# order.
arr = np.arange(10, 22).reshape(3, 4)
tarr = arr.T
tarr[::-1, ::-1]


'''MISSION PASSED SUCCESSFULLY!!'''
