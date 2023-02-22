#Write a Python program that will ask the user to enter a word as an input. 
# If the length of the input string is less than 4, then your program should print the same string as an output. 
# If the input string’s length is greater than 3, then your program should add "er" at the end of the input string. 
# If the input string already ends with "er", then add "est" instead, regardless of the length of the input string
# If the input string already ends with "est", then your program should print the same input string as an output.

user = input("Enter a word: ")
if len(user) < 4 or user[-3:] == "est":
    print(user)
elif user[-2:] == "er":
    print(user[:-2] + "est")
elif len(user) > 3:
    print(user + "er")


