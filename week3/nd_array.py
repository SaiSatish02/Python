import numpy as np
array = np.ndarray((5),dtype=int)
array[:] = [10,20,30,40,50]
print("1D Array elements are:", array)

array2 = np.ndarray((3,3),dtype=int)
array2[:] = [[1,2,3],[4,5,6],[7,8,9]]
print("3D Array elements are:\n", array2)
