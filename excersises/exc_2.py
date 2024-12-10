import numpy as np

A = np.array([
    [2,4,3],
    [0,1,3],
])

B = np.array([
    [-2,-1,3],
    [6,-7,7],
])

C = np.array([
    [0,-6],
    [-3,-2],
    [-2,7],
])

D = np.array([
    [1,2],
    [3,4],
    [2,4],
])


print(A + 3*B)
print(D + C)
print(C - D)
print(A.T + D)