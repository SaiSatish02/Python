import random 
file=open("randoms","w")
for i in range(20):
    num=random.randint(1,100)
    file.write(str(num)+"\n")
print("Written Successfully")
