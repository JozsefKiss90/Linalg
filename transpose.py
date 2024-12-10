import numpy as np

'''
v1_1 = np.array([16, 6, 0])
v1_2 = np.array([6, 10, -3])
v1_3 = np.array([0, -3, 22])
'''
v1_1 = np.array([0, 1, 3])
v1_2 = np.array([1, 0, 3])
v1_3 = np.array([2, 3, 4])
# Method 1: v1_1 and v1_2 as columns
A_columns = np.column_stack((v1_1, v1_2, v1_3))
At1_columns = A_columns.T

# Method 2: v1_1 and v1_2 as rows
A_rows = np.vstack((v1_1, v1_2, v1_3))
At2_rows = A_rows.T

#print(A_columns)
#print(At1_columns)
#print(A_rows)
#print(At2_rows)

D = np.diag ( [ 1 , 2 , 3 , 5 ] )
print(D)

l = .01
I = np.eye( 4 )
A = D
As = A + l * I
print(As)
tr = np.trace(As)
print(tr)