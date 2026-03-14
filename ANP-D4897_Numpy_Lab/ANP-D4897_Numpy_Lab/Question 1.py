# Question 1
'''Create a NumPy array from 1 to 20 and reshape it into 4x5 matrix'''
import numpy as np
arr1 = np.arange(1, 21)
print(arr1)
arr2=arr1.reshape(4,5)
print("After reshaping :")
print(arr2)

# Output:
'''
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
After reshaping :
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]]

'''