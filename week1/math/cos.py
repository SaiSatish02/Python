import math
angle = int(input("Enter an angle between base and hypotenuse: "))
hypo = int(input("Enter the hypotenuse of right angle triangle in meters: "))
base = hypo * math.cos(math.radians(angle))
print("The lenght of base of triangle is: ",round(base,2))