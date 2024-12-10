import numpy as np

def is_orthogonal(matrix):
    transpose = matrix.T
    product = np.dot(matrix, transpose)
    identity = np.eye(matrix.shape[0])
    return np.allclose(product, identity)

# Example usage:
A = np.array([
    [1, 2],
    [-2, 2],
    [-2, 1]
])

print("Is A orthogonal?", is_orthogonal((1/3) * A))
