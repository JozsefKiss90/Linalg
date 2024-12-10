import numpy as np

A = np.array([
    [3, -4],
    [3, -9],
])

B = np.array([
    [4, 4],
    [6, 0],
])

matrix1 = np.array([[1, 2, 5],
                    [-5, 0, 5],
                    [-9, 4, 3]])

# Matrix 2
matrix2 = np.array([[5, 5, 5],
                    [4, 3, 4],
                    [1, 1, 9]])

tr1 = np.trace(matrix1)
tr2 = np.trace(matrix2)

tr3 = np.trace(matrix1+matrix2)

#print(tr3)
#print(tr1+tr2 == tr3)

C = np.array([3,-5,1])

D = np.array([-2,1,5])

matrix_A = np.array([[5, -3],
                    [2, -3]])

# Matrix B
matrix_B = np.array([[-4, -1],
                    [1, 3]])

#print(np.trace(-3*matrix_A + 5*matrix_B))
#print(-15*np.trace(matrix_A + matrix_B))

print(matrix2)
print(tr2)