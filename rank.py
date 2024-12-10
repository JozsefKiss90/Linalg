import numpy as np

A = np.array([
    [1, 2, 3],
    [3, 4, 1],
    [5, 9, 1]
])

B = np.array([
    [0, 3, 5],
    [1, 0, 4],
    [3, 3, 0]
])

C = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

D = np.array([
    [11, 12, 13],
    [7, 12, 31],
    [12, 18, 61]
])

'''rank1 = np.linalg.matrix_rank(A)
rank2 = np.linalg.matrix_rank(B)
rank3 = np.linalg.matrix_rank(C)
rank4 = np.linalg.matrix_rank(D)
print(rank1,'\n',rank2, '\n', rank3)
print(rank4)
'''
v1= np.array([
    [2, 4, 3],
    [0, 1, 3],
])

v2 = np.array([
    [-2, -1, 3],
    [6 ,-7, 7],
])

rank1 = np.linalg.matrix_rank(v1)
rank2 = np.linalg.matrix_rank(v2)
rank3 = np.linalg.matrix_rank(v1 + v2)
rank4 = np.linalg.matrix_rank(v1 @ v1.T)
rank5 = np.linalg.matrix_rank(v1.T @ v1)
rank6 = np.linalg.matrix_rank(v1 @ v2.T)

print(rank1,'\n',rank2, '\n', rank3)
print(rank4,'\n',rank5, '\n', rank6)