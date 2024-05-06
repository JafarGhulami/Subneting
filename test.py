from numpy import random
import numpy as np

arr = np.array([5,6,7,8])

#random.shuffle(arr)
print(arr)

x = random.permutation(arr)
print(arr)
print(x)