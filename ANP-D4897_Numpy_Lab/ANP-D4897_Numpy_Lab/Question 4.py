#Question no 4
'''Create two 3×3 matrices and perform matrix multiplication.'''
import numpy as np
mat1=np.random.randint(1,11,(3,3))
print(mat1)
mat2=np.random.randint(1,11,(3,3))
print(mat2)
print("Multiplications : ")
print(np.dot(mat1,mat2))


#output
'''
[[1 5 3]
 [1 9 4]
 [5 3 4]]
[[2 9 9]
 [1 9 1]
 [9 5 9]]
Multiplications : 
[[ 34  69  41]
 [ 47 110  54]
 [ 49  92  84]]

'''