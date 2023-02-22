#Write a Python program that will ask the user to input a string (containing exactly one word). Then your program should print subsequent substrings of the given string as shown in the examples below.
user = input("Enter a string: ")
for row in range(len(user)):
    for col in range(row + 1):
        print(user[col], end="")
    print()
        