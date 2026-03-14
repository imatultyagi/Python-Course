#Question no 9
'''Generate a NumPy array of 10 random numbers between 0 and 1 and normalize the array between 0 and 1'''
import numpy as np
arr_random = np.random.rand(10)
normalized = (arr_random - arr_random.min()) / (arr_random.max() - arr_random.min())

print("Original Array:", arr_random)
print("Normalized Array:", normalized)

# Output:
'''Original Array:
# [0.54 0.21 0.87 0.12 0.63 ...]
# Normalized Array:
# [0.56 0.12 0.95 0.00 0.67 ...]

'''