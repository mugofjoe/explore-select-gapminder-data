import numpy as np
np.random.seed(42)
grades_nparray = np.random.randint(low=50, high=100, size=100)
print(grades_nparray)



# convert numpy array to pandas series
import pandas as pd 
grades_pd_series = pd.Series(grades_nparray)

print('hello world')



