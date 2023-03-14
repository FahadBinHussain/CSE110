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
