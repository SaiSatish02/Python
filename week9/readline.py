try:
    file = open("sample","r")

    temp1=file.readline()
    temp2=file.readline()
    temp3=file.readline()

    print(temp1)
    print(temp2)
    print(temp3)
except FileNotFoundError:
    print("File does not exist..")
