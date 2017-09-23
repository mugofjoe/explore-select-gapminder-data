# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Examine DataFrame
if True:
    print example_df
    
# Examine groups
if True:
    grouped_data = example_df.groupby('even')
    # The groups attribute is a dictionary mapping keys to lists of row indexes
    print grouped_data.groups
    
# Group by multiple columns
if True:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print grouped_data.groups
    
# Get sum of each group
if True:
    grouped_data = example_df.groupby('even')
    print grouped_data.sum()
    
# Limit columns in result
if True:
    grouped_data = example_df.groupby('even')
    
    # You can take one or more columns from the result DataFrame
    print grouped_data.sum()['value']
    
    print '\n' # Blank line to separate results
    
    # You can also take a subset of columns from the grouped data before 
    # collapsing to a DataFrame. In this case, the result is the same.
    print grouped_data['value'].sum()
    

import os
basepath = os.path.abspath('16_Pandas_groupby.py')
dname = os.path.dirname(basepath)
os.chdir(dname)

# Declare the data file path

if os.environ['COMPUTERNAME'] == 'JDAZO':
    filepath = os.path.normpath(os.path.join(basepath,'..\\..\\..\\data\\' \
                                             'nyc_subway_weather.csv'))
    
elif os.environ['COMPUTERNAME'] == 'MELLOYELLO':
    filepath = os.path.normpath(os.path.join(basepath,'..\\..\\..\\data\\' \
                                             'nyc_subway_weather.csv'))
    
# Load the subway dataset    
    
subway_df = pd.read_csv(filepath)
    
# Glimpse at the top few records
print(subway_df.head())


### Write code here to group the subway data by a variable of your choice, then
### either print out the mean ridership within each group or create a plot.


# Group by the station ID    
stations = subway_df.groupby('UNIT')
station_ridership = stations['ENTRIESn_hourly'].mean()
print(station_ridership.head(n=5))

'''
# Subway ridership by day of the week
'''
subway_df.head()
subway_df.groupby('day_week')
subway_df.groupby('day_week').mean()

subway_df.groupby('day_week').mean()['ENTRIESn_hourly']
ridership_by_day = subway_df.groupby('day_week').mean()['ENTRIESn_hourly']

#%pylab inline
import seaborn as sns

ridership_by_day.plot()

print('\n')







