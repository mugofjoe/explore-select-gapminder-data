import numpy as np
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})

def second_largest_in_column(column):
    # np.sort(df.ix[:,2])[-2]
    # return np.sort(column)[-2]
    sorted_column = column.sort_values(ascending=False)
    return sorted_column.iloc[1]

second_largest_in_column(df['a'])

# Change False to True for this block of code to see what it does

# DataFrame apply() - use case 2
if True:   
    print df.apply(np.mean)
    print df.apply(np.max)
    
def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each 
    column of the input DataFrame.
    '''
    return df.apply(second_largest_in_column)

second_largest(df)