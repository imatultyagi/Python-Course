#Question no 6
'''Create a 4×4 matrix and calculate:Row-wise sum
'''
import numpy as np
matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])

row_sum = matrix.sum(axis=1)
col_sum = matrix.sum(axis=0)

print("Row Sum:", row_sum)
print("Column Sum:", col_sum)

# Output:
''' Row Sum:
[10 26 42 58]
Column Sum:
[28 32 36 40]'''