import numpy as np

v1 = np.array([2,5,4,7])
v2 = np.array([4,1,0,2])

dp = np.dot(v1, v2)
outer = np.outer(v1, v2)
v3 = v1 * v2
vMag = np.linalg.norm(v1)
v_unit = v1 / vMag
print(outer)

# Define the orthogonal matrix Q
Q = np.array([[0, -1], [1, 0]])

# Compute the transpose of Q
Q_T = Q.T

# Multiply Q by its transpose
product = np.dot(Q, Q_T)

print("Q * Q^T =\n", product)
