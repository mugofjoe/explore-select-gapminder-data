# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 13:41:08 2017

@author: jdazo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3 
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for this block of code to see what it does

# groupby() without as_index
if True:
    first_even = example_df.groupby('even').first()
    print first_even
    print first_even['even'] # Causes an error. 'even' is no longer a column in the DataFrame
    
# groupby() with as_index=False
if False:
    first_even = example_df.groupby('even', as_index=False).first()
    print first_even
    print first_even['even'] # Now 'even' is still a column in the DataFrame

# filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
# subway_df = pd.read_csv(filename)

## Make a plot of your choice here showing something interesting about the subway data.
## Matplotlib documentation here: http://matplotlib.org/api/pyplot_api.html
## Once you've got something you're happy with, share it on the forums!

'''
Udacity Solution
'''
import numpy as np
import pandas as pd

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
    
# Make a scatterplot of subway stations with latitude and longitude
# as the x and y axes and ridership as the bubble size

# prevent the latitude and longitude from becoming the row indexes
# for the dataframe by using as_index=False

data_by_location = subway_df.groupby(['latitude', 'longitude'],
                                     as_index=False).mean()

data_by_location.head()['latitude']

%pylab inline
import matplotlib.pyplot as plt
import seaborn as sns

scaled_entries = (data_by_location['ENTRIESn_hourly'] /
                  data_by_location['ENTRIESn_hourly'].std())


plt.scatter(data_by_location['latitude'], data_by_location['longitude'],
            s=data_by_location['ENTRIESn_hourly'])


