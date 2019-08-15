import numpy as np


an_array = np.array([[3,33,333],[2,22,3]])
print("whole array ")
print(an_array)
print("elements ")
print(an_array[0,0])

print("fill the array with the given value")
ex1 = np.full((2,2), 9)
print(ex1)

print("create an array with ones in the diagonals")
ex2 = np.eye(2,2)
print(ex2)

print("create an array with ones as element")
ex3 = np.ones((2,2))
print(ex3)

print("Shape of the matrices")
print("an_array ",an_array.shape)
print("ex1 ",ex1.shape)
print("ex2 ",ex2.shape)
print("ex3 ",ex3.shape)

print("create an array with random values")
ex4 = np.random.random((2,2))
print("ex4 ",ex4)

#For a matrix with n rows and m columns, 
# shape will be (n,m). 
# The length of the shape tuple is therefore the rank, 
# or number of dimensions, ndim.
ex5 = np.array([1,2,3])
print(ex5)
print("ex5 ",ex5.shape)
print("print the dimension of array ", ex5.ndim)
# the total number of elements of the array. 
# This is equal to the product of the elements of shape.
print("size of the array ", ex5.size)
print("type of elements in array ",ex5.dtype)

ex6 = np.array([[11,12,14,14], [21,22,23,24],[31,32,33,34]])
print("ex6 ")
print(ex6)
#This will create the slice of the existing array but not the copy.
ex6_slice = ex6[:2,1:3]
print("ex6_slice ",ex6_slice)
print("change the value in ex6_slice ")
ex6_slice[0,1] = 15
print("the value of ex6 also changes ", ex6)
#This creates the copy of slice
ex6_slice2 = np.array(ex6[:2,1:3])
print("This is a copy of ex6 array slice ",ex6_slice2)
ex6_slice2[0,1] = 13
print("This will not change the ex6 array ", ex6)
row_rank1 = ex6[1, :]
print("using array indexing - single number ",row_rank1, row_rank1.shape)

col_indices = np.array([0,1,2])
#the arange method is used to add values into the array. 
#it works similar to the python range function
row_indices = np.arange(3)
print(row_indices)
for row,col in zip(col_indices,row_indices):
    print(row," , ",col)

print("Values in ex6 at those indices ", ex6[row_indices, col_indices])