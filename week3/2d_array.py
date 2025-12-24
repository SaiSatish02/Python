import numpy as np
lst1 = [[2, 15], [25, 30]]
lst2 = [[40, 45], [55, 60]]
a = np.array(lst1)
b = np.array(lst2)
print("Array1:\n", a)
print("Array2:\n", b)
print("Dimensions of Array1:", a.ndim)
print("Dimensions of Array2:", b.ndim)
print("Sum of Arrays: \n", np.add(a, b))
print("Difference of Arrays: \n", np.subtract(a, b))
print("Multiplication of Arrays: \n", np.dot(a, b))
# print("subtraction of Arrays: \n", np.subtract(a, b))
print("Inverse of Array1:\n",np.linalg.inv(a))
print("Transpose of Array1:\n", np.transpose(a))
print("Trace of Array1:\n", np.trace(a))
print("Determinant of Array1:\n", np.linalg.det(a))
# print("eigenvalues of Array1:\n", np.linalg.eigvals(a))
# print("eigenvalues and eigenvectors of Array1:\n", np.linalg.eig(a))


