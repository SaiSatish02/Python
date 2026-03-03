import os
try:
    source = input("Enter source file name: ")
    destination = input("Enter new file name or path: ")

    if os.path.exists(source):
        os.rename(source, destination)
        print("File moved successfully.")

except FileNotFoundError:
    print("Source file does not exist.")