#Right Angled Triangle
print("Area of Right Angled Triangle Calculation")
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_rt = 0.5 * base * height
print("Area of the Right Angled Triangle is:", round(area_rt,2))
#Equilateral Triangle
print("Area of Equilateral Triangle Calculation")
side = float(input("Enter the side of the triangle: "))
area_eq = (3**0.5 / 4) * side * side
print("Area of the Equilateral Triangle is:", round(area_eq,2)) 
#Area using Heron's Formula
print("Area of Triangle using Heron's Formula Calculation")
a = float(input("Enter side a of the triangle: "))
b = float(input("Enter side b of the triangle: "))
c = float(input("Enter side c of the triangle: "))
s = (a + b + c) / 2
area_heron = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the Triangle using Heron's Formula is:", round(area_heron,2))
