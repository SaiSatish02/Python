n= int(input("Enter a number: "))
for i in range(2,int(n/2)+1):
    if n%i==0:
        print(f"{n} is not a prime number")
        break
else:
    print(f"{n} is a prime number")
        
