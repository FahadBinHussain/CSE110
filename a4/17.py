# inpu1 = input()
# inpu2 = input()

# outpu = ""
# inpu1 += inpu2

# for i in inpu1:
#   if i != inpu2:
#     outpu += i
#   else:
#     print(outpu)
#     outpu = ""

# Taking inputs from user
string = input("Enter a string: ")
splitter = input("Enter the character to split on: ")

# Initializing an empty list to store the words
words = ''

# Initializing an empty string to store the current word
current_word = ''

for char in string:
    if char == splitter:
        print(current_word)
        current_word = ""
    else:
        current_word += char

if current_word != "":
    print(current_word)