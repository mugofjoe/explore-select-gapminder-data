# exec(open(".//08_Calculating_Correlation.py"))
print "Executing Calculating Correlation"

import pandas as pd
filename = '..//..//data/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)

'''
Correlation using numpy corrcoef()
'''

def correlation_corrcoef(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    import numpy as np
    corr_coef = np.corrcoef(x, y)[1,0]

    return corr_coef

'''
Udacity solution
'''

def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.
    
    correlation = average of (x in standard units) times (y in standard units)
    
    Remember to pass the argument "ddof=0" to the Pandas std() function!
    std(ddof=0) is called the uncorrected standard deviation.
    '''

    # Standardize the scores for x and y
    std_x = (x - x.mean()) / x.std(ddof=0)
    std_y = (y - y.mean()) / y.std(ddof=0)

    return (std_x * std_y).mean()


entries = subway_df['ENTRIESn_hourly']  # number of entries each hour
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

correlation(entries, rain)




