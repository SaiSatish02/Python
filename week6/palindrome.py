str = input("Enter a string: ")
if str == str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not a palindrome")