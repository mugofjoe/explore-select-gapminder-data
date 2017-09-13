# load the numpy package
import numpy as numpy

'''
CREATING ARRAYS
'''
# 1D array
a = np.array([1,2,3])

# 2D array
b = np.array([(1.5,2,3), (4,5,6)], dtype=float)

# 3D array
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]], dtype=float)

'''
INITIALIZE ARRAYS
'''
# create array of zeros (3x4)
np.zeros((3,4))

# create array of ones (3D 2x3x4)
np.ones((2,3,4), dtype=np.int16)

# create array of evenly spaced values (step value)
d = np.arange(20, 43, 2)    # 20, 22, 24,...,38, 40, 42

# create array of evenly spaced values (number of samples)
np.linspace(0,2,9)  # from 0 to 2, give 9 items


