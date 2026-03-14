#Question No 2
'''Create a 5×5 matrix with random integers between 1 and 100 and find Minimum value and Maximum value
'''

import numpy as np
integers=np.random.randint(1,101,(5,5))
print(integers)
print("maximum =",np.max(integers))
print("minimum =",np.min(integers))

#output
'''
[[35 83 55  5 31]
 [47 38 63 44  2]
 [12 67 11 81 76]
 [27 30 41 85 80]
 [80 75 31 90 63]]
maximum =90
minimum =2

'''

