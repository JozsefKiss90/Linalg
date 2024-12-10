import numpy as np

# Define your vectors
v1 = np.array([1,2])  # Replace [...] with your vector components
v2 = np.array([1,-2])
v2 = np.array([-1,-2])

# Form a matrix with these vectors as columns
A = np.column_stack((v1, v2))

# Check the rank of the matrix
rank = np.linalg.matrix_rank(A)

# Determine if the vectors are linearly independent
linearly_independent = rank == A.shape[1]

print(rank)
print("Are the vectors linearly independent?", linearly_independent)
