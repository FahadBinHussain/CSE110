# Get input string from user
input_str = input("Enter a string containing all small letters: ")

# Iterate over each character in the input string
for char in input_str:
    # Get the ASCII value of the current character
    ascii_val = ord(char)
    # Check if the character is 'z'
    if ascii_val == 122:
        # If so, set the next character to 'a'
        next_char = 'a'
    else:
        # Otherwise, get the next character by adding 1 to the ASCII value
        next_ascii_val = ascii_val + 1
        next_char = chr(next_ascii_val)
    # Print the next character
    print(next_char, end="")
