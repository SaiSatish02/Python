try:
    file = open("sample","w+")
    file.write("Hello !!\nThis is files in python\nI am  Jinglesa")
    print("Written content successfully")
except FileNotFoundError:
    print("File does not exist..")
