import os
try:
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    if os.path.exists(source):
        with open(source, 'r') as file1:
            data = file1.read()

        with open(destination, 'w') as file2:
            file2.write(data)

        print("File copied successfully.")
except FileNotFoundError:
    print("Source file does not exist.")