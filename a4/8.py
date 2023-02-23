# Take input from user
input_str = input("Enter a string: ")

# Remove characters at even index
result_str = ""
for i in range(len(input_str)):
    if i % 2 != 0:
        result_str += input_str[i]

# Convert result string to uppercase without using upper()
uppercase_str = ""
for char in result_str:
    if ord('a') <= ord(char) <= ord('z'):
        uppercase_str += chr(ord(char) - 32)
    else:
        uppercase_str += char

# Print the resulting string in uppercase
print(uppercase_str)
