#Write a Python program that will ask the user to input a string (containing exactly one word). Then print the ASCII code for each character in the String using the ord() function. 
user = input("Please enter a word: ")
for i in user:
    print(f"{i} : {ord(i)}")
