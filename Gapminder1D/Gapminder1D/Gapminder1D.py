'''
Udacity Questions on Gapminder data
1. How has employment in the U.S. (or another country) varied over time?
2. In the most recent year we have data on, what are the highest and lowest employment levels?
    - which countries have them?
    - where is the U.S. on the spectrum

Same questions for other variables
How do these variables relate to each other?
Are there consistent trends across countries?
  - have there been any global recessions?
  - can we find them in this data?

'''

# 
# Load data using pandas
#

import pandas as pd
daily_engagement_full = pd.read_csv('..\\..\\data\\daily_engagement_full.csv')
print("Total accounts daily engagement: {}".format(len(daily_engagement_full)))

# Use pandas unique function to 
# get unique engagement accounts 

count_unique_engagement = len(daily_engagement_full['acct'].unique())
print("Unique accounts daily engagement: {}".format(count_unique_engagement))

