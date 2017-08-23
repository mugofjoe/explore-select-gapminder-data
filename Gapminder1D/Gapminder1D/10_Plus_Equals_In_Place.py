# exec(open(".//10_Plus_Equals_In_Place.py"))
print "Executing: 10_Plus_Equals"


# In-Place Operation
import numpy as np
a = np.array([1,2,3,4])
b = a
a += np.array([1,1,1,1])
print b 

# Not In-Place Operation
import numpy as np
a = np.array([1,2,3,4])
b = a
a = a + np.array([1,1,1,1])
print b 

# A slice is a view of the array
import numpy as np
a = np.array([1,2,3,4,5])
slice = a[:3]   # up to but not including position 3
slice[0] = 100
print a 



