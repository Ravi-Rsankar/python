import numpy as np

an_array = np.array([[11,12],[21,22],[31,32]])
print(an_array)
fil = (an_array>15)
print(fil)
print(an_array[fil])

print(an_array[an_array>15])
ex1 = np.array([11,12])
print(ex1.dtype)
# force to a different type
ex2 = np.array([11.1, 12.2], dtype=np.int64)
print(ex2)
print(ex2.dtype)
#Datatypes matters in ndarray.
#-----------------------------------#
#Statistical methods
arr = 10 * np.random.randn(2,5)
print(arr)
print(arr.mean())
#compute the mean by row
print(arr.mean(axis=1))
#compute the mean by column
print(arr.mean(axis=0))
print(arr.sum())
#compute median
print(arr)
print(np.median(arr, axis=1))
#-----------------------------------#
#Sorting
unsorted = np.random.randn(10)
print(unsorted)
#create a copy and sort
sorted = unsorted
sorted.sort()
print(sorted)
#finding unique elements
array = np.array([1,1,2,2,3,3,4,4,6])
print(np.unique(array))
#------------------------------------#
#set operations
s1 = np.array(['desk', 'chair', 'bulb'])
s2 = np.array(['lamp', 'bulb','chair'])
print(s1, s2)
print(np.intersect1d(s1,s2))#intersect expects 1d array
print(np.union1d(s1,s2))
print(np.setdiff1d(s1,s2))#elements in s1 not in s2
print(np.in1d(s1,s2))#returns true if that element in s1 is also in s2