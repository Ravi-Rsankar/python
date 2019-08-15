import numpy as np
#broadcasting is useful when working with two matrices with mismatching sizes. 
start = np.zeros((4,3))
print(start)

add_rows = np.array([[1,0,2]])
print(add_rows)
y = start + add_rows
print(y)

add_cols = np.array([[0,1,2,3]])
add_cols = add_cols.T #Transpose operation to convert 1X4 array to 4X1 array
print(add_cols)

y=start + add_cols
print(y)

#broadcasts on both direction
ones = np.array([1])
y=start+ones
print(y)

a = np.array([[0,0],[0,0]])
b1 = np.array([1,1])
b2 = 1

print(a+b1)
print(a+b2)
