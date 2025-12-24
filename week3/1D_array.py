import numpy as np

lst1 = [2,15,18,25,19]
npArr = np.array(lst1)
print("Array: ",npArr)
print("Dimension: ",npArr.ndim)
x = np.zeros(5)
print("Array with zeros: ",x)
y = np.ones(3)
print("Array with ones: ",y)

z = np.arange(5)
print("After arranging: ",z)

print("Sum of elements: ",np.sum(npArr))
print("Sum : ",npArr.sum())

print("Maximum Element: ",np.max(npArr))
print("Max: ",npArr.max())

print("Minimum Element: ",np.min(npArr))
print("Min: ",npArr.min())

print("Average of elements: ",np.mean(npArr))
print("Average: ",npArr.mean())

print("Indexing the elements: ",npArr[0],npArr[-1])
print("Slicing of Array: ",npArr[0:3])
