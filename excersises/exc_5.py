import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

# Matrix multiplication using @ for verification
result_at = A @ B

# Implement matrix multiplication using the "layer perspective"
result_layer = np.zeros((2, 3))  # Initialize a 2x3 result matrix

for i in range(A.shape[1]):  # Loop over the columns of A / rows of B
    # Outer product of the i-th column of A and the i-th row of B
    layer = np.outer(A[:, i], B[i, :])
    # Sum the outer products to get the final result
    result_layer += layer

'''print(result_at, result_layer)
print(A[:, 2])
print( B[2, :])
print(np.outer(A[:, 2],B[2, :]))
'''

diagonal_values = np.array([1, 2, 3, 4])
diagonal_matrix = np.diag(diagonal_values)

# Generate a 4x4 dense matrix of random numbers
dense_matrix = np.random.rand(4, 4)

#print(diagonal_matrix, dense_matrix)

D = np.diag(np.arange(1, 5))
# Create a random 4x4 matrix A
A = np.random.randn(4, 4)

# Element-wise multiplication of D and A
C1 = D * A

# Matrix multiplication of D and A
C2 = D @ A
print(D)
print(A)
# Print the diagonal elements of C1 and C2
print(C1)
print(C2)
print("Diagonal of C1:")
print(np.diag(C1))

print("\nDiagonal of C2:")
print(np.diag(C2))