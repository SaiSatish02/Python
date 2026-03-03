try:
    file = open("sample","+a")
    file.writelines(["\nThis is Python lab","\nMake sure to listen Carefully"])
except FileNotFoundError:
    print("File does not exist..")