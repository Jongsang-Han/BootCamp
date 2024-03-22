import numpy as np

array1 = np.random.uniform(size=(5,3))
array2 = np.random.uniform(size=(3,2))
dot = array1@array2

#print (array1)
#print (array2)
print (dot, dot.shape)
