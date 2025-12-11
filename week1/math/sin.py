import math
angle = int(input("Enter an angle between base and hypotenuse: "))
hypo = int(input("Enter the hypotenuse of right angle triangle in meters: "))
height = hypo * math.sin(math.radians(angle))
print("The lenght of height of triangle is: ",round(height,2))