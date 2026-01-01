x,y,z = map(int, input("Enter three numbers separated by space: ").split())
choice =input("Enter your choice (min/max): ")
if choice == "min":
    if x<y and x<z:
        print(f"{x} is smallest")
    elif y<z :
        print(f"{y} is smallest") 
    else :
        print(f"{z} is smallest")
        
else:
    if x>y and x>z:
        print(f"{x} is greatest")
    elif y>z :
        print(f"{y} is greatest") 
    else :
        print(f"{z} is greatest")
