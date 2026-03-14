#Question no 7
'''Create a NumPy array of numbers from 1 to 15 and find all numbers greater than 10.'''
import numpy as np
numbers=np.arange(1,16)
print(numbers)
print("GReater than 10 : ",numbers>10)


#output

'''
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
GReater than 10 [False False False False False False False False False False  True  True
  True  True  True]


'''