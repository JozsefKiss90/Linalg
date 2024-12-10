import numpy as np

# Create random matrices M1 and M2
M1 = np.array([[1, 2],[3,4]])
M2 = np.array([[5, 6],[7,8]])

# Perform matrix multiplication to get matrix C
C = M1 @ M2
D = M2 @ M1
# Print the resulting matrix C
#print(C)
#print(D)

v1 = np.array([[3, 2], [0, 1]])
v2 = np.array([[1, 1], [1, 2]])

'''print(v1)
print(v1.T)
print((v1 @ v2).T)
'''

matrix1 = np.array([[2, -1, 2],
                    [4, 0, 0],
                    [0, 1, 1]])

matrix2 = np.array([[3, 0, 3],
                    [0, 7, 0]])

#print(matrix1.T @ matrix2.T)
#print((v1.T @ v2.T))

matrix3 = np.array([[1, 11, 1],
                   [-5, -2, 1],
                   [-1, -5, 2]])

simm = 1/2 * (matrix3.T + matrix3)

simm2 =  matrix2.T @ matrix2

print(simm2 == simm2.T)

A = np.array( [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ] )
print(A.flatten(order="F"))