#Write a program that takes a string as input and prints “Binary Number” if the string contains only 0s or 1s. Otherwise, print “Not a Binary Number”
user = input("Enter a string: ")

if user.count("0") + user.count("1") == len(user):
    print("Binary Number")
else:
    print("Not a Binary Number")