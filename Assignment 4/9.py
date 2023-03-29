# Take input from user
input_str = input("Enter a string: ")

# Initialize the new string
new_str = input_str[0]

# Iterate through the input string and add characters to the new string
for i in range(1, len(input_str)):
    # Check if the current character is the same as the previous character
    if input_str[i] != input_str[i-1]:
        new_str += input_str[i]

# Print the resulting string
print(new_str)
