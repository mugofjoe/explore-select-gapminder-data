# exec(open(".//17_Plotting_In_Pandas.py"))
print "Executing: 17_Plotting_In_Pandas\n"

import pandas as pd
import seaborn as sns

path = '..\\..\\data\\'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for
# the United States. You can change the string 'United States' 
# to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']

# Uncomment the following line of code to see the available country names
print employment.index.values

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".

employment_us.hist()
employment_us.plot()

female_completion_us.hist()
female_completion_us.plot()

male_completion_us.hist()
male_completion_us.plot()

life_expectancy_us.hist()
life_expectancy_us.plot()

gdp_us.hist()
gdp_us.plot()