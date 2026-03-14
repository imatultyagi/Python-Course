# Question 3
'''Create a NumPy array of numbers from 1 to 10 and replace all even numbers with 0'''

import numpy as np
arr2 = np.arange(1, 11)
arr2[arr2 % 2 == 0] = 0
print(arr2)

# Output:
# [1 0 3 0 5 0 7 0 9 0]   
        

