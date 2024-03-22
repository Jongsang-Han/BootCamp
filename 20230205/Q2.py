import numpy as np

array1 = np.array([[5,7],[9,11]], float)
array2 = np.array([[2,4],[6,8]], float)

concat_1 = np.concatenate((array1,array2),axis=0)
concat_2 = np.concatenate((array1,array2),axis=1)

print (concat_1)
print (concat_2)
