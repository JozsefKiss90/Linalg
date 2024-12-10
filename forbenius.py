import numpy as np

A = np.array( [ [4, 5, -8 ] , [ 1, -1, 2], [2,-2,4] ] )
B = np.array(  [ [4, 5, -8 ] , [ 1, -1, 2], [2,-2,4] ] )

# Calculate the Frobenius norm of the difference between A and B
norm_diff = np.linalg.norm(A - B, 'fro')
norm_diff_vectorized = np.sqrt(np.sum((A - B ) ** 2))
'''print(norm_diff)
print(norm_diff_vectorized)
print(A.flatten(order="F"))'''
print(np.trace(A.T @ B))