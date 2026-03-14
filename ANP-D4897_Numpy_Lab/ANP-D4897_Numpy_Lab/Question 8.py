#Question no 8
'''Create a 3×3 matrix and calculate the transpose of the matrix.'''
import numpy as np

mat=np.random.randint(3,11,(3,3))
print(mat)

print(":transpose matrix  : ",mat.T)

#output
'''
[[7 5 6]
 [9 7 7]
 [7 7 7]]
:transpose matrix  :  [[7 9 7]
 [5 7 7]
 [6 7 7]]

'''