# exec(open(".//15_Filling_Missing_Values.py"))
print "Executing: 15 Filling Missing Values\n"

import pandas as pd
s1 = pd.Series([1, 2, 3, 4], index=['a','b','c','d'])
s2 = pd.Series([10, 20, 30, 40], index=['c','d','e','f'])

sum_result = s1 + s2
sum_result.dropna()


s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])

# Try to write code that will add the 2 previous series together,
# but treating missing values from either series as 0. The result
# when printed out should be similar to the following line:
# print pd.Series([1, 2, 13, 24, 30, 40], index=['a', 'b', 'c', 'd', 'e', 'f'])

s1.add(s2, fill_value=0)

