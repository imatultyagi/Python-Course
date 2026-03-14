#Question No 5
'''Create a NumPy array of numbers from 1 to 25 and reshape it into a 5×5 matrix.
Extract the middle 3×3 sub-matrix'''

import numpy as np
numbers = np.arange(1,26)
print(numbers)
reshaped_numbers=numbers.reshape(5,5)
print(reshaped_numbers)
sub_matrix=reshaped_numbers[1:4,1:4]
print("sub-matrix = ",sub_matrix)

#output
'''
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
 25]
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]

sub-matrix = 
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]

'''