import numpy as np

# Create random matrices A and B
A = np.random.randn(4, 2)
B = np.random.randn(4, 2)

# Initialize matrix C with zeros
C = np.zeros((2, 2))

# Perform matrix multiplication and fill in matrix C
for col_i in range(2):
    for col_j in range(2):
        C[col_i, col_j] = np.dot(A[:, col_i], B[:, col_j])

# Generate a dense matrix of random numbers
dense_matrix = np.random.rand(3, 3)

# Convert to lower triangular matrix
lower_triangular = np.tril(dense_matrix)

# Transpose the lower triangular matrix
transpose = lower_triangular.T

# Add the lower triangular matrix and its transpose to get a symmetric matrix
symmetric_matrix = lower_triangular + transpose - np.diag(lower_triangular.diagonal())

D = np.zeros((4, 8))

# Fill in the diagonal elements with values from 1 to 4
for d in range(min(D.shape)):
    D[d, d] = d + 1

# Print the resulting matrix D
print("Matrix D:")
print(D)