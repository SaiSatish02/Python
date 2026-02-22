from functools import reduce

t = (2,12,15,18,19,25)

t1 = tuple(map(lambda x: x**2, t))
print("Square of the Tuple is:", t1)

t2 = tuple(filter(lambda x: x % 2 == 0, t))
print("Even numbers of Tuplpe:", t2)

t3 = reduce(lambda x, y: x + y, t)
print("Sum of the Tuple:", t3)