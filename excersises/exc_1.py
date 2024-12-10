import numpy as np

v = np.array([3,5,0,2])
w = np.array([1,0,1,5])
u = np.array([2,4,1])

A = np.array([
    [-1, -2, -6, -6],
    [ 1, -1,  0, -2],
    [-1,  0, -1, -4]
])


print(np.outer(u, v))
print(A)

print(np.outer(u,v) - A)

