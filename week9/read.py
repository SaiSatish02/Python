try:
    file = open("sample","r")

    temp=file.read()
   
    print(temp)

except FileNotFoundError:
    print("File does not exist..")