a,b = map(int,input("enter two numbers: ").split())
while b != 0:
    a, b = b, a % b
print(f"GCD is {a}")
