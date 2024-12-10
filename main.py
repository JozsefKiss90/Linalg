import numpy as np

v1 = np.array ( [ 1,3,5,7] )
v2 = np.array ( [ 0,1, 0] )
op = np.outer( v1 , v2 )
print(op)