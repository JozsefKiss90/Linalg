import numpy as np
from scipy.linalg import null_space

A = np.array([
    [2,3,4],
    [0,0,0],
    [7,8,9]
])

rank_A = np.linalg.matrix_rank(A)
rank_AT = np.linalg.matrix_rank(A.T)
left_null_space_A = null_space(A.T)
null_space_A = null_space(A)

print(rank_A)
print(np.linalg.matrix_rank(left_null_space_A))
print(rank_AT)
print(np.linalg.matrix_rank(null_space_A))
print('\n')

B = np.array([
    [1,2],
    [1,2],
    [2,4]
])

rank_B = np.linalg.matrix_rank(B)
rank_BT = np.linalg.matrix_rank(B.T)
null_space_B = null_space(B)
left_null_space_B = null_space(B.T)

print(rank_B)
print(np.linalg.matrix_rank(left_null_space_B))
print(rank_BT)
print(np.linalg.matrix_rank(null_space_B))
print('\n')

C = np.array([
    [1,0,3],
    [0,4,5],
    [2,0,6]
])

rank_C = np.linalg.matrix_rank(C)
print(rank_C)
print('\n')

D = np.array([
    [1,0],
    [2,0]
])
print(null_space(D))