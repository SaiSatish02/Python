import math

radius = int(input("Enter radius of circle: "))
print(math.pi)
area = math.pi*radius*radius
print("Area of circle is: ",round(area,2))
perimeter = 2*math.pi*radius
print("Perimeter of circle is: ",round(perimeter,2))