# inpu1 = input()
# inpu2 = input()

# outpu = ""

# for i in inpu1:
#   if i != inpu2:
#     outpu += i
    
# if len(inpu1) > 3 and outpu == inpu1:
#   print(outpu[1:len(outpu) - 1])
# else:
#   print(outpu)

# Get input from user
string = input("Enter a string: ")
letter = input("Enter a letter: ")

# Remove all occurrences of the letter from the string
new_string = ''
for char in string:
    if char != letter:
        new_string += char

# Check if the letter was found in the string
if letter not in string and len(string) > 3:
    # If letter not found and length of string is greater than 3,
    # remove first and last characters of the string
    new_string = string[1:-1]

# Print the resulting string
print(new_string)
