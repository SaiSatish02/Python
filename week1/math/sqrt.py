import math

a,b,c = map(int,input("Enter co-efficients of quadratic equation:").split())
root1 = ((-b)+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
root2 = ((-b)-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
print("Root 1 is:",round(root1,2))
print("Root 2 is:",round(root2,2))