n = int(input("Enter a number: "))
f = 0
s = 1
print("Fibonacci Series:")
for i in range(n):
    print(f, end=' ')
    next = f + s
    f = s
    s = next
    