try:
    file = open("sample","r")

    temp4=file.readlines()

    print(temp4)
except FileNotFoundError:
    print("File does not exist..")